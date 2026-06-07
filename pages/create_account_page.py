import allure

from locators import Parameter, Buttons, Pages
from pages.base_page import BasePage
from data import UserFields

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ожидание загрузки Войти на сайт")
    def wait_for_load_page(self):
        return self.find_long_element(Pages.LOGIN_PAGE)

    @allure.step("Получение текущего URL")
    def get_current_url_login_page(self):
        return self.get_current_url_page()
    
    @allure.step("Нажатие на кнопку Созадть аккаунт")
    def click_create_account_button(self):
        self.click(Buttons.CREATE_BUTTON)

    @allure.step("Заполнение формы регистрации")
    def fill_auth_form(self, user):
        self.input_text(Parameter.FIRST_NAME, user[UserFields.NAME])
        self.input_text(Parameter.LAST_NAME, user[UserFields.SURNAME])
        self.input_text(Parameter.USER_NAME, user[UserFields.NAME_USER])
        self.input_text(Parameter.ADDRESS_EMAIL, user[UserFields.EMAIL])
        self.input_text(Parameter.PASS_REGISSTR, user[UserFields.PASSWORD])

    @allure.step("Нажатие на кнопку Создать аккакунт на форме")
    def click_create_acc_but_form(self):
        self.click(Buttons.CREATE_BUTTON_FORM)

    @allure.step("Ожидание загрузки Регистрация")
    def wait_load_page_auth_page(self):
        return self.find_long_element(Pages.AUTH_PAGE)



