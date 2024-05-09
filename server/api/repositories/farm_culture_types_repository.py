from django.db.models.manager import BaseManager
from api.models.farm_culture_type_model import FarmCultureType


class FarmCultureTypesRepository:

    def get_all(self) -> BaseManager[FarmCultureType]:
        result = FarmCultureType.objects.all().values()
        return result
