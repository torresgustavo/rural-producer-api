from typing import Dict
from api.models.farm_rural_producer_model import FarmRuralProducer
from api.repositories.farm_rural_producer_repository import (
    FarmRuralProducerRepository,
)
from api.schemas.dashboard_schemas import DashboardDataSchema, PerAnythingSchema
from api.repositories.farm_rural_culture_producer_repository import (
    FarmCultureRuralProducerRepository,
)


class DashboardDataCalculatorService:

    def __init__(
        self,
        farm_rural_producer_repository: FarmRuralProducerRepository,
        farm_culture_rural_producer_repository: FarmCultureRuralProducerRepository,
    ):
        self.__farm_rural_producer_repository = farm_rural_producer_repository
        self.__farm_culture_rural_producer_repository = (
            farm_culture_rural_producer_repository
        )

    def execute(self):
        farms = self.__farm_rural_producer_repository.get_all()

        state_dictionary: Dict[str, PerAnythingSchema] = {}
        culture_dictionary: Dict[str, PerAnythingSchema] = {}

        farms_count = 0
        total_area = 0
        total_arable_area = 0
        total_vegetation_area = 0

        for farm in farms:
            farms_count += 1
            total_area += farm.total_hectare_area
            total_arable_area += farm.arable_hectare_area
            total_vegetation_area += farm.vegetation_hectare_area

            state_dictionary = self.__handle_state_data(state_dictionary, farm)
            culture_dictionary = self.__handle_culture_data(culture_dictionary, farm)

        return DashboardDataSchema.model_validate(
            {
                "farms_count": farms_count,
                "total_area": total_area,
                "total_arable_area": total_arable_area,
                "total_vegetation_area": total_vegetation_area,
                "per_state": state_dictionary,
                "per_culture": culture_dictionary,
            }
        )

    def __handle_state_data(
        self, state_dictionary: Dict[str, PerAnythingSchema], farm: FarmRuralProducer
    ):
        state_name = farm.rural_producer.state.upper()

        state = state_dictionary.get(state_name, None)
        if state is not None:
            state_dictionary[state_name].farms_count += 1
            state_dictionary[state_name].total_area += farm.total_hectare_area
            state_dictionary[state_name].total_arable_area += farm.arable_hectare_area
            state_dictionary[
                state_name
            ].total_vegetation_area += farm.vegetation_hectare_area
        else:
            state_dictionary[state_name] = PerAnythingSchema.model_validate(
                {
                    "farms_count": 1,
                    "total_area": farm.total_hectare_area,
                    "total_arable_area": farm.arable_hectare_area,
                    "total_vegetation_area": farm.vegetation_hectare_area,
                }
            )

        return state_dictionary

    def __handle_culture_data(
        self, culture_dictionary: Dict[str, PerAnythingSchema], farm: FarmRuralProducer
    ):
        cultures = self.__farm_culture_rural_producer_repository.get_by_farm(farm.id)
        for culture in cultures:
            culture_name = culture.farm_culture_type.name.title()
            culture = culture_dictionary.get(culture_name, None)
            if culture is not None:
                culture_dictionary[culture_name].farms_count += 1
                culture_dictionary[culture_name].total_area += farm.total_hectare_area
                culture_dictionary[
                    culture_name
                ].total_arable_area += farm.arable_hectare_area
                culture_dictionary[
                    culture_name
                ].total_vegetation_area += farm.vegetation_hectare_area
            else:
                culture_dictionary[culture_name] = PerAnythingSchema.model_validate(
                    {
                        "farms_count": 1,
                        "total_area": farm.total_hectare_area,
                        "total_arable_area": farm.arable_hectare_area,
                        "total_vegetation_area": farm.vegetation_hectare_area,
                    }
                )

        return culture_dictionary
