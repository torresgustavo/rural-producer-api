from decimal import Decimal
from typing import List, Optional
from ninja import ModelSchema, Schema

from api.models.rural_producer_model import RuralProducer
from api.models.farm_rural_producer_model import FarmRuralProducer
from api.models.farm_culture_rural_producer_model import FarmCultureRuralProducer

from api.models.farm_culture_type_model import FarmCultureType

from api.enums.document_types_enum import DocumentTypesEnum

class ViewCultureTypeSchema(ModelSchema):
    class Meta:
        model=FarmCultureType
        exclude=['created_at', 'updated_at']

class ViewFarmCultureSchema(ModelSchema):
    farm_culture_type: ViewCultureTypeSchema

    class Meta:
        model=FarmCultureRuralProducer
        exclude=['created_at', 'updated_at', 'farm']

class ViewFarmSchema(ModelSchema):
    cultures: List[ViewFarmCultureSchema]

    class Meta:
        model=FarmRuralProducer
        exclude=['created_at', 'updated_at', 'rural_producer']

class ViewRuralProducersSchema(ModelSchema):
    farm: Optional[ViewFarmSchema]
    
    class Meta:
        model=RuralProducer
        exclude=['created_at', 'updated_at']

    @staticmethod
    def resolve_farm(obj):
        if hasattr(obj, 'farm'):
            return obj.farm
        else:
            return None
        
class FarmCulture(Schema):
    farm_culture_type_id: int

class NewFarmSchema(Schema):
    name: str
    total_hectare_area: Decimal
    arable_hectare_area: Decimal
    vegetation_hectare_area: Decimal

    cultures: List[FarmCulture]
        
class NewRuralProducerSchema(Schema):
    name: str
    document_type: DocumentTypesEnum
    document_number: str
    city: str
    state: str

    farm: NewFarmSchema

class EditFarmSchema(Schema):
    name: Optional[str] = None
    total_hectare_area: Optional[Decimal] = None
    arable_hectare_area: Optional[Decimal] = None
    vegetation_hectare_area: Optional[Decimal] = None

class EditRuralProducerSchema(Schema):
    name: Optional[str] = None
    document_type: Optional[DocumentTypesEnum] = None
    document_number: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None

    farm: Optional[EditFarmSchema] = None
