from uuid import UUID

from api.errors.farm_rural_producer_culture_not_found import (
    FarmRuralProducerCultureNotFound,
)
from api.models.farm_culture_rural_producer_model import FarmCultureRuralProducer


class FarmCultureRuralProducerRepository:

    def get_by_farm_and_culture(
        self, farm_id: UUID, culture_id: int
    ) -> FarmCultureRuralProducer:
        try:
            result = FarmCultureRuralProducer.objects.get(
                farm_id=str(farm_id), farm_culture_type_id=culture_id
            )
            return result
        except FarmCultureRuralProducer.DoesNotExist:
            raise FarmRuralProducerCultureNotFound(
                culture_id=culture_id, farm_id=farm_id
            )

    def save(self, model: FarmCultureRuralProducer) -> FarmCultureRuralProducer:
        model.save()
        return model

    def remove(self, model: FarmCultureRuralProducer) -> None:
        model.delete()
