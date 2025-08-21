from pages.base_page import BasePage

class AccCreatedPage(BasePage):
    acc_created_msg_CSS = '[data-qa="account-created"]'
    continue_btn_CSS = '[data-qa="continue-button"]'

    def __init__(self, page):
        super().__init__(page)

    def verify_acc_created(self):
        assert self.is_visible(self.acc_created_msg_CSS), "Account created message not visible"
        self.click(self.continue_btn_CSS)