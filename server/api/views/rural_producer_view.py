from typing import List
from ninja import Router
from ninja.responses import Response
from ninja.errors import ValidationError

from django.db import transaction
from django.http.request import HttpRequest

from api.repositories.rural_producer_repository import RuralProducerRepository

from api.schemas.rural_producers_schemas import NewRuralProducerSchema, RuralProducersSchema
from api.services.add_rural_producer_service import AddRuralProducerService
from api.validators.rural_producer_validator import RuralProducerValidator

__rural_producers_repository = RuralProducerRepository()
__rural_producers_validator = RuralProducerValidator(
    rural_producer_repository=__rural_producers_repository
)

router = Router(tags=['Rural Producer Management'])


@router.get(
    "", 
    response=List[RuralProducersSchema],
    summary='List all rural producer',
    description='List all rural producer registered'
)
def list(request: HttpRequest):
    rural_producers = __rural_producers_repository.get_all()
    if len(rural_producers) == 0:
        return Response([])

    data = [RuralProducersSchema.from_orm(producer) for producer in rural_producers]
    return Response(data)


@router.get(
    '/{document_number}', 
    response=RuralProducersSchema,
    summary='Get rural producer by documento',
    description='Get rural producer by document number'
)
def get_by_document(request: HttpRequest, document_number: str):

    rural_producer = __rural_producers_repository.get_by_document(document_number)

    data = RuralProducersSchema.from_orm(rural_producer)

    return Response(data)

@router.post(
    '',
    summary='Register new rural producer',
    response={
        200: RuralProducersSchema
    }
)
@transaction.atomic
def add_producer(request: HttpRequest, new_rural_producer: NewRuralProducerSchema):
    service = AddRuralProducerService(
        rural_producer_repository=__rural_producers_repository,
        rural_producer_validator=__rural_producers_validator,
        rural_producer_to_add=new_rural_producer
    )
    rural_producer_added = service.execute()

    data = RuralProducersSchema.from_orm(rural_producer_added)
    return Response(data)
