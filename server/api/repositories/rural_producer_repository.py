from uuid import UUID

from django.db.models.manager import BaseManager
from api.errors.rural_producer_not_found import RuralProducerNotFoundError

from api.models.rural_producer_model import RuralProducer
from api.models.base import BaseModel


class RuralProducerRepository:
    def get_by_id(self, id: UUID) -> RuralProducer:
        try:
            result = RuralProducer.objects.get(id=str(id))
            return result
        except RuralProducer.DoesNotExist:
            raise RuralProducerNotFoundError(str(id))

    def get_all(self) -> BaseManager[RuralProducer]:
        result = RuralProducer.objects.all()
        return result

    def get_by_document(self, document_number: str) -> RuralProducer:
        result = RuralProducer.objects.get(document_number=document_number)

        if result is None:
            raise RuralProducerNotFoundError(document_number)

        return result

    def save(self, model: BaseModel):
        model.save()

    def remove(self, model: BaseModel):
        model.delete()
