from django.http.request import HttpRequest
from typing import List

from ninja import Router
from ninja.responses import Response

from api.repositories.document_type_repository import DocumentTypeRepository
from api.schemas.document_view_schemas import DocumentsSchema

router = Router()

@router.get('/', response=List[DocumentsSchema])
def get(request: HttpRequest):
    document_types = DocumentTypeRepository().get_all()
    return Response([DocumentsSchema.from_orm(document) for document in document_types])
