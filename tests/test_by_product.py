from pages.cartpage import CartPage
from pages.loginpage import LoginPage
from pages.processorspage import CategoryPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_by_processor(browser, set_up):

    lp = LoginPage(browser)
    lp.go_to_site()
    lp.assert_url('https://www.citilink.ru/')
    lp.choose_category()

    cgp = CategoryPage(browser)
    cgp.assert_word(cgp.get_title_page_proc(), 'Процессоры')
    cgp.choose_product()

    # cp = CartPage(browser)
    # cp.confirm_order()
