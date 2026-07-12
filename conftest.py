import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from helpers import generate_user_data


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
 