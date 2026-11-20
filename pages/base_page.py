import allure
from selenium.webdriver.support.ui import WebDriverWait
from data.urls import Url


class BasePages:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    @allure.step('Открыть тестируемый сайт')
    def open_website(self):
        self.driver.get(Url.url)
