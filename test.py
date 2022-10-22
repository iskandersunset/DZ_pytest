import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# @pytest.mark.run(order=1)
s = Service('C:/_teach/resource/chromedriver.exe')  # Путь на работе
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
# options.add_argument("--headless")

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

base_url = 'https://www.citilink.ru/catalog/processory/'
close_button = "Tooltip__close-mini"  # Закрыть прделожение регистрации

driver.get(base_url)
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, close_button))).click()
time.sleep(3)
proc_num_core = "//input[@id='intel']"
move = driver.find_element(By.XPATH, proc_num_core)
driver.execute_script("arguments[0].scrollIntoView();", move)
time.sleep(3)
move.click()

