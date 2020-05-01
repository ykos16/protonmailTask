import unittest
from Pages.LoginPage import LoginPageInfo
from Pages.labelFolderPage import labelFolder_Page
from selenium import webdriver
import time

CHROME_DRIVER_PATH = 'C:/test files/chromedriver'

class ProtonTest(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.driver.get("https://beta.protonmail.com/")
        login = LoginPageInfo(self.driver)
        login.enter_username('veryspecialaccount')
        login.enter_password('verynicepassword')
        login.click_Login()
        time.sleep(6)
        self.driver.get('https://beta.protonmail.com/settings/labels')
        time.sleep(1.5)


    def test_delete_Items(self):
        testPage = labelFolder_Page(self.driver)
        time.sleep(1)
        testPage.item_dropdown()
        time.sleep(0.5)
        testPage.delete_items()
        time.sleep(1)
        testPage.confirm_delete()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()