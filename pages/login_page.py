from pages.BasePage import BasePage
import allure
from utilities import configReader

class Login_Page(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def fill_name(self, name):
        self.type("name_XPATH", name)

    def fill_email(self, email):
        self.type("email_signup_XPATH", email)

    def click_Signup(self):
        self.click("signup_XPATH")
