import time

from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# @pytest.mark.run(order=1)
s = Service('C:/_teach/resource/chromedriver.exe')  # Путь на работе
options = webdriver.ChromeOptions()
options.add_argument('log-level=3')
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
# close_button = "//*[@id='app-filter']/div/div[2]/div[2]/div/div[3]/div[3]/div[5]/div[1]/div"
proc_brand = "//input[@id='intel']"
proc_brand = (By.XPATH, "//input[@id='intel']")
geo_menu = (By.CLASS_NAME, "MainHeader__city")  # Выбираем меню геолокации
title_page_proc = (By.CLASS_NAME, "Subcategory__title")  # Выбираем меню геолокации
sort_by_price_check = (By.CLASS_NAME, "SortingList__svg_desc")
sort_by_price = (By.XPATH, "//div[@data-alias='price']")


driver.get(base_url)
driver.refresh()
# element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, close_button)))
# checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, proc_brand)))
# driver.execute_script("arguments[0].scrollIntoView(); window.scrollBy(0, -window.innerHeight / 4);", checkbox)
# checkbox.click()
# time.sleep(7)
# driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")  # В начало страницы
# sort_by_price = "//div[@data-alias='price']"
sort = WebDriverWait(driver, 10).until(EC.presence_of_element_located(sort_by_price))
sort.click()
sort.click()
time.sleep(2)
price = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(sort_by_price_check))

# price.click()

# products = driver.find_element(By.CLASS_NAME, "Subcategory__title")
# print(products.text)
# time.sleep(5)
# driver.execute_script("arguments[0].scrollIntoView(); window.scrollBy(0, -window.innerHeight / 4);", price)
# print(price.is_selected())

time.sleep(5)
assert price
print('Сортировка по убыванию цены реализована')




driver.quit()


