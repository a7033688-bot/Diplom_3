import allure
from locators.main_page_locators import Main
from pages.base_page import BasePages



class MainPage(BasePages):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Main

    @allure.step('переход по клику на кнопку лента заказов в шапке')
    def click_to_order_list(self):
        self.js_click(self.locators.button_order_list)
        
    @allure.step('клик по ингредиенту в конструкторе')
    def click_to_ingredient(self):
        self.click(self.locators.ingredient)

    @allure.step('дождатся пока окно детали заказа появится')
    def window_with_detailed_information_about_order_will_open(self):
        self.wait_for_visible(self.locators.order_details)

    @allure.step('клик по крестику в окне детали заказа')
    def click_to_cross_order_details(self):
        self.click(self.locators.cross_order_details)

    @allure.step('проверка наличия окна детали заказа')
    def window_with_detailed_information_about_order_will_close(self):
        self.wait_for_invisible(self.locators.order_details)
        return True 

    @allure.step('перемещение ингредиента в конструктор')
    def moving_ingredient_to_constructor(self):
        self.js_drag_and_drop(self.locators.ingredient, self.locators.constructor)
        

    @allure.step('счетчик ингредиента изменился')
    def ingredient_counter_check(self):
        return self.get_text(self.locators.ingredient_counter)

    @allure.step('нажимаем кнопку оформить заказ')
    def click_place_order_button(self):
        self.js_click(self.locators.button_place_an_order)

    @allure.step('закрываем окно идентификатор заказа')
    def close_window_with_order_identifier(self):
        self.click(self.locators.cross_order_identifier)

    @allure.step('запоминаем номер заказа')
    def we_remember_order_number(self):
        element = self.wait_for_visible(self.locators.order_number)
        self.wait.until(lambda d: element.text if element.text != '9999' else False)
        return element.text

    