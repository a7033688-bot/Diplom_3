from selenium.webdriver.common.by import By


class Order:

    constructor_button = [By.XPATH, ".//P[normalize-space()='Конструктор']"] # кнопка конструктор в ленте заказов
    completed_in_total = [By.XPATH, ".//p[normalize-space()='Выполнено за все время:']/following-sibling::p"] # заказы выполненные за все время
    orders_completed_during_day = [By.XPATH, ".//p[normalize-space()='Выполнено за сегодня:']/following-sibling::p"] #заказы выполненные сегодня
    orders_being_processed = [By.XPATH, ".//ul[contains(@class,'OrderFeed_orderListReady__1YFem')]//li"] 