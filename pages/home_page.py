from pages.BasePage import BasePage
from utilities import configReader

class HomePage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def navigate_to_home(self):
        self.page.goto(configReader.readConfig("basic info", "testsiteurl"))
        self.accept_cookies()

    def accept_cookies(self):
        self.page.locator(".fc-dialog .fc-footer-buttons .fc-cta-consent").click()

    def add_product_to_cart(self):
        self.move_to("product_XPATH")
        self.click("product_XPATH")  # Добавление первого продукта


    def go_to_cart(self):
        self.click("cart_XPATH")

    def verify_home_page_loaded(self):
        assert self.is_visible("home_menu_XPATH"), "'Home' menu is not visible"
        style = self.get_attribute("home_menu_XPATH","style")
        assert style and "color: orange;" in style, "'Home' menu is not selected"


    def click_cart_button(self):
        self.click("cart_button_XPATH")