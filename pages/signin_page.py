import allure

from data import URLS
from pages.base_page import BasePage
from locators.signin_page_locators import SigninPageLocators


class SigninPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открываем страницу авторизации")
    def open(self):
        self.go_to_url(URLS.SIGNIN_URL)

    @allure.step("Проверяем что форма авторизации отображается")
    def is_signin_form_visible(self):
        return self.is_element_visible(SigninPageLocators.FORM_SIGNIN)

    @allure.step("Заполняем форму авторизации")
    def fill_signin_form(self, email, password):
        self.enter_text(SigninPageLocators.INPUT_EMAIL, email)
        self.enter_text(SigninPageLocators.INPUT_PASSWORD, password)

    @allure.step("Нажимаем кнопку 'Войти'")
    def click_submit(self):
        self.click(SigninPageLocators.BUTTON_SUBMIT)

    @allure.step("Кликаем на 'Войти' в хедере")
    def click_signin_link(self):
        self.click(SigninPageLocators.LINK_SIGNIN)
