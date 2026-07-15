import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import URLS, APP_DIR
from pages.base_page import BasePage
from locators.recipe_page_locators import RecipePageLocators


class RecipePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Переходим на страницу создания рецепта")
    def open_create_recipe(self):
        self.click(RecipePageLocators.CREATE_RECIPE_LINK)
        self.wait_for_url_contains(URLS.CREATE_RECIPE_URL)

    @allure.step("Вводим название рецепта: {name}")
    def enter_recipe_name(self, name):
        self.enter_text(RecipePageLocators.RECIPE_NAME_INPUT, name)

    @allure.step(
        "Добавляем ингредиент: {ingredient_name}, количество: {amount}")
    def add_ingredient(self, ingredient_name, amount):
        self.enter_text(RecipePageLocators.INGREDIENT_INPUT, ingredient_name)
        WebDriverWait(
            self.driver, 10).until(
            EC.element_to_be_clickable(
                RecipePageLocators.INGREDIENT_DROPDOWN_ITEM)).click()
        self.enter_text(RecipePageLocators.INGREDIENT_AMOUNT_INPUT, amount)
        self.click(RecipePageLocators.ADD_INGREDIENT_BUTTON)

    @allure.step("Вводим время приготовления: {time} мин")
    def enter_cooking_time(self, time):
        self.enter_text(RecipePageLocators.COOKING_TIME_INPUT, time)

    @allure.step("Вводим описание рецепта")
    def enter_description(self, description):
        self.enter_text(RecipePageLocators.DESCRIPTION_TEXTAREA, description)

    @allure.step("Загружаем фото рецепта")
    def upload_photo(self, filename="test_image.png"):
        photo_path = str(APP_DIR / "assets" / filename)
        self.send_keys_to_element(RecipePageLocators.PHOTO_INPUT, photo_path)

    @allure.step("Нажимаем кнопку 'Создать рецепт'")
    def click_submit(self):
        self.click(RecipePageLocators.SUBMIT_BUTTON)

    @allure.step("Проверяем что карточка рецепта отображается")
    def is_recipe_card_visible(self):
        return self.is_element_visible(RecipePageLocators.RECIPE_CARD_TITLE)

    @allure.step("Получаем заголовок созданного рецепта")
    def get_recipe_title(self):
        element = self.wait_for_element_visible(
            RecipePageLocators.RECIPE_CARD_TITLE)
        return element.text
