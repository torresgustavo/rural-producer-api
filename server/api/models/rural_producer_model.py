import uuid

from typing import TYPE_CHECKING
from django.db import models

from api.models.base import BaseModel

if TYPE_CHECKING:
    from document_type_model import DocumentType
    from farm_rural_producer_model import FarmRuralProducer


class RuralProducer(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    document_number = models.CharField(max_length=14)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=100)

    document_type = models.OneToOneField("DocumentType", on_delete=models.CASCADE)

    class Meta:
        db_table = "rural_producer"
