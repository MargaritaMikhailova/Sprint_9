import allure

from data import Urls

class TestAuthPage:

    @allure.title('Проверить Авторизацию')
    @allure.description('Проверить: Нажать кнопку войти и произошел переход на главную страницу')
    def test_login_redirects_to_recipes(self, authorized_user, auth_page):
        
        auth_page.fill_auth_form(authorized_user)
        auth_page.click_login_account_button_form()
        auth_page.wait_for_url_contains(Urls.PAGE_RECIPES)

        assert auth_page.get_current_url_login_page() == Urls.PAGE_RECIPES

    @allure.title('Проверить Авторизацию')
    @allure.description('Проверить: Нажать кнопку войти и проверить что отображается кнопка Выход')
    def test_check_button_logout(self, authorized_user, auth_page):
        
        auth_page.fill_auth_form(authorized_user)
        auth_page.click_login_account_button_form()
        auth_page.check_main_page()

        button_logout = auth_page.check_button_logout()
        assert button_logout.is_displayed()