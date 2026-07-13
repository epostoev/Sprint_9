import allure

from data import URLS
from pages.base_page import BasePage
from locators.signup_page_locators import SignupPageLocators


class SignupPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открываем главную страницу")
    def open_main(self):
        self.go_to_url(URLS.SIGNIN_URL)

    @allure.step("Кликаем на кнопку 'Создать аккаунт' в хедере")
    def click_create_account_link(self):
        self.click(SignupPageLocators.LINK_CREATE_ACCOUNT)

    @allure.step("Заполняем форму регистрации")
    def fill_signup_form(
            self,
            first_name,
            last_name,
            username,
            email,
            password):
        self.enter_text(SignupPageLocators.INPUT_FIRST_NAME, first_name)
        self.enter_text(SignupPageLocators.INPUT_LAST_NAME, last_name)
        self.enter_text(SignupPageLocators.INPUT_USERNAME, username)
        self.enter_text(SignupPageLocators.INPUT_EMAIL, email)
        self.enter_text(SignupPageLocators.INPUT_PASSWORD, password)

    @allure.step("Нажимаем кнопку 'Создать аккаунт'")
    def click_submit(self):
        self.click(SignupPageLocators.BUTTON_SUBMIT)
