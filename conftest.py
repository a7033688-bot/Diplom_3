import pytest
import requests
import copy
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import Main
from data.urls import Url
from helpers import generate_user


@pytest.fixture(scope='function', params =['chrome','firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f'Неизвестный браузер')
    driver.set_window_size(1920,1080)
    driver.implicitly_wait(5)
    driver.set_page_load_timeout(20)
    driver.set_script_timeout(10)
    yield driver
    driver.quit()
    
@pytest.fixture(scope='function')
def user():
    user = generate_user()
    response = requests.post(Url.url + Url.user_creation_api , json=user)
    assert response.status_code ==200 ,f'регистрация не удалась {response.text}'
    user = copy.deepcopy(user)
    del user['name']
    response = requests.post(Url.url + Url.user_authorization_api,json=user)
    user['access_token'] = response.json()['accessToken']
    user['refresh_token'] = response.json()['refreshToken']
    yield user 
    requests.delete(Url.url + Url.user_delete_api , headers={'Authorization': user['access_token']})

@pytest.fixture(scope='function')
def authorized_user(driver,user):
    driver.get(Url.url)
    driver.execute_script("window.localStorage.setItem('accessToken',arguments[0]);"
                          "window.localStorage.setItem('refreshToken',arguments[1]);",
                          user['access_token'],
                          user['refresh_token'])
    driver.get(Url.url)
    WebDriverWait(driver,15).until(EC.visibility_of_element_located(Main.button_order_list))
    return driver

    
    
    