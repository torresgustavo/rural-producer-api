from typing import List
from uuid import UUID

from api.errors.farm_rural_producer_not_found import FarmRuralProducerNotFound
from api.models.farm_rural_producer_model import FarmRuralProducer


class FarmRuralProducerRepository:

    def get_all(self) -> List[FarmRuralProducer]:
        result = [farm for farm in FarmRuralProducer.objects.all()]
        return result

    def get_by_id(self, id: UUID) -> FarmRuralProducer:
        try:
            result = FarmRuralProducer.objects.get(id=str(id))
            return result
        except FarmRuralProducer.DoesNotExist:
            raise FarmRuralProducerNotFound(id)

    def save(self, model: FarmRuralProducer) -> FarmRuralProducer:
        model.save()
        return model

    def remove(self, model: FarmRuralProducer) -> None:
        model.delete()
