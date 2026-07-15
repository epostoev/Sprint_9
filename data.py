from pathlib import Path

APP_DIR = Path(__file__).parent


class URLS:
    BASE_URL = "https://foodgram-frontend-1.foodgram.education-services.ru"
    SIGNUP_URL = f"{BASE_URL}/signup"
    SIGNIN_URL = f"{BASE_URL}/signin"
    RECIPES_URL = f"{BASE_URL}/recipes"
    CREATE_RECIPE_URL = f"{BASE_URL}/recipes/create"


class RecipeData:
    NAME = "Тестовый рецепт картофельный"
    INGREDIENT = "картофель"
    INGREDIENT_AMOUNT = "200"
    COOKING_TIME = "30"
    DESCRIPTION = "Тестовое описание рецепта"
