import allure
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from locators.main_page_locators import Main
from pages.base_page import BasePages


class MainPage(BasePages):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Main
        self.actions = ActionChains(driver)

    @allure.step('переход по клику на кнопку лента заказов в шапке')
    def click_to_order_list(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.button_order_list)).click()

    @allure.step('клик по ингредиенту в конструкторе')
    def click_to_ingredient(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.ingredient)).click()

    @allure.step('дождатся пока окно детали заказа появится')
    def window_with_detailed_information_about_order_will_open(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.order_details))

    @allure.step('клик по крестику в окне детали заказа')
    def click_to_cross_order_details(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.cross_order_details)).click()

    @allure.step('проверка наличия окна детали заказа')
    def window_with_detailed_information_about_order_will_close(self):
        self.wait.until(EC.invisibility_of_element_located(self.locators.order_details))

    @allure.step('перемещение ингредиента в конструктор')
    def moving_ingredient_to_constructor(self):
        source = self.wait.until(EC.visibility_of_element_located(self.locators.ingredient))
        target = self.wait.until(EC.visibility_of_element_located(self.locators.constructor))
        self.actions.drag_and_drop(source, target).perform()

    @allure.step('счетчик ингредиента изменился')
    def ingredient_counter_check(self):
        element = self.wait.until(EC.visibility_of_element_located(self.locators.ingredient_counter))
        return element.text

    @allure.step('нажимаем кнопку оформить заказ')
    def click_place_order_button(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.button_place_an_order)).click()

    @allure.step('закрываем окно идентификатор заказа')
    def close_window_with_order_identifier(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.cross_order_identifier)).click()

    @allure.step('запоминаем номер заказа')
    def we_remember_order_number(self):
        time.sleep(1)
        element = self.wait.until(EC.visibility_of_element_located(self.locators.order_number))
        return element.text

    