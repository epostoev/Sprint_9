from selenium.webdriver.common.by import By
 
 
class RecipePageLocators:
    # Ссылка «Создать рецепт» в навигации
    CREATE_RECIPE_LINK = (By.XPATH, ".//a[text()='Создать рецепт']")
 
    # Поле «Название рецепта» — первый input на странице
    RECIPE_NAME_INPUT = (By.XPATH,
        "(.//input[contains(@class,'styles_inputField__3eqTj')])[1]")
 
    # Поле ввода ингредиента
    INGREDIENT_INPUT = (By.XPATH,
        ".//input[contains(@class,'styles_ingredientsInput__1zzql')]")
 
    # Первый элемент дропдауна ингредиентов
    INGREDIENT_DROPDOWN_ITEM = (By.XPATH,
        ".//div[contains(@class,'styles_container__3ukwm')]/div[1]")
 
    # Поле количества ингредиента
    INGREDIENT_AMOUNT_INPUT = (By.XPATH,
        ".//input[contains(@class,'styles_ingredientsAmountValue__2matT')]")
 
    # Кнопка «Добавить ингредиент»
    ADD_INGREDIENT_BUTTON = (By.XPATH,
        ".//div[contains(@class,'styles_ingredientAdd__3fc32')]")
 
    # Поле «Время приготовления»
    COOKING_TIME_INPUT = (By.XPATH,
        ".//div[contains(@class,'styles_ingredientsTimeInput__3oqdd')]"
        "//input[contains(@class,'styles_inputField__3eqTj')]")
 
    # Поле «Описание рецепта»
    DESCRIPTION_TEXTAREA = (By.XPATH,
        ".//textarea[contains(@class,'styles_textareaField__1wfhC')]")
 
    # Загрузка фото — input[type=file]
    PHOTO_INPUT = (By.XPATH,
        ".//input[contains(@class,'styles_fileInput__3HjP3')]")
 
    # Кнопка «Создать рецепт»
    SUBMIT_BUTTON = (By.XPATH, ".//button[text()='Создать рецепт']")
 
    # Заголовок созданного рецепта на странице просмотра
    RECIPE_CARD_TITLE = (By.XPATH,
        ".//h1[contains(@class,'styles_single-card__title')]")