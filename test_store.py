import pytest, time
from test_login_page import Basic_Test
from login_page_var import *
from web_fixtures import *

@pytest.mark.shop
class Test_Shop(Store_Test):
    def test_add_item(self):
        self.login(good_user, all_passwords)
        self.add_backpack()
        time.sleep(3)
        cart_amount = self.driver.find_element_by_class_name('shopping_cart_badge')
        assert cart_amount.text == '1'
        self.remove_backpack()

    def test_add_3_items(self):
        self.login(good_user, all_passwords)
        self.add_bike_light()
        self.add_jacket()
        self.add_bolt_shirt()
        time.sleep(3)
        cart_amount = self.driver.find_element_by_class_name('shopping_cart_badge')
        assert cart_amount.text == '3'
        self.remove_bike_light()
        assert cart_amount.text == '2'
        self.remove_jacket()
        assert cart_amount.text == '1'
        self.remove_bolt_shirt()

    def test_add_all_items(self):
        self.login(good_user, all_passwords)
        self.add_backpack()
        self.add_bike_light()
        self.add_bolt_shirt()
        self.add_jacket()
        self.add_onsie()
        self.add_t_shirt()
        time.sleep(3)
        cart_amount = self.driver.find_element_by_class_name('shopping_cart_badge')
        assert cart_amount.text == '6'
        self.remove_backpack()
        assert cart_amount.text == '5'
        self.remove_bolt_shirt()
        assert cart_amount.text == '4'
        self.remove_jacket()
        assert cart_amount.text == '3'
        self.remove_onsie()
        assert cart_amount.text == '2'
        self.remove_bike_light()
        assert cart_amount.text == '1'
        self.remove_t_shirt()




        