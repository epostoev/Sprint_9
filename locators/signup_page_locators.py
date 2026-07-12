from selenium.webdriver.common.by import By


class SignupPageLocators:
    
    LINK_CREATE_ACCOUNT = (By.XPATH, ".//a[@href='/signup']")

    # Поля формы регистрации
    INPUT_FIRST_NAME = (By.XPATH, ".//input[@name='first_name']")
    INPUT_LAST_NAME = (By.XPATH, ".//input[@name='last_name']")
    INPUT_USERNAME = (By.XPATH, ".//input[@name='username']")
    INPUT_EMAIL = (By.XPATH, ".//input[@name='email']")
    INPUT_PASSWORD = (By.XPATH, ".//input[@name='password']")

    # Кнопка сабмита формы регистрации
    BUTTON_SUBMIT = (By.XPATH, ".//button[contains(@class,'style_button__1FFWl')]")