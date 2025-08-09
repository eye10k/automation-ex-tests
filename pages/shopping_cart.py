from pages.BasePage import BasePage
import allure
from utilities import configReader

class ShoppingCart(BasePage):
    def __init__(self, page):
        super().__init__(page)


    def verify_shopping_cart_displayed(self):
        with allure.step("Verify that cart page is displayed"):
            cart_title_visible = self.is_visible("cart_title_XPATH")
            assert cart_title_visible, "Cart page title is not visible"

    def click_to_checkout(self):
        self.click("proceed_XPATH")

    def click_to_Register(self):
        self.click("register_XPATH")