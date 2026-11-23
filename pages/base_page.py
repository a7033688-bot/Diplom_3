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

    @allure.step('Ожидает что Url содержит часть {url_part}')
    def wait_for_url(self,url_part):
        self.wait.until(EC.url_contains(url_part))
        return True

    @allure.step('получить текущий url')
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('клик по элементу')
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.js_click_element(element)

    @allure.step('клик по элементу через JavaSkript')
    def js_click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.js_click_element(element)

    @allure.step('вспомогательный метод выполняет клик по элементу средствами JavaSkript')
    def js_click_element(self,element):
        self.driver.execute_script(
            'if (arguments[0].click) {arguments[0].click();}'
            'else {arguments[0].dispatchEvent(new MouseEvent("click", {bubbles: true}));}',
            element
        )
        
    @allure.step('ожидание видимости элемента')
    def wait_for_visible(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step('ожидание исчезновения элемента')
    def wait_for_invisible(self,locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step('получение текста элемента')
    def get_text(self,locator):
        return self.wait_for_visible(locator).text

    @allure.step('перетаскивание элемента с помощью JavaSkript')
    def js_drag_and_drop(self, source_locator, target_locator):
        source = self.wait.until(EC.presence_of_element_located(source_locator))
        target = self.wait.until(EC.presence_of_element_located(target_locator))
        self.driver.execute_script(drag_drop, source, target)

    @allure.step('ожидание что исчезнет заглушка ')
    def wait_for_text(self, locator,value):

        def text_ready(d):
            element = d.find_element(*locator)
            text = element.text
            return text if text and text != value else False
        
        return self.wait.until(text_ready)
    
