import sys

import pytest

from pages.cartpage import CartPage
from pages.checkoutpage import CheckoutPage
from pages.loginpage import LoginPage
from pages.categorypage import CategoryPage


def test_by_processor(driver, setup):
    driver.implicitly_wait(10)

    login_page = LoginPage(driver)
    login_page.go_to_site()
    login_page.assert_url('https://www.citilink.ru/')
    login_page.choose_category()

    category_page = CategoryPage(driver)
    category_page.assert_word(category_page.get_title_page_proc(), 'Процессоры')
    category_page.choose_product()

    id_product_value = category_page.id_product_text()
    product_price_value = category_page.product_price_text()

    category_page.click_cart_button()

    cart_page = CartPage(driver)
    cart_page.assert_url('https://www.citilink.ru/order/')
    print(cart_page.get_current_url())
    cart_page.assert_word(cart_page.get_page_title(), 'Корзина')

    assert id_product_value == cart_page.product_id_cart_text()
    print('Good assertion', id_product_value)
    assert product_price_value == cart_page.product_price_cart_text().replace('₽', '')
    print('Good assertion', product_price_value)
    cart_page.confirm_order()

    checkout_page = CheckoutPage(driver)
    checkout_page.confirm_checkout()
    checkout_page.get_screenshot()
