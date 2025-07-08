from pages.BasePage import BasePage
import allure
from utilities import configReader

class checkout(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def verify_checkout_page(self,User):
        with allure.step("Verify checkout page"):
            assert self.get_text("checkout_fullname_XPATH") == f"Mr. {User.first_name} {User.last_name}"
            assert self.get_text("checkout_phone_XPATH") == f"{User.mobile}"

    def fill_checkout_details(self, User):
        self.click("checkout_message_XPATH")
        self.page.locator(configReader.readConfig("locator", "checkout_message_XPATH")).type("Hello WORLD!")


    def place_order(self):
        self.click("checkout_place_order_XPATH")