from pages.base_page import BasePage

class HomePage(BasePage):
    home_navigation_menu_CSS = '.navbar-nav a[href="/"]'
    product_cart_CSS = 'div.col-sm-4:nth-of-type(2) div.productinfo a[data-product-id="2"]'
    view_cart_popup_CSS = '.text-center a[href="/view_cart"]'
    cart_button_CSS = '#header .shop-menu a:has(i.fa-shopping-cart)'

    def __init__(self, page):
        super().__init__(page)

    def navigate_to_home(self):
        self.open("")
        self.accept_cookies()

    def accept_cookies(self):
        self.page.locator(".fc-dialog .fc-footer-buttons .fc-cta-consent").click()

    def add_product_to_cart(self):
        self.move_to(self.product_cart_CSS)
        self.click(self.product_cart_CSS)

    def go_to_cart(self):
        self.click(self.view_cart_popup_CSS)

    def verify_home_page_loaded(self):
        assert self.is_visible(self.home_navigation_menu_CSS), "'Home' menu is not visible"
        style = self.get_attribute(self.home_navigation_menu_CSS, "style")
        assert style and "color: orange;" in style, "'Home' menu is not selected"

    def click_cart_button(self):
        self.click(self.cart_button_CSS)