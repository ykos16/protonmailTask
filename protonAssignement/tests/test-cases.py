import unittest
from pages.loginPage import LoginPageInfo
from pages.labelFolderPage import labelFolder_Page
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

CHROME_DRIVER_PATH = 'C:/test files/chromedriver'

class ProtonTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        cls.driver.get("https://beta.protonmail.com/")
        login = LoginPageInfo(cls.driver)
        login.enter_username('veryspecialaccount')
        login.enter_password('verynicepassword')
        login.click_Login()
        time.sleep(6)
        cls.driver.get('https://beta.protonmail.com/settings/labels')
        time.sleep(1.5)


    def test_Create(self):
        testPage = labelFolder_Page(self.driver)
        time.sleep(2)
        testPage.create_folder()
        testPage.name_field('demoFolder')
        time.sleep(1)
        testPage.submit_action()
        time.sleep(1)
        testPage.create_label()
        testPage.name_field('demoLabel')
        time.sleep(1)
        testPage.submit_action()
        time.sleep(1)

    def test_Modify(self):
        testPage = labelFolder_Page(self.driver)
        testPage.edit_button()
        time.sleep(1)
        testPage.submit_action()
        time.sleep(0.5)

    def test_Sorting(self):
        driver = self.driver
        folder_sort = driver.find_element_by_xpath('//tr[1]//td[1]//span[1]')
        label_sort = driver.find_element_by_xpath('//tr[2]//td[1]//span[1]')
        time.sleep(1)
        ActionChains(self.driver).drag_and_drop(label_sort, folder_sort).perform()
        time.sleep(1)

    def test_delete_Items(self):
        testPage = labelFolder_Page(self.driver)
        time.sleep(1)
        testPage.item_dropdown()
        time.sleep(0.5)
        testPage.delete_items()
        time.sleep(1)
        testPage.confirm_delete()
        time.sleep(2)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()