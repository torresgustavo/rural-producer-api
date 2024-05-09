from http import HTTPStatus
from api.errors.base_error import BaseError


class FarmRuralProducerNotFound(BaseError):
    error_code = "FARM_RURAL_PRODUER_NOT_FOUND"
    status = HTTPStatus.NOT_FOUND
    details = None

    def __init__(self, query: str):
        self.message = f"Rural producer farm not found: {query}"
