import time

from selenium.webdriver.common.by import By

from base.baseapp import BasePage


class CheckoutPage(BasePage):

    """Locators"""

    page_title = (By.CLASS_NAME, "Checkout__title__text")
    product_checkout = (By.XPATH, "//*[@id='app-check-out']/div/div/div/div[2]/aside/div[2]/div/div/div/div/div"
                                  "/div/div/div/div/div[1]")
    product_price_checkout = (By.XPATH, "//*[@id='app-check-out']/div/div/div/div[2]/aside/div[2]/div/div/div"
                                        "/div/div/div/div/div/div/div[2]/span")
    total = (By.XPATH, "/html/body/div[2]/div/main/div[2]/div/div/div/div[2]/aside/div[4]/div[2]/span")
    delivery_price = (By.XPATH, "/html/body/div[2]/div/main/div[2]/div/div/div/div[2]/aside/div[3]/div[2]/span")
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
    house_number = '5'
    firstname = 'Iskander'
    lastname = 'Sunset'
    phonenum = '9080000000'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

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
    def city_text(self):
        print(self.get_input_citi().text)
        return self.get_input_citi().text

    def field_street(self, street):
        self.get_input_street().clear()
        self.get_input_street().send_keys(street)
        print("Input Street:", street)

    def field_house_number(self, house_number):
        self.get_input_house_number().clear()
        self.get_input_house_number().send_keys(house_number)
        print("Input House Number:", house_number)

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
        print(" === Click Delivery === ")

    def product_checkout_text(self):
        return self.get_product_checkout().text

    def product_price_checkout_text(self):
        return self.get_product_price_checkout().text

    def total_text(self):
        return self.get_total().text

    def product_delivery_price_text(self):
        return self.get_delivery_price().text

    def click_button_checkout(self):
        self.get_button_checkout().click()
        print(" === Click Go to checkout === ")

    '''Methods'''

    def fill_personal_data(self):
        self.assert_word(self.get_page_title(), 'Оформление заказа')
        self.get_screenshot()
        time.sleep(3)
        self.click_delivery()
        time.sleep(3)
        self.field_street(self.street)
        self.field_house_number(self.house_number)
        self.field_phone(self.phonenum)
        self.field_first_name(self.firstname)
        self.field_last_name(self.lastname)
        time.sleep(3)
        print('Как бы нажали оформить заказ')
