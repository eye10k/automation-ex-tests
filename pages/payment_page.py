from pages.base_page import BasePage
import logging
import allure
import json
from utilities.log_util import Logger

log = Logger(__name__, logging.INFO)

class PaymentPage(BasePage):
    field_name_on_card_CSS = '[data-qa="name-on-card"]'
    field_number_on_card_CSS = '[data-qa="card-number"]'
    field_expire_month_CSS = '[data-qa="expiry-month"]'
    field_expire_year_CSS = '[data-qa="expiry-year"]'
    field_cvc_on_card_CSS = '[data-qa="cvc"]'
    pay_confirm_btn_CSS = '[data-qa="pay-button"]'

    def __init__(self, page):
        super().__init__(page)

    def fill_payment_form(self, PaymentCard):
        with allure.step("filling payment details"):
            payment_card_dict = PaymentCard.__dict__
            allure.attach(json.dumps(payment_card_dict, indent=2), name="Payment Card Details",
                          attachment_type=allure.attachment_type.JSON)
            self.type(self.field_name_on_card_CSS, PaymentCard.holder_name)
            self.click(self.field_number_on_card_CSS)
            self.type(self.field_number_on_card_CSS, PaymentCard.card_number)
            self.click(self.field_expire_month_CSS)
            self.type(self.field_expire_month_CSS, PaymentCard.expire_month)
            self.click(self.field_expire_year_CSS)
            self.type(self.field_expire_year_CSS, PaymentCard.expire_year)
            self.click(self.field_cvc_on_card_CSS)
            self.type(self.field_cvc_on_card_CSS, PaymentCard.cvc)
            self.click(self.pay_confirm_btn_CSS)
            log.logger.info("Clicked on payment button")