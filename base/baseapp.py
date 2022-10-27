import datetime
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.citilink.ru/'

    def find_elements(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def find_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

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
        get_url = self.driver.current_url
        assert get_url == result
        print(" === Good assert URL === ")

    def assert_selected(self, checkbox):
        try:
            time.sleep(3)
            assert checkbox.is_selected()
            print(" === CheckBox Selected === ")
        except AssertionError:
            print(" === Troubles, troubles === ")

    def assert_locator(self, locator):
        try:
            time.sleep(2)
            assert locator
            print(" === Locator found === ")
        except AssertionError:
            print(" === Troubles, troubles === ")

    def go_to_site(self):
        return self.driver.get(self.base_url)
