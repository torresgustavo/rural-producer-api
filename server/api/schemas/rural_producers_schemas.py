from decimal import Decimal
from typing import List, Optional
from ninja import ModelSchema, Schema

from api.models.rural_producer_model import RuralProducer
from api.models.farm_rural_producer_model import FarmRuralProducer
from api.models.farm_culture_rural_producer_model import FarmCultureRuralProducer
from api.models.farm_culture_type_model import FarmCultureType
from api.enums.document_types_enum import DocumentTypesEnum

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
        
class NewFarmCulture(Schema):
    farm_culture_type_id: int

class NewFarmSchema(Schema):
    name: str
    total_hectare_area: Decimal
    arable_hectare_area: Decimal
    vegetation_hectare_area: Decimal

    cultures: List[NewFarmCulture]
        
class NewRuralProducerSchema(Schema):
    name: str
    document_type: DocumentTypesEnum
    document_number: str
    city: str
    state: str

    farm: NewFarmSchema
