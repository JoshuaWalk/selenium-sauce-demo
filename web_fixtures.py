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
