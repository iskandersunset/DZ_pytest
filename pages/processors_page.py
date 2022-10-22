import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Processors_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators============================
    price_slider_left = "/html/body/div[3]/div[2]/main/section/div[1]/div[2]/div/div/div[2]" \
                        "/div[2]/div/div[3]/div[2]/div[3]/div/div[4]"
    price_slider_right = "/html/body/div[3]/div[2]/main/section/div[1]/div[2]/div/div/div[2]" \
                         "/div[2]/div/div[3]/div[2]/div[3]/div/div[5]"

    # Getters=============================

    def get_price_slider_left(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_slider_left)))

    def get_price_slider_right(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_slider_right)))

    # Actions =============================
    def move_price_slider_left(self):
        move = ActionChains(self.driver)
        move.click_and_hold(self.get_price_slider_left()).move_by_offset(50, 0).release().perform()
        print(" === Левый ползунок тащим === ")

    def move_price_slider_right(self):
        move = ActionChains(self.driver)
        move.click_and_hold(self.get_price_slider_right()).move_by_offset(-20, 0).release().perform()
        print(" === Правый ползунок тащим === ")

    # Methods =============================
    def price_set(self):
        self.move_price_slider_left()
        time.sleep(3)
        self.move_price_slider_right()
