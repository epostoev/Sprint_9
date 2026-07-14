import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from helpers import generate_user_data
from data import URLS
from pages.signup_page import SignupPage
from pages.signin_page import SigninPage


def get_driver():
    """Возвращает локальный Chrome или Remote (Selenoid) в зависимости от окружения."""
    selenoid_url = os.getenv("SELENOID_URL")
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    if selenoid_url:
        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion", "128.0")
        options.set_capability("selenoid:options", {
            "enableVNC": True,
            "enableVideo": False
        })
        return webdriver.Remote(
            command_executor=selenoid_url,
            options=options
        )
    else:
        return webdriver.Chrome(options=options)


@pytest.fixture
def driver():
    browser = get_driver()
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


@pytest.fixture
def logged_in_driver(driver, registered_user):
    """Драйвер с уже залогиненным пользователем."""
    signin_page = SigninPage(driver)
    signin_page.login(
        email=registered_user["username"],
        password=registered_user["password"],
    )
    return driver