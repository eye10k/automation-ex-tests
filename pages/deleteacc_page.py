from pages.base_page import BasePage

class DeleteAccPage(BasePage):
    delete_account_msg_CSS = '[data-qa="account-deleted"]'
    continue_btn_CSS = '[data-qa="continue-button"]'

    def __init__(self, page):
        super().__init__(page)

    def check_delete_message(self):
        self.move_to(self.delete_account_msg_CSS)
        assert self.get_text(self.delete_account_msg_CSS) == "Account Deleted!"

    def click_continue(self):
        self.click(self.continue_btn_CSS)
