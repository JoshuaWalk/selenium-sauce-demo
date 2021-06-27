from web_fixtures import *
import pytest


class Test_Cart(Cart_Test):
    @pytest.mark.cart
    def test_cart_page(self):
        self.login(good_user, all_passwords)
        self.get_to_cart()
        assert self.driver.current_url == ('https://www.saucedemo.com/cart.html')

    @pytest.mark.cart
    def test_one_item_checkout(self):
        self.login(good_user, all_passwords)
        self.one_item_cart()
        self.get_to_cart()
        assert self.driver.current_url == ('https://www.saucedemo.com/checkout-step-one.html')

    @pytest.mark.checkout
    def test_no_last_name(self):
        self.login(good_user, all_passwords)
        self.three_item_cart()
        self.get_to_cart()
        self.check_out()
        self.check_out_form('josh', '', '83554')
        error_msg = self.driver.find_element_by_class_name('error-message-container')
        assert error_msg.text == 'Error: Last Name is required'

    @pytest.mark.checkout
    def test_no_first_name(self):
        self.login(good_user, all_passwords)
        self.get_to_cart()
        self.check_out()
        self.check_out_form('', 'josh', '83554')
        error_msg = self.driver.find_element_by_class_name('error-message-container')
        assert error_msg.text == 'Error: First Name is required'

    @pytest.mark.checkout
    def test_no_zip(self):
        self.login(good_user, all_passwords)
        self.get_to_cart()
        self.check_out()
        self.check_out_form('josh', 'walk', '')
        error_msg = self.driver.find_element_by_class_name('error-message-container')
        assert error_msg.text == 'Error: Postal Code is required'
