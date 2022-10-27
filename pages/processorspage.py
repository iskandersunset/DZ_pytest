import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from base.baseapp import BasePage


class CategoryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators============================
    price_slider_left = (By.XPATH, "/html/body/div[3]/div[2]/main/section/div[1]/div[2]/div/div/div[2]"
                                   "/div[2]/div/div[3]/div[2]/div[3]/div/div[4]")
    price_slider_right = (By.XPATH, "/html/body/div[3]/div[2]/main/section/div[1]/div[2]/div/div/div[2]"
                                    "/div[2]/div/div[3]/div[2]/div[3]/div/div[5]")
    proc_brand = (By.XPATH, "//input[@id='intel']")
    proc_brand_check = (By.XPATH, "//input[@name='intel']")
    proc_num_core_check = (By.XPATH, "//input[@id='8554_2612']")
    sort_by_price = (By.CLASS_NAME, "SortingList__item")
    product = (By.CLASS_NAME, "ProductCardHorizontal__title")  # Наименование товара
    id_product = (By.CLASS_NAME, "ProductCardHorizontal__meta")  # ID товара
    product_price = (By.CLASS_NAME, "ProductCardHorizontal__button_desktop")  # Цена товара
    button_add_cart = (By.CLASS_NAME, "ProductCardHorizontal__button_desktop")
    cart_button = (By.CLASS_NAME, "HeaderMenu__buttons_basket")

    # Getters=============================

    def get_price_slider_left(self):
        return self.find_element(self.price_slider_left)

    def get_price_slider_right(self):
        return self.find_element(self.price_slider_right)

    def get_proc_brand(self):
        return self.find_element(self.proc_brand)

    def get_proc_num_core(self):
        return self.find_element(self.proc_num_core_check)

    def get_sort_by_price(self):
        return self.find_element(self.sort_by_price)

    '''Выбираем самый дорогой товар, список отсортирован по убыванию цены.'''

    def get_product(self):
        return self.find_elements(self.product)[0]

    def get_id_product(self):
        return self.find_elements(self.id_product)[0]

    def get_product_price(self):
        return self.find_elements(self.product_price)[0]

    def get_button_add_cart(self):
        return self.find_elements(self.button_add_cart)[0]

    def get_cart_button(self):
        return self.find_element(self.cart_button)

    # Actions =============================
    '''Move left slider'''

    def move_price_slider_left(self):
        move = ActionChains(self.driver)
        move.click_and_hold(self.get_price_slider_left()).move_by_offset(50, 0).release().perform()
        time.sleep(3)
        print(" === Move left slide === ")

    '''Move right slider'''

    def move_price_slider_right(self):
        try:
            move = ActionChains(self.driver)
            move.click_and_hold(self.get_price_slider_right()).move_by_offset(-20, 0).release().perform()
            print(" === Move right slider === ")
        except ElementClickInterceptedException:
            move = ActionChains(self.driver)
            move.click_and_hold(self.get_price_slider_right()).move_by_offset(-20, 0).release().perform()
            print(' --- ElementClickInterceptedException --- ')
            print(" === Move right slider === ")

    '''Checkbox Choose a brand'''

    def checkbox_proc_brand(self):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(); window.scrollBy(0, -window.innerHeight "
                                       "/ 4);", self.get_proc_brand())
            self.get_proc_brand().click()
            print(" === Choose a brand === ")
        except ElementClickInterceptedException:
            self.driver.refresh()
            self.driver.execute_script("arguments[0].scrollIntoView(); window.scrollBy(0, -window.innerHeight "
                                       "/ 4);", self.get_proc_brand())
            self.get_proc_brand().click()
            print(" --- ElementClickInterceptedException --- ")
            print(" === Choose a brand === ")

    '''Checkbox Choose the number of cores'''

    def checkbox_proc_num_core(self):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(); window.scrollBy(0, -window.innerHeight "
                                       "/ 4);", self.get_proc_num_core())
            self.get_proc_num_core().click()
            print(" === Choose the number of cores === ")
        except ElementClickInterceptedException:
            self.driver.refresh()
            self.driver.execute_script("arguments[0].scrollIntoView(); window.scrollBy(0, -window.innerHeight "
                                       "/ 4);", self.get_proc_num_core())
            self.get_proc_num_core().click()
            print(" --- ElementClickInterceptedException --- ")
            print(" === Choose the number of cores === ")

    '''Sort by price descending'''

    def click_sort_by_price(self):
        try:
            self.driver.execute_script("window.scrollTo(0, -document.body.scrollTop);")
            self.get_sort_by_price().click()
            self.get_sort_by_price().click()
            print(" === Click sort by price === ")
        except StaleElementReferenceException:
            self.driver.execute_script("window.scrollTo(0, -document.body.scrollTop);")
            self.get_sort_by_price().click()
            self.get_sort_by_price().click()
            print(" --- StaleElementReferenceException --- ")
            print(" === Click sort by price === ")

    '''Adding the selected product to the cart'''

    def click_button_add_cart(self):
        try:
            self.get_button_add_cart().click()
            print(" === Click Add to Cart === ")
            time.sleep(3)
            webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            print('=== Type Escape Button ===')
        except (StaleElementReferenceException, ElementClickInterceptedException):
            self.get_button_add_cart().click()
            print(" --- StaleElementReferenceException --- ")
            print(" === Click Add to Cart === ")
            time.sleep(3)  # Просто, для того чтобы увидеть окно всплывающее:)
            webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            print('=== Type Escape Button ===')

    def click_cart_button(self):
        try:
            self.get_cart_button().click()
            print(" === Click to Cart Button === ")
            time.sleep(2)
        except (StaleElementReferenceException, ElementClickInterceptedException):
            self.get_cart_button().click()
            print(" --- StaleElementReferenceException --- ")
            print(" === Click Add to Cart === ")
            time.sleep(2)
            print(" === Click to Cart Button === ")

    # Methods =============================
    def choose_product(self):
        self.move_price_slider_left()
        self.move_price_slider_right()
        self.checkbox_proc_brand()
        time.sleep(3)
        self.checkbox_proc_num_core()
        time.sleep(3)
        self.click_sort_by_price()
        self.click_button_add_cart()
        self.click_cart_button()
