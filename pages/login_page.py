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

    # Getters=============================

    def get_close_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, self.close_button)))

    def get_geo_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, self.geo_menu)))

    def get_citi_select(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.citi_select)))

    # Actions =============================
    def click_close_button(self):
        self.get_close_button().click()
        print("Click close registration")

    def click_geo_menu(self):
        self.get_geo_menu().click()
        print("Click Menu Geolocation")

    def click_citi_select(self):
        self.get_citi_select().click()
        print("Click Citi Chelyabinsk")

    # Methods =============================
    def geolocation(self):
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.get_current_url()
        self.click_close_button()
        self.click_geo_menu()
        self.click_citi_select()
        # self.init_user_name("standard_user")
        # self.init_user_pass("secret_sauce")
        # self.click_login_button()
        # self.assert_word(self.get_main_word(), 'PRODUCTS')

