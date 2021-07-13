import pytest, time
from login_page_var import *
from web_fixtures import *
from selenium.webdriver.support.ui import Select

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

    @pytest.mark.sorting
    def test_sort_low_to_high(self):
        self.login(good_user, all_passwords)
        options = Select(self.driver.find_element_by_class_name('product_sort_container'))
        options.select_by_visible_text('Price (low to high)')
        prices = []
        i = 0 
        time.sleep(3)
        for item in self.driver.find_elements_by_class_name('inventory_item_price'):
            number = float(item.text[1:])
            prices.append(number)
        while i < len(prices) - 1:
            assert prices[i] <= prices[i + 1]
            i += 1


    @pytest.mark.sorting
    def test_sort_high_to_low(self):
        self.login(good_user, all_passwords)
        options = Select(self.driver.find_element_by_class_name('product_sort_container'))
        options.select_by_visible_text('Price (high to low)')
        prices = []
        i = 0 
        time.sleep(3)
        for item in self.driver.find_elements_by_class_name('inventory_item_price'):
            number = float(item.text[1:])
            prices.append(number)
        while i < len(prices) - 1:
            assert prices[i] >= prices[i + 1]
            i += 1

    @pytest.mark.sorting
    def test_sort_a_to_z(self):
        self.login(good_user, all_passwords)
        options = Select(self.driver.find_element_by_class_name('product_sort_container'))
        options.select_by_visible_text('Name (A to Z)')
        names = []
        time.sleep(3)
        for name in self.driver.find_elements_by_class_name('inventory_item_name'):
            names.append(name.text)
        sorts = sorted(names)
        assert names == sorts

    @pytest.mark.sorting
    def test_sort_z_to_a(self):
        self.login(good_user, all_passwords)
        options = Select(self.driver.find_element_by_class_name('product_sort_container'))
        options.select_by_visible_text('Name (Z to A)')
        names = []
        time.sleep(3)
        for name in self.driver.find_elements_by_class_name('inventory_item_name'):
            names.append(name.text)
        reverse = sorted(names, reverse=True)
        assert names == reverse






        