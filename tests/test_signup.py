import allure

from data import URLS
from pages.signup_page import SignupPage
from pages.signin_page import SigninPage


@allure.feature("Создание аккаунта")
class TestSignup:

    @allure.title("Успешное создание аккаунта переводит на страницу авторизации")
    def test_signup_redirects_to_signin(self, driver, new_user):
        signup_page = SignupPage(driver)
        signup_page.open_main()
        signup_page.click_create_account_link()
        signup_page.wait_for_url_contains(URLS.SIGNUP_URL)
        signup_page.fill_signup_form(
            first_name=new_user["first_name"],
            last_name=new_user["last_name"],
            username=new_user["username"],
            email=new_user["email"],
            password=new_user["password"],
        )
        signup_page.click_submit()
        signup_page.wait_for_url_contains(URLS.SIGNIN_URL)
        assert URLS.SIGNIN_URL in signup_page.get_current_url(), \
            "После регистрации не произошёл переход на страницу авторизации"

    @allure.title("После регистрации отображается форма авторизации")
    def test_signup_shows_signin_form(self, driver, new_user):
        signup_page = SignupPage(driver)
        signup_page.open_main()
        signup_page.click_create_account_link()
        signup_page.wait_for_url_contains(URLS.SIGNUP_URL)
        signup_page.fill_signup_form(
            first_name=new_user["first_name"],
            last_name=new_user["last_name"],
            username=new_user["username"],
            email=new_user["email"],
            password=new_user["password"],
        )
        signup_page.click_submit()
        signup_page.wait_for_url_contains(URLS.SIGNIN_URL)

        signin_page = SigninPage(driver)
        assert signin_page.is_signin_form_visible(), \
            "Форма авторизации не отображается после регистрации"
