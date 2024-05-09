import re

from api.enums.document_types_enum import DocumentTypesEnum
from api.errors.invalid_document_type import InvalidDocumentType


class DocumentsValidator():

    def __init__(self, document_number: str, document_type: DocumentTypesEnum):
        self.__document_number = document_number
        self.__document_type = document_type

    def execute(self):
        if self.__document_type == DocumentTypesEnum.CPF:
            return self.__cpf_validator()
        elif self.__document_type == DocumentTypesEnum.CNPJ:
            return self.__cnpj_validator()
        else:
            raise InvalidDocumentType(self.__document_type)

    def __cpf_validator(self) -> bool:
        self.__document_number = re.sub(r'[^0-9]', '', self.__document_number)
        
        if len(self.__document_number) != 11:
            return False
        
        if self.__document_number == self.__document_number[0] * 11:
            return False
        
        digit_sum = 0
        for i in range(9):
            digit_sum += int(self.__document_number[i]) * (10 - i)
        first_digit = 11 - (digit_sum % 11)
        if first_digit > 9:
            first_digit = 0
        
        digit_sum = 0
        for i in range(10):
            digit_sum += int(self.__document_number[i]) * (11 - i)
        second_digit = 11 - (digit_sum % 11)
        if second_digit > 9:
            second_digit = 0
        
        if int(self.__document_number[9]) == first_digit and int(self.__document_number[10]) == second_digit:
            return True
        else:
            return False

    def __cnpj_validator(self) -> bool:
        self.__document_number = re.sub(r'[^0-9]', '', self.__document_number)
        
        if len(self.__document_number) != 14:
            return False
        
        if self.__document_number == self.__document_number[0] * 14:
            return False
        
        total = 0
        multiplier = 5
        for i in range(12):
            total += int(self.__document_number[i]) * multiplier
            multiplier -= 1
            if multiplier == 1:
                multiplier = 9
        digit1 = 11 - (total % 11)
        if digit1 > 9:
            digit1 = 0
        
        total = 0
        multiplier = 6
        for i in range(13):
            total += int(self.__document_number[i]) * multiplier
            multiplier -= 1
            if multiplier == 1:
                multiplier = 9
        digit2 = 11 - (total % 11)
        if digit2 > 9:
            digit2 = 0
        
        return int(self.__document_number[12]) == digit1 and int(self.__document_number[13]) == digit2
