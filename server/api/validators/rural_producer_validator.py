from typing import Callable, List

from ninja.errors import ValidationError
from api.errors.rural_producer_not_found import RuralProducerNotFoundError

from api.repositories.rural_producer_repository import RuralProducerRepository

from api.models.rural_producer_model import RuralProducer
from api.models.farm_culture_rural_producer_model import FarmCultureRuralProducer

from api.enums.document_types_enum import DocumentTypesEnum
from api.models.farm_rural_producer_model import FarmRuralProducer
from api.models.farm_culture_type_model import FarmCultureType


class RuralProducerValidator():

    def __init__(
            self,
            rural_producer_repository: RuralProducerRepository
        ):
        self.__rural_producer_repository = rural_producer_repository

    def validate_document(self, rural_producer: RuralProducer):
        try:
            rural_producer_registered = self.__rural_producer_repository.get_by_document(rural_producer.document_number)

            if rural_producer_registered and rural_producer.id != rural_producer_registered.id:
                raise self.__create_validation_error(
                    valid=False,
                    message='Document already registered',
                    error_code='DOCUMENT_ALREADY_REGISTERED'
                )
        except (RuralProducerNotFoundError, RuralProducer.DoesNotExist):
            pass


        if rural_producer.document_type not in DocumentTypesEnum:
            raise self.__create_validation_error(
                valid=False,
                message='Document type is invalid',
                error_code='INVALID_DOCUMENT_TYPE'
            )

        document_validator: Callable[[str], bool] = DocumentTypesEnum.get_validator(rural_producer.document_type)
        is_valid = document_validator(rural_producer.document_number)
        
        if is_valid is False:
            raise self.__create_validation_error(
                valid=False,
                message=f'{rural_producer.document_type} is not valid',
                error_code='INVALID_DOCUMENT_NUMBER'
            )
    
    def validate_farm_area(self, farm: FarmRuralProducer):
        sum_total_area = farm.arable_hectare_area + farm.vegetation_hectare_area
        total_area = farm.total_hectare_area

        if total_area <= 0:
            raise self.__create_validation_error(
                valid=False,
                message='Total area shoud be more than 0 hectare',
                error_code='FARM_AREA_INVALID'
            )

        if sum_total_area > total_area:
            raise self.__create_validation_error(
                valid=False,
                message='The sum of arable and vegetation areas goes beyond the total farm',
                error_code='FARM_AREA_INVALID'
            )
    
    def validate_cultures(self, cultures: List[FarmCultureRuralProducer]):
        for culture in cultures:

            try:
                hasattr(culture, 'farm_culture_type')
            except FarmCultureType.DoesNotExist:
                raise self.__create_validation_error(
                    valid=False,
                    error_code='FARM_CULTURE_NOT_FOUND',
                    message=f'Farm culture not registered'
                )

            repeated_culture = list(filter(lambda c: c.farm_culture_type == culture.farm_culture_type, cultures))
            if len(repeated_culture) > 1:
                raise self.__create_validation_error(
                    valid=False,
                    error_code='FARM_CULTURE_REPEATED',
                    message=f'Farm culture {culture.farm_culture_type.name} repeated in the culture list'
                )

    

    def __create_validation_error(self, valid: bool, message: str = None, error_code: str = None) -> ValidationError:
        return ValidationError({
            'valid': valid,
            'error_message': message,
            'error_code': error_code
        })