import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from helpers import generate_user_data
from data import URLS
from pages.signup_page import SignupPage


@pytest.fixture
def driver():
    options = Options()
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def new_user():
    """Генерирует уникальные данные пользователя для каждого теста."""
    return generate_user_data()


@pytest.fixture
def registered_user(driver):
    """Регистрирует пользователя через UI и возвращает его данные."""
    user = generate_user_data()
    signup_page = SignupPage(driver)
    signup_page.open_main()
    signup_page.click_create_account_link()
    signup_page.wait_for_url_contains(URLS.SIGNUP_URL)
    signup_page.fill_signup_form(
        first_name=user["first_name"],
        last_name=user["last_name"],
        username=user["username"],
        email=user["email"],
        password=user["password"],
    )
    signup_page.click_submit()
    signup_page.wait_for_url_contains(URLS.SIGNIN_URL)
    return user
