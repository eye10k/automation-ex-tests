from pages.base_page import BasePage
import time

class SignupPage(BasePage):
        title_radio_CSS = '#id_gender1'
        first_name_field_CSS = '[data-qa="first_name"]'
        password_field_CSS = '[data-qa="password"]'
        dropdown_day_CSS = '[data-qa="days"]'
        dropdown_month_CSS = '[data-qa="months"]'
        dropdown_year_CSS = '[data-qa="years"]'
        last_name_CSS = '[data-qa="last_name"]'
        company_field_CSS = '[data-qa="company"]'
        address_field_CSS = '[data-qa="address"]'
        address2_field_CSS = '[data-qa="address2"]'
        country_dropdown_CSS = '[data-qa="country"]'
        state_field_CSS = '[data-qa="state"]'
        city_field_CSS = '[data-qa="city"]'
        zipcode_field_CSS = '[data-qa="zipcode"]'
        mobile_field_CSS = '[data-qa="mobile_number"]'
        create_account_btn_CSS = '[data-qa="create-account"]'

        def __init__(self, page):
            super().__init__(page)

        def enter_acc_details(self, User):
            self.click(self.title_radio_CSS)
            self.type(self.first_name_field_CSS, User.first_name)
            self.type(self.last_name_CSS, User.last_name)
            self.type(self.password_field_CSS, User.password)
            self.select(self.dropdown_day_CSS, User.birth_day)
            self.select(self.dropdown_month_CSS, User.birth_month)
            self.select(self.dropdown_year_CSS, User.birth_year)
            self.type(self.company_field_CSS, User.company)
            self.type(self.address_field_CSS, User.address)
            self.type(self.address2_field_CSS, User.address2)
            self.select(self.country_dropdown_CSS, User.country)
            self.type(self.state_field_CSS, User.state)
            self.type(self.city_field_CSS, User.city)
            self.type(self.zipcode_field_CSS, User.zipcode)
            self.type(self.mobile_field_CSS, User.mobile)
            self.click(self.create_account_btn_CSS)
            time.sleep(5)



    #
    # def is_account_created(self):
    #     return self.page.locator("//b[normalize-space()='Account Created!']").is_visible()
