import uuid

from typing import TYPE_CHECKING
from django.db import models

from api.models.base import BaseModel

if TYPE_CHECKING:
    from farm_rural_producer_model import FarmRuralProducer
    from farm_culture_type_model import FarmCultureType


class FarmCultureRuralProducer(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    farm_culture_type = models.ForeignKey("FarmCultureType", on_delete=models.PROTECT)

    farm = models.ForeignKey("FarmRuralProducer", related_name='cultures', on_delete=models.CASCADE)

    class Meta:
        unique_together = ("farm_id", "farm_culture_type")
        db_table = "farm_culture_rural_producer"
