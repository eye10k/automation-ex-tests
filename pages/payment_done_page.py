from pages.base_page import BasePage

class PaymentDonePage(BasePage):
    order_confirmed_msg_XPATH = "//p[text()='Congratulations! Your order has been confirmed!']"
    delete_account_btn_CSS = 'a[href="/delete_account"]'

    def __init__(self, page):
        super().__init__(page)

    def payment_done_message(self):
        assert self.get_text(self.order_confirmed_msg_XPATH) == "Congratulations! Your order has been confirmed!"

    def delete_acc(self):
        self.click(self.delete_account_btn_CSS)
