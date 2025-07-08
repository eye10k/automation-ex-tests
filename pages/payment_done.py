from pages.BasePage import BasePage
from utilities import configReader

class PaymentDone(BasePage):
    def __init__(self, page):
        super().__init__(page)


    def payment_done_message(self):
        assert self.get_text("payment_done_title_XPATH") == "Congratulations! Your order has been confirmed!"

    def delete_acc(self):
        self.click("delete_account_XPATH")