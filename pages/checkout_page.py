from pages.base_page import BasePage
import allure

class CheckoutPage(BasePage):
    item_box_fullname_CSS = '#address_delivery li.address_firstname.address_lastname'
    item_box_phone_CSS = '#address_delivery li.address_phone'
    message_area_CSS = 'textarea[name="message"]'
    place_order_btn_XPATH = '//a[normalize-space()="Place Order"]'

    def __init__(self, page):
        super().__init__(page)

    def verify_checkout_page(self, User):
        with allure.step("Verify checkout page"):
            assert self.get_text(self.item_box_fullname_CSS) == f"Mr. {User.first_name} {User.last_name}"
            assert self.get_text(self.item_box_phone_CSS) == f"{User.mobile}"

    def fill_checkout_details(self, User):
        self.click(self.message_area_CSS)
        self.page.locator(self.message_area_CSS).type("Hello WORLD!")  # Уже не нужен configReader

    def place_order(self):
        self.click(self.place_order_btn_XPATH)
