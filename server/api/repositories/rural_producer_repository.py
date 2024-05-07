from typing import List

from api.errors.rural_producer_not_found import RuralProducerNotFoundError

from api.models.rural_producer_model import RuralProducer
from api.models.farm_rural_producer_model import FarmRuralProducer
from api.models.farm_culture_rural_producer_model import FarmCultureRuralProducer
from api.models.farm_culture_type_model import FarmCultureType


class RuralProducerRepository:

    def get_all(self):
        result = RuralProducer.objects.all()
        return result

    def get_by_document(self, document_number: str):
        result = RuralProducer.objects.filter(document_number=document_number).first()

        if result is None:
            raise RuralProducerNotFoundError(document_number)

        return result

    def get_rural_producer_farms(self, rural_producer_id: str):
        rural_producer = RuralProducer.objects.get(id=rural_producer_id)

        if rural_producer is None:
            return

        farm = FarmRuralProducer.objects.get(rural_producer=rural_producer)
        if farm is None:
            return (rural_producer, farm, None)

        farm_cultures = FarmCultureRuralProducer.objects.filter(farm_id=farm)

        return (rural_producer, farm, farm_cultures)
