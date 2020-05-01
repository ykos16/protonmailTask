class LoginPageInfo(object):

 def __init__(self, driver):
    self.driver = driver

    #self.chrome
    self.username_textbox_id = 'username'
    self.password_textbox_name = 'password'
    self.login_button_id = 'login_btn'

 def enter_username(self, username):
    self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

 def enter_password(self, password):
    self.driver.find_element_by_name(self.password_textbox_name).send_keys(password)

 def click_Login(self):
    self.driver.find_element_by_id(self.login_button_id).click()



