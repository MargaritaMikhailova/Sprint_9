import allure

from locators import Parameter, Buttons, Pages
from pages.base_page import BasePage
from data import UserFields


class AuthPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ожидание загрузки Войти на сайт")
    def wait_for_load_page(self):
        return self.find_long_element(Pages.LOGIN_PAGE)

    @allure.step("Получение текущего URL")
    def get_current_url_login_page(self):
        return self.get_current_url_page()
    
    @allure.step("Нажатие на кнопку Войти")
    def click_login_account_button(self):
        self.click(Buttons.LOGIN_BUTTON)

    @allure.step("Нажатие на кнопку Войти на форме")
    def click_login_account_button_form(self):
        self.click(Buttons.LOGIN_BUTTON_FORM)
    
    @allure.step("Заполнение формы авторизации")
    def fill_auth_form(self, user):
        self.input_text(Parameter.EMAIL, user[UserFields.NAME_USER])
        self.input_text(Parameter.PASSWORD, user[UserFields.PASSWORD])

    @allure.step("Ожидание загрузки главной страницы с рецептами")
    def check_main_page(self):
       return self.find_element(Pages.MAIN_PAGE)
    
    @allure.step("Найти кнопку выход")
    def check_button_logout(self):
       return self.find_element(Buttons.EXIT_BUTTON)
