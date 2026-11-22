import allure
from pages.main_page import MainPage
from pages.order_list_page  import OrderList
from data.urls import Url


class TestBasicFunctionalityCheck:

    @allure.title('переход на страницу заказов нажатием кнопки лента заказов')
    def test_click_to_go_to_order_feed_section(self,driver):
        main_pages = MainPage(driver)
        main_pages.open_website()
        main_pages.click_to_order_list()
        assert main_pages.wait_for_url(Url.order_list) 

    @allure.title('переход на страницу конструктора нажатием кнопки конструктор')
    def test_click_to_constructor_button(self,driver):
        order_pages = OrderList(driver)
        order_pages.open_website()
        order_pages.click_to_constructor_button()
        assert order_pages.get_current_url() == Url.url

    @allure.title('при нажатий на ингредиент появляется окно детали заказа')
    def test_window_with_order_details_will_open(self,driver):
        main_pages = MainPage(driver)
        main_pages.open_website()
        main_pages.click_to_ingredient()
        main_pages.window_with_detailed_information_about_order_will_open()
        assert Url.ingredient in main_pages.get_current_url()

    @allure.title('при клике на крестик детали заказа окно детали заказа закрывается')
    def test_сlosing_order_details_window(self,driver):
        main_pages = MainPage(driver)
        main_pages.open_website()
        main_pages.click_to_ingredient()
        main_pages.window_with_detailed_information_about_order_will_open()
        main_pages.click_to_cross_order_details()
        main = main_pages.window_with_detailed_information_about_order_will_close()
        assert main == True

    @allure.title('при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_when_an_ingredient_is_added_to_an_order_counter_for_ingredient_increases(self,driver):
        main_pages = MainPage(driver)
        main_pages.open_website()
        main_pages.moving_ingredient_to_constructor()
        assert main_pages.ingredient_counter_check() == '2'
        