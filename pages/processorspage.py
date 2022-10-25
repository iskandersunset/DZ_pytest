import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class ProcessorsPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators============================
    price_slider_left = "/html/body/div[3]/div[2]/main/section/div[1]/div[2]/div/div/div[2]" \
                        "/div[2]/div/div[3]/div[2]/div[3]/div/div[4]"
    price_slider_right = "/html/body/div[3]/div[2]/main/section/div[1]/div[2]/div/div/div[2]" \
                         "/div[2]/div/div[3]/div[2]/div[3]/div/div[5]"
    proc_brand = "//input[@id='intel']"
    proc_num_core = "//input[@id='8554_2612']"
    sort_by_price = "//div[@data-alias='price']"
    product = "ProductCardHorizontal__title"
    button_add_cart = "ProductCardHorizontal__button_car"

    # Getters=============================

    def get_price_slider_left(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_slider_left)))

    def get_price_slider_right(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_slider_right)))

    def get_proc_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.proc_brand)))

    def get_proc_num_core(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.proc_num_core)))

    def get_sort_by_price(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.sort_by_price)))

    '''Выбираем самый дорогой товар, список отсортирован по убыванию цены.'''
    def get_product(self):
        return self.driver.find_elements(By.CLASS_NAME, self.product)[0]

    def get_button_add_cat(self):
        return self.driver.find_elements(By.CLASS_NAME, self.button_add_cart)[0]

    # Actions =============================
    def move_price_slider_left(self):
        move = ActionChains(self.driver)
        move.click_and_hold(self.get_price_slider_left()).move_by_offset(50, 0).release().perform()
        print(" === Move left slide === ")

    def move_price_slider_right(self):
        move = ActionChains(self.driver)
        move.click_and_hold(self.get_price_slider_right()).move_by_offset(-20, 0).release().perform()
        print(" === Move right slider === ")

    def checkbox_proc_brand(self):
        self.driver.execute_script("arguments[0].scrollIntoView(); window.scrollBy(0, -window.innerHeight / 4);",
                                   self.get_proc_brand())
        self.get_proc_brand().click()
        print(" === Choose a brand === ")

    def checkbox_proc_num_core(self):
        self.driver.execute_script("arguments[0].scrollIntoView(); window.scrollBy(0, -window.innerHeight / 4);",
                                   self.get_proc_num_core())
        self.get_proc_num_core().click()
        print(" === Choose the number of cores === ")

    def click_sort_by_price(self):
        self.driver.execute_script("window.scrollTo(0, -document.body.scrollTop);")
        self.get_sort_by_price().click()
        self.get_sort_by_price().click()
        print(" === Click sort by price === ")

    # Methods =============================
    def price_set(self):
        self.move_price_slider_left()
        time.sleep(3)
        self.move_price_slider_right()
        time.sleep(3)
        self.checkbox_proc_brand()
        time.sleep(3)
        self.checkbox_proc_num_core()
        time.sleep(3)
        self.click_sort_by_price()