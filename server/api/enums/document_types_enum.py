import enum
from typing import Callable
from api.utils.document_validators import cnpj_validator, cpf_validator

class DocumentTypesEnum(enum.StrEnum):
    CPF='CPF',
    CNPJ='CNPJ'

    @classmethod
    def get_validator(cls, document_type: 'DocumentTypesEnum') -> Callable[[str], bool]:
        document_validator_dictionary = {
            cls.CPF: cpf_validator,
            cls.CNPJ: cnpj_validator
        }

        return document_validator_dictionary[document_type.value]