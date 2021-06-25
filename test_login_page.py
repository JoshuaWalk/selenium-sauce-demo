import pytest, time
from login_page_var import *
from web_fixtures import *

@pytest.mark.login
class Test_Login(Basic_Test):
    def test_valid_login(self):
        self.login(good_user, all_passwords)
        title = self.driver.find_element_by_class_name('title').text
        assert title == 'PRODUCTS'

    def test_locked_login(self):
        self.login(locked_user, all_passwords)
        error_message = 'Epic sadface: Sorry, this user has been locked out.'
        error_div = self.driver.find_element_by_class_name('error-message-container')
        assert error_div.text == error_message

    def test_problem_login(self):
        self.login(problem_user, all_passwords)
        title = self.driver.find_element_by_class_name('title').text
        assert title == 'PRODUCTS'

    def test_glitch_login(self):
        self.login(glitched_user, all_passwords)
        title = self.driver.find_element_by_class_name('title').text
        assert title == 'PRODUCTS'