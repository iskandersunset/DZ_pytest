from pages.cartpage import CartPage
from pages.loginpage import LoginPage
from pages.categorypage import CategoryPage
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
    product_value = cgp.product_text()
    id_product_value = cgp.id_product_text()
    product_price_value = cgp.product_price_text()
    cgp.click_cart_button()

    cp = CartPage(browser)
    cp.assert_url('https://www.citilink.ru/order/')
    cp.assert_word(cp.get_page_title, 'Корзина')
    assert product_value == cp.product_cart_text()
    assert id_product_value == cp.product_id_cart_text()
    assert product_price_value == cp.product_price_cart_text()
    # cp.confirm_order()
