import time

import pytest

from pages.cartpage import CartPage
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
    pp.choose_product()

    cp = CartPage(browser)
    cp.confirm_order()

    time.sleep(15)
