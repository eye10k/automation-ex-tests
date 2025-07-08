from pages.BasePage import BasePage
import time

class SignupPage(BasePage):
        def __init__(self, page):
            super().__init__(page)

        def enter_acc_details(self, User):
            self.click("title_XPATH")
            self.type("first_name_XPATH", User.first_name)
            self.type("sign_password_XPATH", User.password)
            self.select("sing_day_XPATH", User.birth_day)
            self.select("sing_month_XPATH", User.birth_month)
            self.select("sing_year_XPATH", User.birth_year)
            self.type("first_name_XPATH", User.first_name)
            self.type("last_name_XPATH", User.last_name)
            self.type("company_XPATH", User.company)
            self.type("address_XPATH", User.address)
            self.type("address2_XPATH", User.address2)
            self.select("country_XPATH", User.country)
            self.type("state_XPATH", User.state)
            self.type("city_XPATH", User.city)
            self.type("zipcode_XPATH", User.zipcode)
            self.type("mobile_XPATH", User.mobile)
            self.click("create_account_XPATH")
            time.sleep(5)



    #
    # def is_account_created(self):
    #     return self.page.locator("//b[normalize-space()='Account Created!']").is_visible()
