from selenium.webdriver.common.by import By


class SigninPageLocators:
    LINK_SIGNIN = (
        By.XPATH,
        ".//a[@href='/signin' and contains(@class,'styles_menuLink')]")
    INPUT_EMAIL = (By.XPATH, ".//input[@name='email']")
    INPUT_PASSWORD = (By.XPATH, ".//input[@name='password']")
    BUTTON_SUBMIT = (
        By.XPATH,
        ".//button[contains(@class,'style_button__1FFWl')]")
    # Форма авторизации — признак что мы на странице логина
    FORM_SIGNIN = (By.XPATH, ".//form")
