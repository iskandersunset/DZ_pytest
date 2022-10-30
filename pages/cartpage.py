from selenium.webdriver.common.by import By

from base.baseapp import BasePage


class CartPage(BasePage):
    """Locators"""
    page_title = (By.XPATH, "/html/body/div[2]/div/main/div[1]/div/div[2]")
    product_cart = (By.CLASS_NAME, "ProductCardForBasket__name")
    id_product_cart = (By.CLASS_NAME, "ProductCardForBasket__vendor-code")
    product_price_cart = (By.CLASS_NAME, "ProductCardForBasket__price-current")
    button_submit = (By.CLASS_NAME, "OrderFinalPrice__order-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    '''Getters'''

    def get_page_title(self):
        return self.driver.find_element(*self.page_title)

    def get_product_cart(self):
        return self.driver.find_element(*self.product_cart)

    def get_id_product_cart(self):
        return self.driver.find_element(*self.id_product_cart)

    def get_product_price_cart(self):
        return self.driver.find_element(*self.product_price_cart)

    def get_button_submit(self):
        return self.driver.find_element(*self.button_submit)

    '''Actions'''

    def click_button_submit(self):
        self.get_button_submit().click()
        print(" === Click Go to checkout === ")

    def product_cart_text(self):
        return self.get_product_cart().text

    def product_id_cart_text(self):
        return self.get_id_product_cart().text.replace('Код товара: ', '')

    def product_price_cart_text(self):
        return self.get_product_price_cart().text.replace(' ', '')

    '''Methods'''

    def confirm_order(self):
        self.click_button_submit()
