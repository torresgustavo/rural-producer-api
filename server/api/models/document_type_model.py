from django.db import models
from api.models.base import BaseModel

class DocumentType(BaseModel):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=10, null=False)

    class Meta:
        db_table = "document_type"