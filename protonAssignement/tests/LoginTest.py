import unittest

from Pages.LoginPage import LoginPageInfo
from selenium import webdriver

class IDEScript(unittest.TestCase):



    def test_login_page(self):
        self.driver = webdriver.Chrome('C:/test files/chromedriver')
        driver = self.driver
        driver.get('https://beta.protonmail.com/')
        login = LoginPageInfo(driver)
        login.enter_username('veryspecialproject')
        login.enter_password('verynicepassword')
        login.click_Login()
        driver.get('https://beta.protonmail.com/settings/labels')












