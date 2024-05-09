from typing import Optional
from uuid import UUID
from ninja.errors import ValidationError

from api.errors.rural_producer_not_found import RuralProducerNotFoundError

from api.repositories.rural_producer_repository import RuralProducerRepository

from api.schemas.rural_producers_schemas import EditRuralProducerSchema

from api.models.farm_rural_producer_model import FarmRuralProducer
from api.models.rural_producer_model import RuralProducer

from api.validators.rural_producer_validator import RuralProducerValidator
from api.utils.tools import clean_numerical_string


class EditRuralProducerService():

    def __init__(
            self,
            rural_producer_validator: RuralProducerValidator,
            rural_producer_repository: RuralProducerRepository,
            rural_producer_schema: EditRuralProducerSchema
        ) -> None:
        self.__rural_producer_validator = rural_producer_validator
        self.__rural_producer_repository = rural_producer_repository

        self.__rural_producer_schema = rural_producer_schema

        if self.__rural_producer_schema.document_number:
            self.__rural_producer_schema.document_number = clean_numerical_string(self.__rural_producer_schema.document_number)

    def execute(self, _id: UUID) -> RuralProducer:
        rural_producer = self.__rural_producer_repository.get_by_id(id=_id)
        self.__validate(rural_producer)

        self.__update_rural_producer(rural_producer)

        if self.__rural_producer_schema.farm is not None:
            self.__update_farm(rural_producer.farm)
        
        return rural_producer

    def __update_rural_producer(self, rural_producer: RuralProducer) -> RuralProducer:
        if self.__rural_producer_schema.name:
            rural_producer.name = self.__rural_producer_schema.name
        if self.__rural_producer_schema.document_type is not None:
            rural_producer.document_type = self.__rural_producer_schema.document_type
        if self.__rural_producer_schema.document_number is not None:
            rural_producer.document_number = clean_numerical_string(self.__rural_producer_schema.document_number)
        if self.__rural_producer_schema.city is not None:
            rural_producer.city = self.__rural_producer_schema.city
        if self.__rural_producer_schema.state is not None:
            rural_producer.state = self.__rural_producer_schema.state

        self.__rural_producer_repository.save(rural_producer)
        return rural_producer
    
    def __update_farm(self, farm: Optional[FarmRuralProducer]) -> Optional[FarmRuralProducer]:
        if farm is None:
            return farm
        
        if self.__rural_producer_schema.farm.name is not None:
            farm.name = self.__rural_producer_schema.farm.name

        if self.__rural_producer_schema.farm.total_hectare_area is not None:
            farm.total_hectare_area = self.__rural_producer_schema.farm.total_hectare_area

        if self.__rural_producer_schema.farm.arable_hectare_area is not None:
            farm.arable_hectare_area = self.__rural_producer_schema.farm.arable_hectare_area

        if self.__rural_producer_schema.farm.vegetation_hectare_area is not None:
            farm.vegetation_hectare_area = self.__rural_producer_schema.farm.vegetation_hectare_area
        
        self.__rural_producer_repository.save(farm)
        return farm

    def __validate(self, rural_producer_model: RuralProducer):

        document_to_validate = self.__rural_producer_schema.document_number if self.__rural_producer_schema.document_number else rural_producer_model.document_number
        document_type_to_validate = self.__rural_producer_schema.document_type if self.__rural_producer_schema.document_type else rural_producer_model.document_type

        self.__rural_producer_validator.validate_document(
            document_number=document_to_validate,
            document_type=document_type_to_validate,
            rural_producer_editing=rural_producer_model
        )

        if self.__rural_producer_schema.farm is None:
            return

        arable_hectare_area = self.__rural_producer_schema.farm.arable_hectare_area if self.__rural_producer_schema.farm.arable_hectare_area is not None else rural_producer_model.farm.arable_hectare_area
        vegetation_hectare_area = self.__rural_producer_schema.farm.vegetation_hectare_area if self.__rural_producer_schema.farm.vegetation_hectare_area is not None else rural_producer_model.farm.vegetation_hectare_area
        total_hectare_area = self.__rural_producer_schema.farm.total_hectare_area if self.__rural_producer_schema.farm.total_hectare_area is not None else rural_producer_model.farm.total_hectare_area

        self.__rural_producer_validator.validate_farm_area(
            arable_hectare_area=arable_hectare_area,
            vegetation_hectare_area=vegetation_hectare_area,
            total_hectare_area=total_hectare_area
        )
