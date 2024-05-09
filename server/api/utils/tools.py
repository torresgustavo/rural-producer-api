import re


def clean_numerical_string(text: str):
    return re.sub(r"\D", "", text)
