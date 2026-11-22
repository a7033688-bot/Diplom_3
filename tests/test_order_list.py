import allure
from pages.main_page import MainPage
from pages.order_list_page  import OrderList
from data.urls import Url


class TestOrderList:

    @allure.title('при создании нового заказа счётчик «Выполнено за всё время» увеличивается')
    def test_when_a_new_order_is_created_completed_in_total_time_counter_increases(self,authorized_user):
        main_pages = MainPage(authorized_user)
        order_list = OrderList(authorized_user)
        main_pages.open_website()
        main_pages.click_to_order_list()
        number_up_to = order_list.we_receive_meter_number_registered_for_entire_period()
        order_list.click_to_constructor_button()
        main_pages.moving_ingredient_to_constructor()
        main_pages.click_place_order_button()
        main_pages.close_window_with_order_identifier()
        main_pages.click_to_order_list()
        number_after = order_list.we_receive_meter_number_registered_for_entire_period()
        assert number_after > number_up_to

    @allure.title('при создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
    def test_when_a_new_order_created_completed_today_counter_increases(self,authorized_user):
        main_pages = MainPage(authorized_user)
        order_list = OrderList(authorized_user)
        main_pages.open_website()
        main_pages.click_to_order_list()
        number_up_to = order_list.we_receive_counter_value_registered_today_before_placing_order()
        order_list.click_to_constructor_button()
        main_pages.moving_ingredient_to_constructor()
        main_pages.click_place_order_button()
        main_pages.close_window_with_order_identifier()
        main_pages.click_to_order_list()
        number_after = order_list.we_receive_counter_value_registered_today_before_placing_order()
        assert number_after > number_up_to

    @allure.title('после оформления заказа его номер появляется в разделе «В работе»')
    def test_after_placing_an_order_number_is_displayed_in_in_progress_section(self,authorized_user):
        main_pages = MainPage(authorized_user)
        order_list = OrderList(authorized_user)
        main_pages.open_website()
        main_pages.moving_ingredient_to_constructor()
        main_pages.click_place_order_button()
        number = main_pages.we_remember_order_number()
        main_pages.close_window_with_order_identifier()
        main_pages.click_to_order_list()
        number_already = order_list.we_re_reviewing_current_orders()
        assert '0' + number in number_already 

