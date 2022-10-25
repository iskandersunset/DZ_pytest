import time

# import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
from pages.loginpage import LoginPage
from pages.processorspage import ProcessorsPage


# @pytest.mark.run(order=1)
def test_by_processor(set_group):
    s = Service('C:/_teach/resource/chromedriver.exe')  # Путь на работе

    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options, service=s)

    stealth(driver,
            languages=["ru-RU", "ru"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    print(' === START TEST ====')

    login = LoginPage(driver)
    login.geolocation()

    pp = ProcessorsPage(driver)
    pp.price_set()

    print(' === FINISH TEST === ')
    time.sleep(15)
    # driver.quit()

