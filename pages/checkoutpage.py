from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from base.baseapp import BasePage


class CheckoutPage(BasePage):

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
        return self.find_element(self.page_title)


    '''Actions'''
    def click_button_submit(self):
        self.get_button_submit().click()
        print(" === Click Citi Chelyabinsk === ")

    '''Methods'''
    def confirm_order(self):
        self.assert_url('https://www.citilink.ru/order/')
        self.assert_word(self.get_page_title(), 'Корзина')
        self.click_button_submit()

