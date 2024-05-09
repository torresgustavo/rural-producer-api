from uuid import UUID

from api.repositories.farm_rural_culture_producer_repository import (
    FarmCultureRuralProducerRepository,
)
from api.models.farm_rural_producer_model import FarmRuralProducer
from api.repositories.farm_rural_producer_repository import (
    FarmRuralProducerRepository,
)


class RemoveFarmCultureRuralProducerService:

    def __init__(
        self,
        farm_culture_rural_producer_repository: FarmCultureRuralProducerRepository,
        farm_rural_producer_repository: FarmRuralProducerRepository,
    ) -> None:
        self.__farm_rural_producer_repository = farm_rural_producer_repository
        self.__farm_culture_rural_producer_repository = (
            farm_culture_rural_producer_repository
        )

    def execute(self, farm_id: UUID, farm_culture_type_id: int) -> FarmRuralProducer:
        farm_culture = (
            self.__farm_culture_rural_producer_repository.get_by_farm_and_culture(
                farm_id=farm_id, culture_id=farm_culture_type_id
            )
        )
        self.__farm_culture_rural_producer_repository.remove(farm_culture)

        return self.__farm_rural_producer_repository.get_by_id(farm_id)
