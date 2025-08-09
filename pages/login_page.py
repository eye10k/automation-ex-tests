from pages.base_page import BasePage

class LoginPage(BasePage):
    name_field_CSS = '[data-qa="signup-name"]'
    email_field_CSS = '[data-qa="signup-email"]'
    signup_btn_CSS = '[data-qa="signup-button"]'

    def __init__(self, page):
        super().__init__(page)

    def fill_name(self, name):
        self.type(self.name_field_CSS, name)

    def fill_email(self, email):
        self.type(self.email_field_CSS, email)

    def click_Signup(self):
        self.click(self.signup_btn_CSS)

