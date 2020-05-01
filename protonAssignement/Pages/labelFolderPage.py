class labelFolder_Page(object):

 def __init__(self, driver):
        self.driver = driver
        self.add_folder_button = '[data-test-id="folders/labels:addFolder"]'
        self.add_label_button = '[data-test-id="folders/labels:addLabel"]'
        self.item_name_field = 'accountName'
        self.edit_btn = '[data-test-id="folders/labels:item-edit"]'
        self.folder_sort = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div/main/div/section/table/tbody/tr[1]/td[1]/span')
        self.label_sort = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div/main/div/section/table/tbody/tr[2]/td[1]/span')
        self.dropdown = '[data-test-id="dropdown:open"]'
        self.item_delete = '[data-test-id="folders/labels:item-delete"]'
        self.item_delete_confirm = '/html/body/div[11]/dialog/form/footer/button[2]'
        self.submit_button = '/html/body/div[9]/dialog/form/footer/button[2]'

 def create_folder(self):
    self.driver.find_element_by_css_selector(self.add_folder_button).click()

 def create_label(self):
    self.driver.find_element_by_css_selector(self.add_label_button).click()

 def name_field(self, name):
    self.driver.find_element_by_id(self.item_name_field).send_keys(name)

 def edit_button(self):
    self.driver.find_element_by_css_selector(self.edit_btn).click()

 def submit_action(self):
    self.driver.find_element_by_id(self.item_name_field).submit()

 def item_dropdown(self):
    self.driver.find_element_by_css_selector(self.dropdown).click()

 def delete_items(self):
    self.driver.find_element_by_css_selector(self.item_delete).click()

 def confirm_delete(self):
    self.driver.find_element_by_xpath(self.item_delete_confirm).click()


