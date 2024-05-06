import uuid

from typing import TYPE_CHECKING
from django.db import models

from api.models.base import BaseModel

if TYPE_CHECKING:
    from models.document_type_model import DocumentType


class RuralProducer(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    document_number = models.CharField(max_length=14)
    document_type = models.ForeignKey("DocumentType", on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=100)

    class Meta:
        db_table = "rural_producer"
