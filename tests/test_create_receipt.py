import allure

from data import Urls

class TestReceiptPage:

    @allure.title('Проверить Создание рецепта')
    @allure.description('Проверить: Авторизоваться и перейти на табу Создать рецепт')
    def test_check_tab_create_receipt(self, receipt_page, authorized_user, auth_page):
        
        auth_page.fill_auth_form(authorized_user)
        auth_page.click_login_account_button_form()
        receipt_page.wait_for_url_contains(Urls.PAGE_RECIPES)
        receipt_page.click_tab_create_receipt()

        assert receipt_page.get_current_url_login_page() == Urls.CREATE_RECEIPT

    @allure.title('Проверить Создание рецепта')
    @allure.description('Проверить: Заполнить все полня формы Создания рецепта и нажать кнопку Создать рецепт')
    def test_check_receipt_create(self, receipt_page, authorized_user, auth_page):
        
        auth_page.fill_auth_form(authorized_user)
        auth_page.click_login_account_button_form()
        receipt_page.wait_for_url_contains(Urls.PAGE_RECIPES)
        receipt_page.click_tab_create_receipt()
        receipt_page.fill_form_receipt()
        receipt_page.fill_photo()
        receipt_page.click_create_receipt()
        individual_card = receipt_page.find_receipt_card_individual()

        assert individual_card.is_displayed()


    @allure.title('Проверить Создание рецепта')
    @allure.description('Проверить: Заполнить все полня формы Создания рецепта и нажать кнопку Создать рецепт')
    def test_find_receipt_on_all_receipt(self, receipt_page, authorized_user, auth_page):
        
        auth_page.fill_auth_form(authorized_user)
        auth_page.click_login_account_button_form()
        receipt_page.wait_for_url_contains(Urls.PAGE_RECIPES)
        receipt_page.click_tab_create_receipt()
        receipt_page.fill_form_receipt()
        receipt_page.fill_photo()
        receipt_page.click_create_receipt()
        receipt_page.click_tab_all_receipt()

        find_name_receipt = receipt_page.get_receipt_name()
        assert find_name_receipt.is_displayed()

        