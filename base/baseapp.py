import datetime
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome


class BasePage:

    def __init__(self, driver: Chrome):
        self.driver = driver
        self.base_url = 'https://www.citilink.ru/'

        driver.implicitly_wait(10)

    # def find_elements(self, locator, time=30):
    #     return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
    #                                                   message=f"Can't find elements by locator {locator}")
    #
    # def find_element(self, locator, time=30):
    #     return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
    #                                                   message=f"Can't find element by locator {locator}")


    def should_be_on_page(self, locator):
        element = self.driver.find_element(locator)
        assert element, f"Element {locator} does not found."
        return element

    """Method Get current URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(" ======> Current URL " + get_url)

    """Method Assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print(" === Good assert WORD ===>> ", result)

    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Python\\DZ_pytest\\screen\\' + name_screenshot)
        print(" === Screenshot Done === ")

    """Method Assert word"""

    def assert_url(self, result):
        url = self.driver.current_url
        assert url == result, f"Wrong url: {url}"
        print(" === Good assert URL === ")

    def assert_selected(self, checkbox):
        try:
            assert checkbox.is_selected()
            print(" === CheckBox Selected === ")
        except AssertionError:
            print(" === Troubles, troubles === ")

    def assert_locator(self, locator):
        try:
            assert locator
            print(" === Locator found === ")
        except AssertionError:
            print(" === Troubles, troubles === ")

    def go_to_site(self):
        return self.driver.get(self.base_url)
