import pytest

from selenium.webdriver import Chrome, ChromeOptions

from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth


@pytest.fixture(scope="session")
def driver():
    service = Service('C:/_teach/resource/chromedriver.exe')  # Путь на работе

    options = ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument('log-level=3')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = Chrome(options=options, service=service)

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
def setup():
    print(" >>> Start TEST <<< ")
    yield
    print(" >>> Finish TEST <<< ")


@pytest.fixture(scope="module")
def setup_group():
    print(" >>> Enter System <<< ")
    yield
    print(" >>> Exit System <<< ")
