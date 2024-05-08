from typing import List, Optional
from ninja import ModelSchema

from api.schemas.document_schemas import DocumentsSchema

from api.models.rural_producer_model import RuralProducer
from api.models.farm_rural_producer_model import FarmRuralProducer
from api.models.farm_culture_rural_producer_model import FarmCultureRuralProducer
from api.models.farm_culture_type_model import FarmCultureType

class CultureTypeSchema(ModelSchema):
    class Meta:
        model=FarmCultureType
        exclude=['created_at', 'updated_at']

class FarmCultureSchema(ModelSchema):
    farm_culture_type: CultureTypeSchema

    class Meta:
        model=FarmCultureRuralProducer
        exclude=['created_at', 'updated_at', 'farm']

class FarmSchema(ModelSchema):
    cultures: List[FarmCultureSchema]

    class Meta:
        model=FarmRuralProducer
        exclude=['created_at', 'updated_at', 'rural_producer']

class RuralProducersSchema(ModelSchema):
    document_type: DocumentsSchema
    farm: Optional[FarmSchema]
    
    class Meta:
        model=RuralProducer
        exclude=['created_at', 'updated_at']

    @staticmethod
    def resolve_farm(obj):
        if hasattr(obj, 'farm'):
            return obj.farm
        else:
            return None
