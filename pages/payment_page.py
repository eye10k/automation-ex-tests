from pages.BasePage import BasePage
import allure
from utilities import configReader
import logging
import allure
from utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)

class payment(BasePage):
    def __init__(self, page):
        super().__init__(page)


    def payment(self):
        with allure.step("filling payment details"):
            self.click("payment_name_on_card_XPATH")
            self.type("payment_name_on_card_XPATH", "serg test")
            self.click("payment_number_on_card_XPATH")
            self.type("payment_number_on_card_XPATH", "1234567890")
            self.click("payment_expire_month_XPATH")
            self.type("payment_expire_month_XPATH", "12")
            self.click("payment_expire_year_XPATH")
            self.type("payment_expire_year_XPATH", "2023")
            self.click("payment_cvc_on_card_XPATH")
            self.type("payment_cvc_on_card_XPATH", "123")
            self.click("payment_pay_button_XPATH")
            log.logger.info("Clicked on payment button")