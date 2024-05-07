from dataclasses import dataclass
from typing import Optional
from http import HTTPStatus


@dataclass
class BaseError(Exception):
    def __init__(
        self,
        message: str,
        error_code: str = "UNEXPECTED_ERROR",
        status: HTTPStatus = HTTPStatus.INTERNAL_SERVER_ERROR,
        details: Optional[dict] = None,
    ):
        self.message = message
        self.status = status
        self.error_code = error_code
        self.details = details

        super().__init__(message)

    def to_dict(self) -> dict:
        data = {
            "status_code": self.status.value,
            "error_code": self.error_code,
            "message": self.message,
            "details": self.details,
        }

        return data
