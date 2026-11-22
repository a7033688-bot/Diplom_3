import allure
from selenium.webdriver.support.ui import WebDriverWait
from data.urls import Url
from selenium.webdriver.support import expected_conditions as EC
from helpers import drag_drop
from selenium.common.exceptions import ElementClickInterceptedException


class BasePages:

    def __init__(self,driver, timeaut = 15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeaut)

    @allure.step('Открыть тестируемый сайт')
    def open_website(self):
        self.driver.get(Url.url)

    def wait_for_url(self,url_part):
        self.wait.until(EC.url_contains(url_part))
        return True

    def get_current_url(self):
        return self.driver.current_url

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script('arguments[0].click();', element)


    def js_click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script('arguments[0].click();',element)

    def wait_for_visible(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_invisible(self,locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def get_text(self,locator):
        return self.wait_for_visible(locator).text

    def js_drag_and_drop(self, source_locator, target_locator):
        source = self.wait.until(EC.presence_of_element_located(source_locator))
        target = self.wait.until(EC.presence_of_element_located(target_locator))
        self.driver.execute_script(drag_drop, source, target)
