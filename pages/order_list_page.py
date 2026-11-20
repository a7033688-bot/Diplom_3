import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.order_list_pages_locators import Order
from pages.base_page import BasePages


class OrderList(BasePages):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Order

    @allure.step('переход по клику на кнопку Конструктор в ленте заказов')
    def click_to_constructor_button(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.constructor_button)).click()

    @allure.step('получаем число счетчика оформленно за все время до оформления заказа')
    def we_receive_meter_number_registered_for_entire_period(self):
        element = self.wait.until(EC.visibility_of_element_located(self.locators.completed_in_total))
        return element.text

    @allure.step('получаем число счетчика оформленно за сегодня до оформления заказа')
    def we_receive_counter_value_registered_today_before_placing_order(self):
        element = self.wait.until(EC.visibility_of_element_located(self.locators.orders_completed_during_day))
        return element.text

    @allure.step('смотрим заказы в работе')
    def we_re_reviewing_current_orders(self):
        element = self.wait.until(EC.visibility_of_element_located(self.locators.orders_being_processed))
        return element.text