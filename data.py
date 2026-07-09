import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"


class Urls:
    MAIN_PAGE = "https://foodgram-frontend-1.foodgram.education-services.ru"
    BASE_PAGE = f"{MAIN_PAGE}"
    LOGIN_PAGE = f"{MAIN_PAGE}/signin"
    AUTH_PAGE = f"{MAIN_PAGE}/signup"
    PAGE_RECIPES = f"{MAIN_PAGE}/recipes"
    CREATE_RECEIPT = f"{PAGE_RECIPES}/create"

class Domain:
    DOMAIN = "ya.ru"


class UserFields:
    NAME = "name"
    SURNAME = "surname"
    NAME_USER = "name_user"
    EMAIL = "email"
    PASSWORD = "password"


class Data:
    NAME_ING = ["икра", "хлеб"]
    PHOTO_FILE = "buterbrod.jpg"
    STRING_LENGTH = 10
    DIGITS_LENGTH = 3

    @staticmethod
    def photo_path(filename: str | None = None) -> Path:
        return ASSETS_DIR / (filename or Data.PHOTO_FILE)

    @staticmethod
    def upload_photo_path(filename: str | None = None) -> str:
        name = filename or Data.PHOTO_FILE
        if os.getenv("SELENOID_URL"):
            return f"/app/assets/{name}"
        return str(Data.photo_path(name))
