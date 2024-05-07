from uuid import UUID
from ninja.schema import Schema

from server.api.schemas.document_schemas import DocumentsSchema


class RuralProducersSchema(Schema):
    id: UUID
    name: str
    document_number: str
    city: str
    state: str
    document_type: DocumentsSchema
