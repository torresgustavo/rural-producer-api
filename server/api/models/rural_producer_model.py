import uuid

from typing import TYPE_CHECKING
from django.db import models

from api.models.base import BaseModel
from api.enums.document_types_enum import DocumentTypesEnum


class RuralProducer(BaseModel):
    class DocumentTypeChoices(models.TextChoices):
        CPF = (DocumentTypesEnum.CPF,)
        CNPJ = DocumentTypesEnum.CNPJ

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    document_number = models.CharField(max_length=14, unique=True)
    document_type = models.CharField(choices=DocumentTypeChoices)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=100)

    class Meta:
        db_table = "rural_producer"
