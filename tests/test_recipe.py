import allure

from locators.recipe_page_locators import RecipePageLocators
from pages.recipe_page import RecipePage

RECIPE_NAME = "Тестовый рецепт картофельный"

@allure.feature("Создание рецепта")
class TestCreateRecipe:
 
    @allure.title("Созданный рецепт отображается на странице с карточкой")
    def test_created_recipe_card_is_visible(self, logged_in_driver):
        recipe_page = RecipePage(logged_in_driver)
        recipe_page.open_create_recipe()
        recipe_page.enter_recipe_name(RECIPE_NAME)
        recipe_page.add_ingredient("картофель", "200")
        recipe_page.enter_cooking_time("30")
        recipe_page.enter_description("Тестовое описание рецепта")
        recipe_page.upload_photo()
        recipe_page.click_submit()
        assert recipe_page.is_element_visible(RecipePageLocators.RECIPE_CARD_TITLE), \
            "Карточка созданного рецепта не отображается"
	
    @allure.title("Название созданного рецепта совпадает с введённым")
    def test_created_recipe_has_correct_name(self, logged_in_driver):
        recipe_page = RecipePage(logged_in_driver)
        recipe_page.open_create_recipe()
        recipe_page.enter_recipe_name(RECIPE_NAME)
        recipe_page.add_ingredient("картофель", "200")
        recipe_page.enter_cooking_time("30")
        recipe_page.enter_description("Тестовое описание рецепта")
        recipe_page.upload_photo()
        recipe_page.click_submit()
        title = recipe_page.get_recipe_title()
        assert RECIPE_NAME in title, \
            f"Название рецепта '{title}' не совпадает с ожидаемым '{RECIPE_NAME}'"