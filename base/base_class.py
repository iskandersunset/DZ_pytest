import datetime
from termcolor import colored, cprint


class Base:

    def __init__(self, driver):
        self.driver = driver

    """Method Get current URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        cprint("Current URL " + get_url, 'yellow', 'on_blue')

    """Method Assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        cprint(" === Good value WORD === ", 'yellow', 'on_blue')

    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Python\\DZ_pytest\\screen\\' + name_screenshot)
        cprint(" === Screenshot Done ===", 'yellow', 'on_blue')

    """Method Assert word"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        cprint(" === Good value URL === ", 'yellow', 'on_blue')
