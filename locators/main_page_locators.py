from selenium.webdriver.common.by import By


class MainPageLocators:
    # Ссылка «Выход» в навигации
    LOGOUT_LINK = (By.XPATH, ".//a[text()='Выход']")

    # Ссылка «Войти» в хедере
    SIGNIN_LINK = (By.XPATH, ".//a[@href='/signin']")
