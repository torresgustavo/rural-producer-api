from http import HTTPStatus
from api.errors.base_error import BaseError


class InvalidDocumentType(BaseError):
    error_code = "INVALID_DOCUMENT_TYPE"
    status = HTTPStatus.BAD_REQUEST
    details = None

    def __init__(self, document_type_name: str):
        self.message = f"Document type is invalid: {document_type_name}"
