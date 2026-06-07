import allure

from data import Urls

class TestCreateAccountPage:

    @allure.title('Проверить Создание аккаунта')
    @allure.description('Проверить: заполнить все поля формы регистрации и нажать на кнопку Создать аккаунт')
    def test_registration_redirects_to_signin(self, login_page, user):
        
        login_page.wait_load_page_auth_page()
        login_page.click_create_account_button()
        login_page.fill_auth_form(user)
        login_page.click_create_acc_but_form()
        login_page.wait_for_url_contains(Urls.LOGIN_PAGE)

        assert login_page.get_current_url_login_page() == Urls.LOGIN_PAGE

    @allure.title('Проверить Создание аккаунта')
    @allure.description('Проверить: нажать на кнопку Создать аккаунт и произошел переход на страницу авторизации')
    def test_check_url_auth(self, login_page):
        
        login_page.wait_load_page_auth_page()
        login_page.click_create_account_button()
        login_page.wait_for_load_page()

        assert login_page.get_current_url_login_page() == Urls.AUTH_PAGE


    @allure.title('Проверить Создание аккаунта')
    @allure.description('Проверить: нажать на кнопку Создать аккаунт и отображается ли форма авторизации')
    def test_check_form_auth(self, login_page):
        
        login_page.wait_load_page_auth_page()
        login_page.click_create_account_button()
        
        form_auth = login_page.wait_load_page_auth_page()

        assert form_auth.is_displayed()

    