import random
import string

from data import Data, Domain, UserFields

def random_string(length: int = Data.STRING_LENGTH) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=length))

def random_string_email(length: int = Data.STRING_LENGTH) -> str:
    local_part = random_string(length)
    return f"{local_part}@{Domain.DOMAIN}"

def random_digits(length: int = Data.DIGITS_LENGTH) -> str:
    return "".join(random.choices(string.digits, k=length))

def random_password(length: int = Data.DIGITS_LENGTH) -> str:
    return f"Pass{random_digits(length)}!"

def generate_user() -> dict:
    return {
        UserFields.NAME: random_string(),
        UserFields.SURNAME: random_string(),
        UserFields.NAME_USER: random_string(),
        UserFields.EMAIL: random_string_email(),
        UserFields.PASSWORD: random_password(),
    }
