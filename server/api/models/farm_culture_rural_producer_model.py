import uuid

from typing import TYPE_CHECKING
from django.db import models

from api.models.base import BaseModel

if TYPE_CHECKING:
    from farm_rural_producer_model import FarmRuralProducer
    from farm_culture_type_model import FarmCultureType


class FarmCultureRuralProducer(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    farm_id = models.ForeignKey("FarmRuralProducer", on_delete=models.CASCADE)
    farm_culture_type = models.ForeignKey("FarmCultureType", on_delete=models.CASCADE)
    used_hectare_area = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('farm_id', 'farm_culture_type')
        db_table = "farm_culture_rural_producer"
