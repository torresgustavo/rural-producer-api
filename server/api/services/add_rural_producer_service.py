import re
from ninja.errors import ValidationError
from api.errors.rural_producer_not_found import RuralProducerNotFoundError

from api.repositories.rural_producer_repository import RuralProducerRepository

from api.schemas.rural_producers_schemas import NewRuralProducerSchema

from api.models.farm_culture_rural_producer_model import FarmCultureRuralProducer
from api.models.farm_rural_producer_model import FarmRuralProducer
from api.models.rural_producer_model import RuralProducer

from api.validators.rural_producer_validator import RuralProducerValidator
from api.utils.tools import clean_numerical_string


class AddRuralProducerService():

    def __init__(
            self,
            rural_producer_validator: RuralProducerValidator,
            rural_producer_repository: RuralProducerRepository,
            rural_producer_schema: NewRuralProducerSchema
        ):
        self.__rural_producer_validator = rural_producer_validator
        self.__rural_producer_repository = rural_producer_repository

        self.rural_producer_schema = rural_producer_schema
        if self.rural_producer_schema.document_number:
            self.rural_producer_schema.document_number = clean_numerical_string(self.rural_producer_schema.document_number)

    def execute(self):
        self.__validate()

        rural_producer = RuralProducer(
            name=self.rural_producer_schema.name,
            document_number=self.rural_producer_schema.document_number,
            document_type=self.rural_producer_schema.document_type,
            city=self.rural_producer_schema.city,
            state=self.rural_producer_schema.state,
        )
        self.__rural_producer_repository.save(rural_producer)
        
        farm = FarmRuralProducer(
            rural_producer_id=rural_producer.id,
            name=self.rural_producer_schema.farm.name,
            total_hectare_area=self.rural_producer_schema.farm.total_hectare_area,
            arable_hectare_area=self.rural_producer_schema.farm.arable_hectare_area,
            vegetation_hectare_area=self.rural_producer_schema.farm.vegetation_hectare_area
        )
        self.__rural_producer_repository.save(farm)

        cultures = []
        for culture_pre_add in self.rural_producer_schema.farm.cultures:
            culture = FarmCultureRuralProducer(
                farm_culture_type_id=culture_pre_add.farm_culture_type_id,
                farm_id=farm.id
            )
            cultures.append(culture)
            self.__rural_producer_repository.save(culture)
        
        return rural_producer

    
    def __validate(self):
        try:
            rural_producer_already_registered = self.__rural_producer_repository.get_by_document(self.rural_producer_schema.document_number)
            if rural_producer_already_registered:
                raise ValidationError({
                'valid': False,
                'error_message': 'Document already registered',
                'error_code': 'DOCUMENT_ALREADY_REGISTERED'
            })
        except (RuralProducerNotFoundError, RuralProducer.DoesNotExist):
            pass

        self.__rural_producer_validator.validate_document(
            document_number=self.rural_producer_schema.document_number,
            document_type=self.rural_producer_schema.document_type
        )
        self.__rural_producer_validator.validate_farm_area(
            arable_hectare_area=self.rural_producer_schema.farm.arable_hectare_area,
            vegetation_hectare_area=self.rural_producer_schema.farm.vegetation_hectare_area,
            total_hectare_area=self.rural_producer_schema.farm.total_hectare_area
        )

        culture_type_ids = [culture.farm_culture_type_id for culture in self.rural_producer_schema.farm.cultures]
        self.__rural_producer_validator.validate_cultures(culture_type_ids)
