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
    price_slider = "#app-filter > div > div.css-13fb20f.ely0d2x0 > div.css-1fvvpk9.ef363jm0 > " \
                   "div > div.e1514ezh0.css-1tn5u6r.elalcrq0 > div.e10glbzz0.css-1px02k5.ehx9ljd0 > " \
                   "div.css-zuxqkm.e2e6zdw0 > div > div.rc-slider-handle.rc-slider-handle-1"
    price_right = ""

    # Getters=============================

    def get_price_slider(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.price_slider)))

    # Actions =============================
    def click_price_slider(self):
        move = ActionChains(self.driver)
        move.click_and_hold(self.get_price_slider()).move_by_offset(20, 0).release().perform()
        print("Ползунок тащим левый")

    # Methods =============================
    def price_set(self):
        self.click_price_slider()
    #     self.click_select_product_1()
