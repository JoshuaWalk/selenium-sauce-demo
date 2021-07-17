import pytest
from login_page_var import *
from web_fixtures import *

@pytest.mark.login
class Test_Login(Basic_Test):
    def test_valid_login(self):
        self.login(good_user, all_passwords)
        title = self.driver.find_element_by_class_name('title').text
        assert title == 'PRODUCTS'

    @pytest.mark.xfail
    def test_bad_pass(self):
        self.login(good_user, 'all_passwords')
        title = self.driver.find_element_by_class_name('title').text
        assert title == 'PRODUCTS'

    @pytest.mark.skip(reason="element does not exist")
    def test_fake_element(self):
        email = self.driver.find_element_by_class_name('email')
        email.send_keys('jw@gmail.com')
        email.submit()
        title = self.driver.find_element_by_class_name('title').text
        assert title == 'Products'

    def test_valid_login_with_spaces(self):
        self.login('            ' + good_user, all_passwords)
        error_msg = 'Epic sadface: Username and password do not match any user in this service'
        error_div = self.driver.find_element_by_class_name('error-message-container')
        assert error_div.text == error_msg

    def test_wrong_username(self):
        self.login('foo' , all_passwords)
        error_msg = 'Epic sadface: Username and password do not match any user in this service'
        error_div = self.driver.find_element_by_class_name('error-message-container')
        assert error_div.text == error_msg

    def test_wrong_password(self):
        self.login(good_user , 'wrong_password')
        error_msg = 'Epic sadface: Username and password do not match any user in this service'
        error_div = self.driver.find_element_by_class_name('error-message-container')
        assert error_div.text == error_msg
        
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