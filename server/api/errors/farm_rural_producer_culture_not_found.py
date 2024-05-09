from http import HTTPStatus
from uuid import UUID
from api.errors.base_error import BaseError


class FarmRuralProducerCultureNotFound(BaseError):
    error_code = "FARM_RURAL_PRODUCER_CULTURE_NOT_FOUND"
    status = HTTPStatus.NOT_FOUND
    details = None

    def __init__(self, farm_id: UUID, culture_id: int):
        self.message = f"Rural producer farm culture not found: Farm {farm_id} and culture id {culture_id}"
