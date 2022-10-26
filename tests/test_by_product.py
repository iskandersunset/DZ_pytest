import time

import pytest

from pages.cartpage import CartPage
# import pytest as pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium_stealth import stealth

from pages.loginpage import LoginPage
from pages.processorspage import CategoryPage


def test_by_processor(browser, set_up):

    lp = LoginPage(browser)
    lp.choose_category()

    cgp = CategoryPage(browser)
    cgp.choose_product()

    cp = CartPage(browser)
    cp.confirm_order()
