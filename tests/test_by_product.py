import time

# import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import Login_page
from pages.processors_page import Processors_page


# @pytest.mark.run(order=1)
def test_by_processor(set_group):
    s = Service('C:/_teach/resource/chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    print('START TEST 1')

    login = Login_page(driver)
    login.geolocation()

    pp = Processors_page(driver)
    pp.price_set()

    print('FINISH TEST 1')
    time.sleep(10)

