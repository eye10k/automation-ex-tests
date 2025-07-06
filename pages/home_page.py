from pages.BasePage import BasePage
from utilities import configReader

class HomePage(BasePage):
    def navigate_to_home(self):
        self.page.goto(configReader.readConfig("basic info", "testsiteurl"))

    def add_product_to_cart(self):
        self.click("product_XPATH")  # Добавление первого продукта


    def go_to_cart(self):
        self.click("cart_XPATH")