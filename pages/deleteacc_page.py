from pages.BasePage import BasePage

class DeleteAcc(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def check_delete_message(self):
        self.move_to("delete_acc_message_XPATH")
        assert self.get_text("delete_acc_message_XPATH") == "Your account has been permanently deleted!"

    def click_continue(self):
        self.click("cont_delete_XPATH")