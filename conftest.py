import pytest
import requests
import copy
from selenium import webdriver
from data.urls import Url
from helpers import generate_user

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
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
    return driver

    
    
    