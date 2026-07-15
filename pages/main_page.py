import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Проверяем что кнопка 'Выход' отображается")
    def is_logout_visible(self):
        return self.is_element_visible(MainPageLocators.LOGOUT_LINK)
