from pages.base_page import BasePage

class PaymentDonePage(BasePage):
    order_confirmed_msg_XPATH = "//p[text()='Congratulations! Your order has been confirmed!']"
    delete_account_btn_CSS = 'a[href="/delete_account"]'

    def __init__(self, page):
        super().__init__(page)

    def payment_done_message(self, expected_message):
        actual_message = self.get_text(self.order_confirmed_msg_XPATH)
        assert actual_message == expected_message, f"Expected: {expected_message}, but got: {actual_message}"

    def delete_acc(self):
        self.click(self.delete_account_btn_CSS)