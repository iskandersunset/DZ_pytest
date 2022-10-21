from termcolor import colored, cprint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_page(Base):
    base_url = 'https://citilink.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators============================

    close_button = "Tooltip__close-mini"  # Закрыть прделожение регистрации
    geo_menu = "MainHeader__city"  # Выбираем меню геолокации
    citi_select = "//a[@data-search='челябинск']"
    catalog_proc = "//a[@href='catalog/processory/']"

    # Getters=============================

    def get_close_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, self.close_button)))

    def get_geo_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, self.geo_menu)))

    def get_citi_select(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.citi_select)))

    def get_catalog_proc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_proc)))

    # Actions =============================
    def click_close_button(self):
        self.get_close_button().click()
        cprint(" === Click close registration === " * 10, 'yellow', 'on_blue')

    def click_geo_menu(self):
        self.get_geo_menu().click()
        cprint(" === Click Menu Geolocation === ", 'yellow', 'on_blue')

    def click_citi_select(self):
        self.get_citi_select().click()
        cprint(" === Click Citi Chelyabinsk === ", 'yellow', 'on_blue')

    def click_catalog_proc(self):
        self.get_catalog_proc().click()
        cprint(" === Click Processors === ", 'yellow', 'on_blue')

    # Methods =============================
    def geolocation(self):
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.get_current_url()
        self.click_close_button()
        self.click_geo_menu()
        self.click_citi_select()
        self.click_catalog_proc()
        self.get_current_url()
        self.get_screenshot()
        self.assert_url('https://www.citilink.ru/catalog/processory/')
        self.get_screenshot()
        # self.assert_word(self.get_main_word(), 'PRODUCTS')

