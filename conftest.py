import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.file_detector import LocalFileDetector

from data import Urls
from helpers import generate_user
from pages.auth_page import AuthPage
from pages.create_account_page import LoginPage
from pages.create_receipt import ReceiptPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")

    selenoid_url = os.getenv("SELENOID_URL")
    if selenoid_url:
        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion", "128.0")
        options.set_capability("selenoid:options", {"enableVideo": False})
        browser = webdriver.Remote(command_executor=selenoid_url, options=options)
        browser.file_detector = LocalFileDetector()
    else:
        browser = webdriver.Chrome(options=options)

    browser.get(Urls.MAIN_PAGE)
    yield browser
    browser.quit()


@pytest.fixture
def user():
    return generate_user()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def authorized_user(login_page, user):
    login_page.wait_load_page_auth_page()
    login_page.click_create_account_button()
    login_page.fill_auth_form(user)
    login_page.click_create_acc_but_form()
    login_page.wait_for_url_contains(Urls.LOGIN_PAGE)
    return user


@pytest.fixture
def auth_page(driver):
    return AuthPage(driver)


@pytest.fixture
def receipt_page(driver):
    return ReceiptPage(driver)
