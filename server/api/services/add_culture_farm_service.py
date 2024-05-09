from uuid import UUID

from api.schemas.rural_producers_schemas import AddNewFarmCultures
from api.validators.rural_producer_validator import RuralProducerValidator

from api.models.farm_rural_producer_model import FarmRuralProducer
from api.models.farm_culture_rural_producer_model import FarmCultureRuralProducer

from api.repositories.farm_rural_producer_repository import (
    FarmRuralProducerRepository,
)


class AddCultureFarmService:

    def __init__(
        self,
        rural_producer_validator: RuralProducerValidator,
        farm_rural_producer_repository: FarmRuralProducerRepository,
        culture_schema: AddNewFarmCultures,
    ):
        self.__rural_producer_validator = rural_producer_validator
        self.__farm_rural_producer_repository = farm_rural_producer_repository
        self.__culture_schema = culture_schema

    def execute(self, id: UUID) -> FarmRuralProducer:
        farm_rural_producer = self.__farm_rural_producer_repository.get_by_id(id)
        self.__validate(farm_rural_producer)

        for culture in self.__culture_schema.cultures:
            new_culture = FarmCultureRuralProducer(
                farm_culture_type_id=culture.farm_culture_type_id, farm_id=id
            )
            self.__farm_rural_producer_repository.save(new_culture)

        return farm_rural_producer

    def __validate(self, farm: FarmRuralProducer):
        culture_type_ids = [
            culture.farm_culture_type_id for culture in farm.cultures.all()
        ]
        culture_type_ids.extend(
            [culture.farm_culture_type_id for culture in self.__culture_schema.cultures]
        )
        self.__rural_producer_validator.validate_cultures(culture_type_ids)
