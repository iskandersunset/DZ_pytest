import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth


@pytest.fixture(scope="session")
def browser():
    s = Service('C:/_teach/resource/chromedriver.exe')  # Путь на работе
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument('log-level=3')
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
    yield driver
    driver.quit()


@pytest.fixture(scope='module')
def set_up():
    print(" >>> Start TEST <<< ")
    yield
    print(" >>> Finish TEST <<< ")



@pytest.fixture(scope="module")
def set_group():
    print(" >>> Enter System <<< ")
    yield
    print(" >>> Exit System <<< ")

