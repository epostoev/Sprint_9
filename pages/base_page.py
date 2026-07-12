import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    
    def go_to_url(self, url):
        self.driver.get(url)
 
    def get_current_url(self):
        return self.driver.current_url

    def wait_for_url_contains(self, url_part, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url_part)
        )

    @allure.step("Вводим текст в поле")
    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
    
    @allure.step("Кликаем по элементу")
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()