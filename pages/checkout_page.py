from pages.BasePage import BasePage

class SignupPage(BasePage):
    def register_user(self, user_data):
        self.click("title_XPATH")
        self.type("sign_name_XPATH", user_data["name"])
        self.type("sign_email_XPATH", user_data["email"])
        self.type("sign_password_XPATH", user_data["password"])
        self.page.locator("sing_day_XPATH").select_option(user_data["day"])
        self.page.locator("sing_month_XPATH").select_option(user_data["month"])
        self.page.locator("sing_year_XPATH").select_option(user_data["year"])
        self.page.locator("sign_checkbox_XPATH").check()
        self.page.locator("sign_checkbox2_XPATH").check()
        self.type("first_name_XPATH", user_data["first_name"])
        self.type("last_name_XPATH", user_data["last_name"])
        self.type("company_XPATH", user_data["company"])
        self.type("address_XPATH", user_data["address"])
        self.type("address2_XPATH", user_data["address2"])
        self.page.locator("country_XPATH").select_option(user_data["country"])
        self.type("state_XPATH", user_data["state"])
        self.type("city_XPATH", user_data["city"])
        self.type("zipcode_XPATH", user_data["zipcode"])
        self.type("mobile_XPATH", user_data["mobile"])
        self.click("create_account_XPATH")

    def is_account_created(self):
        return self.page.locator("//b[normalize-space()='Account Created!']").is_visible()
