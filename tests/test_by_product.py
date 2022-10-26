import time

import pytest

# import pytest as pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium_stealth import stealth

from pages.loginpage import LoginPage
from pages.processorspage import ProcessorsPage


@pytest.mark.run()
def test_by_processor(browser, set_up):

    lp = LoginPage(browser)
    lp.geolocation()

    pp = ProcessorsPage(browser)
    pp.price_set()

    time.sleep(15)
