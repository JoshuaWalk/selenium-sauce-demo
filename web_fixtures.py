import pytest, time
from selenium import webdriver
from login_page_var import *

@pytest.fixture(params=['chrome', 'firefox'],scope='class')
def web_driver(request):
    if request.param == 'chrome':
        browser = webdriver.Chrome()
    if request.param == 'firefox':
        browser = webdriver.Firefox()
    request.cls.driver = browser
    yield
    browser.close()

@pytest.mark.usefixtures('web_driver')
class Basic_Test():
    def login(self, user_name, pass_word):
        self.driver.get(url)
        username = self.driver.find_element_by_id('user-name')
        password = self.driver.find_element_by_id('password')
        username.send_keys(user_name)
        password.send_keys(pass_word)
        password.submit()
        time.sleep(3)

    def click_button(self, button_id):
        button = self.driver.find_element_by_id(button_id)
        button.click()

    def click_button_class(self, class_name):
        button = self.driver.find_element_by_class_name(class_name)
        button.click()

class Store_Test(Basic_Test):
    def add_backpack(self):
        self.click_button('add-to-cart-sauce-labs-backpack')
    def add_bike_light(self):
        self.click_button('add-to-cart-sauce-labs-bike-light')
    def add_bolt_shirt(self):
        self.click_button('add-to-cart-sauce-labs-bolt-t-shirt')
    def add_jacket(self):
        self.click_button('add-to-cart-sauce-labs-fleece-jacket')
    def add_onsie(self):
        self.click_button('add-to-cart-sauce-labs-onesie')
    def add_t_shirt(self):
        self.click_button('add-to-cart-test.allthethings()-t-shirt-(red)')

    def remove_backpack(self):
        self.click_button('remove-sauce-labs-backpack')
    def remove_bike_light(self):
        self.click_button('remove-sauce-labs-bike-light')
    def remove_bolt_shirt(self):
        self.click_button('remove-sauce-labs-bolt-t-shirt')
    def remove_jacket(self):
        self.click_button('remove-sauce-labs-fleece-jacket')
    def remove_onsie(self):
        self.click_button('remove-sauce-labs-onesie')
    def remove_t_shirt(self):
        self.click_button('remove-test.allthethings()-t-shirt-(red)')

class Cart_Test(Store_Test):
    def get_to_cart(self):
        self.click_button_class('shopping_cart_link')

    def check_out(self):
        self.click_button('checkout')

    def one_item_cart(self):
        self.add_backpack()
        self.get_to_cart()

    def three_item_cart(self):
        self.add_t_shirt()
        self.add_bike_light()
        self.add_jacket()
        self.get_to_cart()

    def all_item_cart(self):
        self.add_backpack()
        self.add_bike_light()
        self.add_bolt_shirt()
        self.add_jacket()
        self.add_onsie()
        self.add_t_shirt()
        self.get_to_cart()