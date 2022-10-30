from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By

from base.baseapp import BasePage


class LoginPage(BasePage):
    # Locators============================
    close_button = (By.CLASS_NAME, "Tooltip__close-mini")  # Закрыть пределожение регистрации
    geo_menu = (By.CLASS_NAME, "MainHeader__city")  # Выбираем меню геолокации
    citi_select = (By.XPATH, "//a[@data-search='челябинск']")
    catalog_proc = (By.XPATH, "//a[@href='catalog/processory/']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Getters =============================

    def get_close_button(self):
        return self.driver.find_element(*self.close_button)

    def get_geo_menu(self):
        return self.driver.find_element(*self.geo_menu)

    def get_citi_select(self):
        return self.driver.find_element(*self.citi_select)

    def get_catalog_proc(self):
        return self.driver.find_element(*self.catalog_proc)

    # Actions =============================
    def click_close_button(self):
        try:
            self.get_close_button().click()
            print(" === Click close registration === " * 10)
        except ElementClickInterceptedException:
            self.get_close_button().click()
            print(" === Click close registration === " * 10)

    def click_geo_menu(self):
        self.get_geo_menu().click()
        print(" === Click Menu Geolocation === ")

    def click_city_select(self):
        self.get_citi_select().click()
        print(" === Click Citi Chelyabinsk === ")

    def click_catalog_proc(self):
        self.get_catalog_proc().click()
        print(" === Click Processors === ")

    # Methods =============================
    def choose_category(self):

        self.click_close_button()
        self.click_geo_menu()
        self.click_city_select()

        self.assert_word(self.get_geo_menu(), 'Челябинск')

        self.get_screenshot()

        self.click_catalog_proc()
        self.assert_url('https://www.citilink.ru/catalog/processory/')

        self.get_screenshot()
