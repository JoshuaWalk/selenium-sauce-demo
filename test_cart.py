from web_fixtures import *
import pytest

@pytest.mark.cart
class Test_Cart(Cart_Test):
    def test_cart_page(self):
        self.login(good_user, all_passwords)
        self.get_to_cart()
        assert self.driver.current_url == ('https://www.saucedemo.com/cart.html')

    def test_one_item_checkout(self):
        self.login(good_user, all_passwords)
        self.one_item_cart()
        self.get_to_cart()
        assert self.driver.current_url == ('https://www.saucedemo.com/checkout-step-one.html')