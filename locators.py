from selenium.webdriver.common.by import By


class Buttons:
    CREATE_BUTTON = (By.XPATH, "//a[@href='/signup']")
    LOGIN_BUTTON = (By.XPATH, "//a[@href='/signin']")
    LOGIN_BUTTON_FORM = (By.XPATH, "//button[text()='Войти']")
    CREATE_BUTTON_FORM = (By.XPATH, "//button[text()='Создать аккаунт']")
    EXIT_BUTTON = (By.XPATH, "//a[text()='Выход']")
    CREATE_RECEIPT_TAB = (By.XPATH, "//a[text()='Создать рецепт']")
    ALL_RECIPES_TAB = (By.XPATH, "//a[@href='/recipes']")
    CHOOSE_FILE = (By.XPATH, "//button[text()='Выбрать файл']")
    CREATE_RECEIPT = (By.XPATH, "//button[text()='Создать рецепт']")


class Parameter:
    EMAIL = (By.XPATH, "//input[@name='email']")
    PASSWORD = (By.XPATH, "//input[@name='password']")
    FIRST_NAME = (By.XPATH, "//input[@name='first_name']")
    LAST_NAME = (By.XPATH, "//input[@name='last_name']")
    USER_NAME = (By.XPATH, "//input[@name='username']")
    ADDRESS_EMAIL = (By.XPATH, "//input[@name='email' and contains(@class, 'styles_inputField__3eqTj')]")
    PASS_REGISSTR = (By.XPATH, "//input[@name='password' and contains(@class, 'styles_inputField__3eqTj')]")
    NAME_RECEIPT = (By.XPATH, "(//input[contains(@class, 'styles_inputField__3eqTj')])[1]")
    INGRIDIENTS = (By.XPATH, "//input[contains(@class, 'styles_ingredientsInput')]")
    AMOUNT_ING = (By.XPATH, "//input[contains(@class, 'styles_ingredientsAmountValue')]")
    TIME_COOK = (By.XPATH, "(//input[contains(@class, 'styles_inputField__3eqTj') ""and not(contains(@class, 'ingredients'))])[2]")
    INGREDIENT_OPTION = (By.XPATH, "//div[contains(@class, 'styles_container__3ukwm')]//div[normalize-space(text())='{name}']")
    DESCRIPTION = (By.CLASS_NAME, "styles_textareaField__1wfhC")
    RECEIPT_ELEMENT = (By.CLASS_NAME, "style_link__1kPh8")
    FILE_INPUT = (By.XPATH, "//input[@type='file']")


class Pages:
    LOGIN_PAGE = (By.CLASS_NAME, "style_container__mLpjI")
    AUTH_PAGE = (By.CLASS_NAME, "styles_form__2nwxz")
    MAIN_PAGE = (By.CLASS_NAME, "style_cardList__2pI7x")
    RECEIPT_CARD = (By.CLASS_NAME, "style_card__1Le2w")
    CARD_INDIVIDUAL_RECEIPT = (By.CLASS_NAME, "style_main__Zjyqx")


class Links:
    ADD_ING = (By.CLASS_NAME, "styles_ingredientAdd__3fc32")


def ingredient_option(name: str):
    return (
        By.XPATH,
        Parameter.INGREDIENT_OPTION[1].format(name=name),
    )
