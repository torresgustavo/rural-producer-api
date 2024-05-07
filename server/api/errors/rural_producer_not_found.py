from http import HTTPStatus
from api.errors.base_error import BaseError

class RuralProducerNotFoundError(BaseError):
    error_code = 'RURAL_PRODUCER_NOT_FOUND'
    status = HTTPStatus.NOT_FOUND
    details = None
    
    def __init__(self, query: str):
        self.message = f'Rural producer not found: {query}'
