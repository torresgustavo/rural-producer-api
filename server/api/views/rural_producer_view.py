from typing import List
from ninja import Router
from ninja.responses import Response
from django.http.request import HttpRequest

from api.repositories.rural_producer_repository import RuralProducerRepository

from api.schemas.rural_producers_schemas import RuralProducersSchema

__rural_producers_repository = RuralProducerRepository()

router = Router()


@router.get("", response=List[RuralProducersSchema])
def list(request: HttpRequest):
    rural_producers = __rural_producers_repository.get_all()
    if len(rural_producers) == 0:
        return Response([])

    data = [RuralProducersSchema.from_orm(producer) for producer in rural_producers]
    return Response(data)


@router.get('/{document_number}')
def get_by_document(request: HttpRequest, document_number: str):

    rural_producer = __rural_producers_repository.get_by_document(document_number)

    data = RuralProducersSchema.from_orm(rural_producer)

    return Response(data)
