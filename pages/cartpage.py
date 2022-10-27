from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from base.baseapp import BasePage


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    '''Locators'''

    page_title = (By.CLASS_NAME, "Basket__title__text")
    product_cart = (By.CLASS_NAME, "ProductCardForBasket__name")
    id_product_cart = (By.CLASS_NAME, "ProductCardForBasket__vendor-code")
    product_price_cart = (By.CLASS_NAME, "ProductCardForBasket__price-current")
    button_submit = (By.CLASS_NAME, "OrderFinalPrice__order-button")

    '''Getters'''
    def get_page_title(self):
        print(self.find_element(self.page_title).text)
        return self.find_element(self.page_title)

    def get_product_cart(self):
        print(self.find_element(self.product_cart).text)
        return self.find_element(self.product_cart)

    def get_id_product_cart(self):
        print(self.find_element(self.id_product_cart).text)
        return self.find_element(self.id_product_cart)

    def get_product_price_cart(self):
        print(self.find_element(self.product_price_cart).text)
        return self.find_element(self.product_price_cart)

    def get_button_submit(self):
        return self.find_element(self.button_submit)

    '''Actions'''
    def click_button_submit(self):
        self.get_button_submit().click()
        print(" === Click Go to checkout === ")

    '''Methods'''
    def confirm_order(self):
        self.assert_url('https://www.citilink.ru/order/')
        self.assert_word(self.get_page_title(), 'Корзина')
        self.click_button_submit()

