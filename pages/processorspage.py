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

    # Getters=============================

    def get_price_slider_left(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_slider_left)))

    def get_price_slider_right(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_slider_right)))

    def get_proc_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.proc_brand)))

    def get_proc_num_core(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.proc_num_core)))

    # Actions =============================
    def move_price_slider_left(self):
        move = ActionChains(self.driver)
        move.click_and_hold(self.get_price_slider_left()).move_by_offset(50, 0).release().perform()
        print(" === Левый ползунок тащим === ")

    def move_price_slider_right(self):
        move = ActionChains(self.driver)
        move.click_and_hold(self.get_price_slider_right()).move_by_offset(-20, 0).release().perform()
        print(" === Правый ползунок тащим === ")

    def checkbox_proc_brand(self):
        self.driver.execute_script("arguments[0].scrollIntoView(); window.scrollBy(0, -window.innerHeight / 4);",
                                   self.get_proc_brand())
        self.get_proc_brand().click()
        print(" === Выбираем бренд === ")

    def checkbox_proc_num_core(self):
        self.driver.execute_script("arguments[0].scrollIntoView(); window.scrollBy(0, -window.innerHeight / 4);",
                                   self.get_proc_num_core())
        self.get_proc_num_core().click()
        print(" === Выбираем бренд === ")

    # Methods =============================
    def price_set(self):
        self.move_price_slider_left()
        time.sleep(3)
        self.move_price_slider_right()
        time.sleep(5)
        self.checkbox_proc_brand()
        time.sleep(5)
        self.checkbox_proc_num_core()
