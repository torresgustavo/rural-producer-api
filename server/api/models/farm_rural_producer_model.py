import uuid

from typing import TYPE_CHECKING, List
from django.db import models

from api.models.base import BaseModel

if TYPE_CHECKING:
    from rural_producer_model import RuralProducer
    from farm_culture_rural_producer_model import FarmCultureRuralProducer


class FarmRuralProducer(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    total_hectare_area = models.DecimalField(max_digits=5, decimal_places=2)
    arable_hectare_area = models.DecimalField(max_digits=5, decimal_places=2)
    vegetation_hectare_area = models.DecimalField(max_digits=5, decimal_places=2)

    rural_producer = models.OneToOneField("RuralProducer", related_name='farm', on_delete=models.CASCADE)

    class Meta:
        db_table = "farm_rural_producer"
