from pathlib import Path

APP_DIR = Path(__file__).parent

class URLS:
    BASE_URL = "https://foodgram-frontend-1.foodgram.education-services.ru"
    SIGNUP_URL = f"{BASE_URL}/signup"
    SIGNIN_URL = f"{BASE_URL}/signin"
    RECIPES_URL = f"{BASE_URL}/recipes"
    CREATE_RECIPE_URL = f"{BASE_URL}/recipes/create"


class UserData:
    FIRST_NAME = "QATester"
    LAST_NAME = "LastQATester"
    USERNAME = "testuser_autoqa"
    EMAIL = "test_user_qa@yandex.ru"
    PASSWORD = "Test1234!"
