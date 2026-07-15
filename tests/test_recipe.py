import allure

from data import RecipeData
from pages.recipe_page import RecipePage


@allure.feature("Создание рецепта")
class TestCreateRecipe:

    @allure.title("Созданный рецепт отображается на странице с карточкой")
    def test_created_recipe_card_is_visible(self, logged_in_driver):
        recipe_page = RecipePage(logged_in_driver)
        recipe_page.open_create_recipe()
        recipe_page.enter_recipe_name(RecipeData.NAME)
        recipe_page.add_ingredient(
            RecipeData.INGREDIENT,
            RecipeData.INGREDIENT_AMOUNT)
        recipe_page.enter_cooking_time(RecipeData.COOKING_TIME)
        recipe_page.enter_description(RecipeData.DESCRIPTION)
        recipe_page.upload_photo()
        recipe_page.click_submit()
        assert recipe_page.is_recipe_card_visible(), \
            "Карточка созданного рецепта не отображается"

    @allure.title("Название созданного рецепта совпадает с введённым")
    def test_created_recipe_has_correct_name(self, logged_in_driver):
        recipe_page = RecipePage(logged_in_driver)
        recipe_page.open_create_recipe()
        recipe_page.enter_recipe_name(RecipeData.NAME)
        recipe_page.add_ingredient(
            RecipeData.INGREDIENT,
            RecipeData.INGREDIENT_AMOUNT)
        recipe_page.enter_cooking_time(RecipeData.COOKING_TIME)
        recipe_page.enter_description(RecipeData.DESCRIPTION)
        recipe_page.upload_photo()
        recipe_page.click_submit()
        title = recipe_page.get_recipe_title()
        assert RecipeData.NAME in title, \
            f"Название рецепта '{title}' не совпадает с ожидаемым '{RecipeData.NAME}'"
