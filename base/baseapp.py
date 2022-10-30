import datetime
from selenium.webdriver import Chrome


class BasePage:

    def __init__(self, driver: Chrome):
        self.driver = driver
        self.base_url = 'https://www.citilink.ru/'

        driver.implicitly_wait(15)

    def should_be_on_page(self, locator):
        element = self.driver.find_element(locator)
        assert element, f"Element {locator} does not found."
        return element

    """Method Get current URL"""

    def get_current_url(self):
        get_url = self.driver.current_url

    """Method Assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result, f"Word {result} does not match."
        print('Good assert', value_word)

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
        print(" === Good assert URL === ", result)

    def assert_selected(self, checkbox):
        try:
            assert checkbox.is_selected(), f"Checkbox {checkbox} not checked."
            print(" === CheckBox Selected === ")
        except AssertionError:
            print(" === Troubles, troubles === ")

    def assert_locator(self, locator):
        try:
            assert locator, f"Element {locator} does not found."
        except AssertionError:
            print(" === Troubles, troubles === ")

    def go_to_site(self):
        return self.driver.get(self.base_url)
