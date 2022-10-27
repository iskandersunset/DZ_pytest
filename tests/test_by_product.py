from pages.cartpage import CartPage
from pages.loginpage import LoginPage
from pages.processorspage import CategoryPage


def test_by_processor(browser, set_up):

    lp = LoginPage(browser)
    citi = lp.get_geo_menu().text
    print('citi')
    assert citi == 'Челябинск'
    lp.choose_category()

    cgp = CategoryPage(browser)
    cgp.choose_product()

    cp = CartPage(browser)
    cp.confirm_order()
