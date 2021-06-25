import pytest, time
from test_login_page import Basic_Test
from login_page_var import *
from web_fixtures import *

class Test_Shop(Basic_Test):
    def test_add_item(self):
        self.login(good_user, all_passwords)
        self.click_button('add-to-cart-sauce-labs-backpack')
        time.sleep(3)
        cart_amount = self.driver.find_element_by_class_name('shopping_cart_badge')
        assert cart_amount.text == '1'

    


        