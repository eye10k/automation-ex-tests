from pages.base_page import BasePage
import allure

class ShoppingCartPage(BasePage):
    shoppingcart_title_CSS = 'li.active'
    proceed_btn_CSS = '.btn.check_out'
    register_popup_link_CSS = '.text-center a[href="/login"]'

    def __init__(self, page):
        super().__init__(page)

    def verify_shopping_cart_displayed(self):
        with allure.step("Verify that cart page is displayed"):
            cart_title_visible = self.is_visible(self.shoppingcart_title_CSS)
            assert cart_title_visible, "Cart page title is not visible"

    def click_to_checkout(self):
        self.click(self.proceed_btn_CSS)

    def click_to_Register(self):
        self.click(self.register_popup_link_CSS)
