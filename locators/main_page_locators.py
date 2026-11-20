from selenium.webdriver.common.by import By


class Main:
    button_order_list = [By.XPATH, ".//P[normalize-space()='Лента Заказов']"] # кнопка лента заказов на главной
    ingredient = [By.XPATH, ".//img[@alt='Краторная булка N-200i']"] # ингредиент на главной странице
    order_details = [By.XPATH, ".//h2[normalize-space()='Детали ингредиента']"] # окно детали заказа
    cross_order_details = [By.XPATH,".//section[contains(@class,'Modal_modal_opened__3ISw4')]//div//button//*[name()='svg']"] # крестик в окне детали заказа
    constructor = [By.XPATH, ".//span[@class='constructor-element__row']"] #конструктор бургера
    ingredient_counter = [By.XPATH, ".//a[@href='/ingredient/6ae327a87e8698001b542b38']//div//p[@class='counter_counter__num__3nue1']"] # счетчик ингредиента
    button_place_an_order = [By.XPATH,".//button[normalize-space()='Оформить заказ']"] #кнопка оформить заказ
    cross_order_identifier = [By.XPATH,".//section[contains(@class,'Modal_modal_opened__3ISw4')]//div//button//*[name()='svg']"] #крестик в окне идетификатор заказа
    order_number = [By.XPATH, "//p[text()='идентификатор заказа']/preceding-sibling::h2"]