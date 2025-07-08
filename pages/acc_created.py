from pages.BasePage import BasePage
import allure
from utilities import configReader


class AccCreated(BasePage):
    def __init__(self, page):
        super().__init__(page)


    def verify_acc_created(self):
        account_created_message = "acc_created_XPATH"
        self.is_visible(account_created_message)
        self.click("continue_XPATH")