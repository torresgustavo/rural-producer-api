from api.errors.rural_producer_not_found import RuralProducerNotFoundError

from api.models.rural_producer_model import RuralProducer

class RuralProducerRepository:

    def get_all(self):
        result = RuralProducer.objects.all()
        return result

    def get_by_document(self, document_number: str):
        result = RuralProducer.objects.get(document_number=document_number)

        if result is None:
            raise RuralProducerNotFoundError(document_number)

        return result
