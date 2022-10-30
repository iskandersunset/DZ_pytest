from pages.cartpage import CartPage
from pages.checkoutpage import CheckoutPage
from pages.loginpage import LoginPage
from pages.categorypage import CategoryPage

"""1) Заходим на https://www.citilink.ru/ (прверка), 2) выбираем категорию процессоры (проверка),
3) ограничиваем слайдером цену, выбираем бренд Intel(проверка), кол-во ядер 12(проверка), 
сортируем по убыванию цены(проверка), добавляем товар в корзину, закрываем всплывающее окно, 
переходим в корзину(проверка), 4) Сверяем цену и id товара с выбранной, жмем оформить
5) Выбираем доставку заполняем данные, сверяем наименование товара и цену с исходными."""


def test_by_processor(driver, setup):
    driver.implicitly_wait(10)

    login_page = LoginPage(driver)
    login_page.go_to_site()
    login_page.assert_url('https://www.citilink.ru/')
    login_page.choose_category()

    category_page = CategoryPage(driver)
    category_page.assert_word(category_page.get_title_page_proc(), 'Процессоры')
    category_page.choose_product()

    product = category_page.product_text()
    id_product = category_page.id_product_text()
    product_price = category_page.product_price_text()

    category_page.click_cart_button()

    cart_page = CartPage(driver)
    cart_page.assert_url('https://www.citilink.ru/order/')
    cart_page.assert_word(cart_page.get_page_title(), 'Корзина')

    product_price_cart = cart_page.product_price_cart_text().replace('₽', '')
    product_id_cart = cart_page.product_id_cart_text()

    assert id_product == product_id_cart, f"ID product {id_product} does not match."
    assert product_price == product_price_cart, f"Price {product_price} does not match."
    cart_page.confirm_order()

    checkout_page = CheckoutPage(driver)

    checkout_page.fill_personal_data()

    assert product == checkout_page.product_checkout_text(), f"Name product {product} does not match."
    print('Наименование товара совпало с исходным')
    assert (int(checkout_page.total_text().replace(' ', '')) - int(checkout_page.product_delivery_price_text())) == \
           int(product_price), f"Price product {product_price} does not match."
    print('Цена товара корректна')
