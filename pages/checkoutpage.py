import time

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
    page_title = (By.CLASS_NAME, "Checkout__title__text")
    product_checkout = (By.XPATH, "//*[@id='app-check-out']/div/div/div/div[2]/aside/div[2]/div/div/div/div/div"
                                  "/div/div/div/div/div[1]")
    product_price_checkout = (By.XPATH, "//*[@id='app-check-out']/div/div/div/div[2]/aside/div[2]/div/div/div"
                                        "/div/div/div/div/div/div/div[2]/span")
    total = (By.XPATH, "//*[@id='app-check-out']/div/div/div/div[2]/aside/div[4]/div[2]/span")
    delivery_price = (By.XPATH, "///*[@id='app-check-out']/div/div/div/div[2]/aside/div[3]/div[2]/span")
    button_delivery = (By.XPATH, "//*[@id='app-check-out']/div/div/div/div[1]/div[3]/div/div/div[2]/div/div[1]"
                                 "/div/div/div/div/div[1]/button[2]")
    input_citi = (By.XPATH, "//*[@id='app-check-out']/div/div/div/div[1]/div[3]/div/div/div[2]"
                            "/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/label/input")
    input_street = (By.XPATH, "//*[@id='app-check-out']/div/div/div/div[1]/div[3]/div/div/div[2]/div/div[1]/div/div"
                              "/div/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]/label/input")
    input_house_number = (By.XPATH, "//input[@name='house']")
    first_name = (By.XPATH, "//input[@name='firstName']")
    last_name = (By.XPATH, "//input[@name='lastName']")
    phone = (By.XPATH, "//input[@name='phone']")
    button_checkout = (By.XPATH, "//*[@id='app-check-out']/div/div/div/div[1]/div[4]/div/div[2]/div/div/div[7]/div[3]"
                                 "/div/button")
    street = 'Улица Ленина'
    housenum = '5'
    firstname = 'Iskander'
    lastname = 'Sunset'
    phonenum = '9080000000'

    '''Getters'''

    def get_page_title(self):
        return self.driver.find_element(*self.page_title)

    def get_button_delivery(self):
        return self.driver.find_element(*self.button_delivery)

    def get_product_checkout(self):
        return self.driver.find_element(*self.product_checkout)

    def get_product_price_checkout(self):
        return self.driver.find_element(*self.product_price_checkout)

    def get_total(self):
        return self.driver.find_element(*self.total)

    def get_delivery_price(self):
        return self.driver.find_element(*self.delivery_price)

    def get_input_citi(self):
        return self.driver.find_element(*self.input_citi)

    def get_input_street(self):
        return self.driver.find_element(*self.input_street)

    def get_input_house_number(self):
        return self.driver.find_element(*self.input_house_number)

    def get_first_name(self):
        return self.driver.find_element(*self.first_name)

    def get_last_name(self):
        return self.driver.find_element(*self.last_name)

    def get_phone(self):
        return self.driver.find_element(*self.phone)

    def get_button_checkout(self):
        return self.driver.find_element(*self.button_checkout)

    '''Actions'''
    def citi_text(self):
        print(self.get_input_citi().text)
        return self.get_input_citi().text

    # def field_citi(self):
    #     self.get_first_name().clear()
    #     self.get_first_name().send_keys(firstname)
    #     print("Input user_pass", firstname)
    #
    def field_street(self, street):
        self.get_input_street().clear()
        self.get_input_street().send_keys(street)
        print("Input Street:", street)

    def field_housenum(self, housenum):
        self.get_input_house_number().clear()
        self.get_input_house_number().send_keys(housenum)
        print("Input House Number:", housenum)

    def field_first_name(self, firstname):
        self.get_first_name().clear()
        self.get_first_name().send_keys(firstname)
        print("Input First Name:", firstname)

    def field_last_name(self, lastname):
        self.get_last_name().clear()
        self.get_last_name().send_keys(lastname)
        print("Input Last Name:", lastname)

    def field_phone(self, phonenum):
        self.get_phone().clear()
        self.get_phone().send_keys(phonenum)
        print("Input Phone Number:", phonenum)

    def click_delivery(self):
        self.get_button_delivery().click()
        print(" === Click Доставка === ")

    def product_checkout_text(self):
        print(self.get_product_checkout().text)
        return self.get_product_checkout().text

    def product_price_checkout_text(self):
        return self.get_product_price_checkout().text

    def total_text(self):
        print(self.get_total().text)
        return self.get_total().text

    def product_delivery_price_text(self):
        print(self.get_delivery_price().text)
        return self.get_delivery_price().text

    # def total_sum(self):
    #     total_sum_value = self.get_product_price_checkout()

    def click_button_checkout(self):
        self.get_button_checkout().click()
        print(" === Click Go to checkout === ")

    '''Methods'''

    def confirm_checkout(self):
        self.assert_word(self.get_page_title(), 'Оформление заказа')
        self.click_delivery()
        print(self.citi_text())
        self.field_street(self.street)
        self.field_housenum(self.housenum)
        self.field_phone(self.phonenum)
        self.field_first_name(self.firstname)
        self.field_last_name(self.lastname)
        print(self.product_checkout_text(), self.product_price_checkout_text(), self.total_text())
        # self.click_button_checkout()
        print('Как бы нажали оформить заказ')
