import pytest
from api.utils.document_validators import cpf_validator, cnpj_validator

@pytest.mark.parametrize("cpf", [
    "123.456.789-09",
    "529.982.247-25",
    "862.883.667-57",
])
def test_cpf_is_valid(cpf: str):
    assert cpf_validator(cpf)

@pytest.mark.parametrize("cpf", [
    "123.456.789-10",
    "529.982.247-20",
    "000.000.000-00",
    "999.999.999-99",
    "12345678910",
    "1234567891",
    "123.456.789/10",
    "529.982.247-2A",
])
def test_cpf_is_invalid(cpf: str):
    assert cpf_validator(cpf) is False

@pytest.mark.parametrize("cnpj", [
    "21.149.712/0001-47",
    "12.549.764/0001-10",
    "39.202.811/0001-00",
])
def test_cnpj_is_valid(cnpj: str):
    assert cnpj_validator(cnpj)

@pytest.mark.parametrize("cnpj", [
    "12.345.678/0001-13",
    "86.747.865/0001-58",
    "11.111.111/1111-11",
    "22.222.222/2222-22",
    "12345678000113",
    "1234567800011",
    "12345678/0001-13",
    "86.74A.865/0001-58"
])
def test_cnpj_is_invalid(cnpj: str):
    assert cnpj_validator(cnpj) is False
