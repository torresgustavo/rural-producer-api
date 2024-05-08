import re

def cpf_validator(cpf: str) -> bool:
    cpf = re.sub(r'[^0-9]', '', cpf)
    
    if len(cpf) != 11:
        return False
    
    if cpf == cpf[0] * 11:
        return False
    
    digit_sum = 0
    for i in range(9):
        digit_sum += int(cpf[i]) * (10 - i)
    first_digit = 11 - (digit_sum % 11)
    if first_digit > 9:
        first_digit = 0
    
    digit_sum = 0
    for i in range(10):
        digit_sum += int(cpf[i]) * (11 - i)
    second_digit = 11 - (digit_sum % 11)
    if second_digit > 9:
        second_digit = 0
    
    if int(cpf[9]) == first_digit and int(cpf[10]) == second_digit:
        return True
    else:
        return False

def cnpj_validator(cnpj: str) -> bool:
    cnpj = re.sub(r'[^0-9]', '', cnpj)
    
    if len(cnpj) != 14:
        return False
    
    if cnpj == cnpj[0] * 14:
        return False
    
    total = 0
    multiplier = 5
    for i in range(12):
        total += int(cnpj[i]) * multiplier
        multiplier -= 1
        if multiplier == 1:
            multiplier = 9
    digit1 = 11 - (total % 11)
    if digit1 > 9:
        digit1 = 0
    
    total = 0
    multiplier = 6
    for i in range(13):
        total += int(cnpj[i]) * multiplier
        multiplier -= 1
        if multiplier == 1:
            multiplier = 9
    digit2 = 11 - (total % 11)
    if digit2 > 9:
        digit2 = 0
    
    return int(cnpj[12]) == digit1 and int(cnpj[13]) == digit2
