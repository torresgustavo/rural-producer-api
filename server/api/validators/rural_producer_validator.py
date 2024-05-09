from decimal import Decimal
from typing import Callable, List, Optional

from ninja.errors import ValidationError
from api.errors.rural_producer_not_found import RuralProducerNotFoundError

from api.repositories.rural_producer_repository import RuralProducerRepository

from api.models.rural_producer_model import RuralProducer

from api.enums.document_types_enum import DocumentTypesEnum
from api.models.farm_culture_type_model import FarmCultureType
from api.repositories.farm_culture_types_repository import FarmCultureTypesRepository
from api.validators.document_validators import DocumentsValidator


class RuralProducerValidator:

    def __init__(
        self,
        rural_producer_repository: RuralProducerRepository,
        culture_types_repository: FarmCultureTypesRepository,
    ) -> None:
        self.__rural_producer_repository = rural_producer_repository
        self.__culture_types_repository = culture_types_repository

    def validate_document(
        self,
        document_type: str,
        document_number: str,
        rural_producer_editing: Optional[RuralProducer] = None,
    ):
        if document_type not in DocumentTypesEnum:
            raise self.__create_validation_error(
                valid=False,
                message="Document type is invalid",
                error_code="INVALID_DOCUMENT_TYPE",
            )
        is_valid = DocumentsValidator(
            document_number=document_number, document_type=document_type
        ).execute()

        if is_valid is False:
            raise self.__create_validation_error(
                valid=False,
                message=f"{document_type} is not valid",
                error_code="INVALID_DOCUMENT_NUMBER",
            )

        try:
            rural_producer_registered = (
                self.__rural_producer_repository.get_by_document(document_number)
            )
            if (
                rural_producer_editing
                and rural_producer_registered.id != rural_producer_editing.id
            ):
                raise self.__create_validation_error(
                    valid=False,
                    message="Document already registered",
                    error_code="DOCUMENT_ALREADY_REGISTERED",
                )
        except (RuralProducerNotFoundError, RuralProducer.DoesNotExist):
            pass

    def validate_farm_area(
        self,
        total_hectare_area: Decimal,
        arable_hectare_area: Decimal,
        vegetation_hectare_area: Decimal,
    ):
        sum_total_area = arable_hectare_area + vegetation_hectare_area

        if arable_hectare_area < 0:
            raise self.__create_validation_error(
                valid=False,
                message="Arable area shoud be more than 0 hectare",
                error_code="FARM_AREA_INVALID",
            )

        if vegetation_hectare_area < 0:
            raise self.__create_validation_error(
                valid=False,
                message="Vegetation area shoud be more than 0 hectare",
                error_code="VEGETATION_AREA_INVALID",
            )

        if total_hectare_area < 0:
            raise self.__create_validation_error(
                valid=False,
                message="Total area shoud be more than 0 hectare",
                error_code="FARM_AREA_INVALID",
            )

        if sum_total_area > total_hectare_area:
            raise self.__create_validation_error(
                valid=False,
                message="The sum of arable and vegetation areas goes beyond the total farm",
                error_code="FARM_AREA_INVALID",
            )

    def validate_cultures(self, cultures_type_id_list: List[int]) -> None:
        cultures_type = self.__culture_types_repository.get_all()
        for culture_type_id in cultures_type_id_list:
            try:
                culture = cultures_type.get(id=culture_type_id)
            except FarmCultureType.DoesNotExist:
                raise self.__create_validation_error(
                    valid=False,
                    error_code="FARM_CULTURE_NOT_FOUND",
                    message=f"Farm culture not registered",
                )

            repeated_culture = list(
                filter(
                    lambda culture_type_id: culture_type_id == culture.get("id"),
                    cultures_type_id_list,
                )
            )
            if len(repeated_culture) > 1:
                raise self.__create_validation_error(
                    valid=False,
                    error_code="FARM_CULTURE_REPEATED",
                    message=f"Farm culture {culture['name']} repeated in the culture list",
                )

    def __create_validation_error(
        self, valid: bool, message: str = None, error_code: str = None
    ) -> ValidationError:
        return ValidationError(
            {"valid": valid, "error_message": message, "error_code": error_code}
        )
