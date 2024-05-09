from decimal import Decimal
from typing import Dict, TypedDict
from ninja import Schema


class PerAnythingSchema(Schema):
    farms_count: int
    total_area: Decimal
    total_arable_area: Decimal
    total_vegetation_area: Decimal


class DashboardDataSchema(Schema):
    total_area: Decimal
    total_arable_area: Decimal
    total_vegetation_area: Decimal
    farms_count: int

    per_state: Dict[str, PerAnythingSchema]
    per_culture: Dict[str, PerAnythingSchema]
