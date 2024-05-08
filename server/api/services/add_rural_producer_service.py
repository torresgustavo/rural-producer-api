import logging
from typing import Callable, List

from django.forms import ValidationError

from api.utils.document_validators import cpf_validator, cnpj_validator

from api.repositories.rural_producer_repository import RuralProducerRepository
from api.schemas.rural_producers_schemas import NewRuralProducerSchema
from api.enums.document_types_enum import DocumentTypesEnum
from api.models.farm_culture_rural_producer_model import FarmCultureRuralProducer
from api.models.farm_rural_producer_model import FarmRuralProducer
from api.models.rural_producer_model import RuralProducer
from api.validators.rural_producer_validator import RuralProducerValidator


class AddRuralProducerService():

    def __init__(
            self,
            rural_producer_validator: RuralProducerValidator,
            rural_producer_repository: RuralProducerRepository,
            rural_producer_to_add: NewRuralProducerSchema
        ):
        self.__rural_producer_validator = rural_producer_validator
        self.__rural_producer_repository = rural_producer_repository

        self.rural_producer_to_add = rural_producer_to_add

    def execute(self):
        rural_producer = RuralProducer(
            name=self.rural_producer_to_add.name,
            document_number=self.rural_producer_to_add.document_number,
            document_type=self.rural_producer_to_add.document_type,
            city=self.rural_producer_to_add.city,
            state=self.rural_producer_to_add.state,
        )
        self.__rural_producer_repository.save(rural_producer)
        
        farm = FarmRuralProducer(
            rural_producer_id=rural_producer.id,
            name=self.rural_producer_to_add.farm.name,
            total_hectare_area=self.rural_producer_to_add.farm.total_hectare_area,
            arable_hectare_area=self.rural_producer_to_add.farm.arable_hectare_area,
            vegetation_hectare_area=self.rural_producer_to_add.farm.vegetation_hectare_area
        )
        self.__rural_producer_repository.save(farm)

        cultures = []
        for culture_pre_add in self.rural_producer_to_add.farm.cultures:
            culture = FarmCultureRuralProducer(
                farm_culture_type_id=culture_pre_add.farm_culture_type_id,
                farm_id=farm.id
            )
            cultures.append(culture)
            self.__rural_producer_repository.save(culture)

        self.__validate(rural_producer=rural_producer, farm=farm, cultures=cultures)
        
        return rural_producer

    
    def __validate(self, rural_producer: RuralProducer, farm: FarmRuralProducer, cultures: List[FarmCultureRuralProducer]):
        self.__rural_producer_validator.validate_document(rural_producer)
        self.__rural_producer_validator.validate_cultures(cultures)
        self.__rural_producer_validator.validate_farm_area(farm)
