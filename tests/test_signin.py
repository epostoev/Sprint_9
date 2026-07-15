import allure

from data import URLS
from pages.signin_page import SigninPage
from pages.main_page import MainPage


@allure.feature("Авторизация")
class TestSignin:

    @allure.title("Успешная авторизация переводит на главную страницу")
    def test_signin_redirects_to_recipes(self, driver, registered_user):
        signin_page = SigninPage(driver)
        signin_page.click_signin_link()
        signin_page.wait_for_url_contains(URLS.SIGNIN_URL)
        signin_page.fill_signin_form(
            email=registered_user["username"],
            password=registered_user["password"],
        )
        signin_page.click_submit()
        signin_page.wait_for_url_contains(URLS.RECIPES_URL)
        assert URLS.RECIPES_URL in signin_page.get_current_url(), \
            "После авторизации не произошёл переход на главную страницу"

    @allure.title("После авторизации отображается кнопка 'Выход'")
    def test_signin_shows_logout_button(self, driver, registered_user):
        signin_page = SigninPage(driver)
        signin_page.click_signin_link()
        signin_page.wait_for_url_contains(URLS.SIGNIN_URL)
        signin_page.fill_signin_form(
            email=registered_user["username"],
            password=registered_user["password"],
        )
        signin_page.click_submit()
        signin_page.wait_for_url_contains(URLS.RECIPES_URL)

        main_page = MainPage(driver)
        assert main_page.is_logout_visible(), \
            "Кнопка 'Выход' не отображается после авторизации"
