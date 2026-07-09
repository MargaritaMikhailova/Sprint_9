import allure

from selenium.webdriver.support import expected_conditions as EC

from locators import Parameter, Buttons, Pages, Links, ingredient_option
from pages.base_page import BasePage
from data import Data
from helpers import random_string, random_digits


class ReceiptPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.receipt_name = None

    @allure.step("Ожидание загрузки Рецепты")
    def wait_for_load_page(self):
        return self.find_long_element(Pages.MAIN_PAGE)

    @allure.step("Получение текущего URL")
    def get_current_url_login_page(self):
        return self.get_current_url_page()

    @allure.step("Перейти на табу создать рецепты")
    def click_tab_create_receipt(self):
        self.click(Buttons.CREATE_RECEIPT_TAB)

    @allure.step("Перейти на табу рецепты")
    def click_tab_all_receipt(self):
        self.click(Buttons.ALL_RECIPES_TAB)

    @allure.step("Получить последний элемент по локатору")
    def get_last_element(self, locator):
        elements = self.driver.find_elements(*locator)
        return elements[-1]

    @allure.step("Заполнить последнее поле: {text}")
    def fill_last_input(self, locator, text):
        element = self.get_last_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Добавить ингредиент: {ingredient}")
    def add_ingredient(self, ingredient: str, amount: str):
        self.fill_last_input(Parameter.INGRIDIENTS, ingredient)
        self.wait.until(
            EC.element_to_be_clickable(ingredient_option(ingredient))
        ).click()
        self.fill_last_input(Parameter.AMOUNT_ING, amount)
        self.get_last_element(Links.ADD_ING).click()

    @allure.step("Заполнить форму создание рецепта")
    def fill_form_receipt(self):
        self.receipt_name = random_string()
        amount = random_digits()
        self.input_text(Parameter.NAME_RECEIPT, self.receipt_name)
        for ingredient in Data.NAME_ING:
            self.add_ingredient(ingredient, amount)
        self.input_text(Parameter.TIME_COOK, amount)
        self.input_text(Parameter.DESCRIPTION, self.receipt_name)

    @allure.step("Загрузить фото")
    def fill_photo(self, filename: str = Data.PHOTO_FILE):
        file_path = Data.photo_path(filename)
        assert file_path.exists(), f"Файл {file_path} не найден"
        self.upload_file(Parameter.FILE_INPUT, Data.upload_photo_path(filename))

    @allure.step("Нажать на кнопку Создать рецепт")
    def click_create_receipt(self):
        button = self.long_wait.until(EC.element_to_be_clickable(Buttons.CREATE_RECEIPT))
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        button.click()

    @allure.step("Найти карточку рецепта")
    def find_receipt_card(self):
        return self.find_element(Pages.RECEIPT_CARD)

    @allure.step("Карточка индивидуальная рецепта")
    def find_receipt_card_individual(self):
        return self.find_element(Pages.CARD_INDIVIDUAL_RECEIPT)

    @allure.step("Получить название рецепта")
    def get_receipt_name(self):
        return self.find_element(Parameter.RECEIPT_ELEMENT)
