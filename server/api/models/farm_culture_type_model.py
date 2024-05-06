from django.db import models
from api.models.base import BaseModel


class FarmCultureType(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "farm_culture_type"