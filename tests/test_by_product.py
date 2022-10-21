import time

# import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import Login_page


# @pytest.mark.run(order=1)
def test_by_product_1(set_group):
    s = Service('C:/_teach/resource/chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    print('START TEST 1')

    login = Login_page(driver)
    login.geolocation()

    print('FINISH TEST 1')
    time.sleep(10)

