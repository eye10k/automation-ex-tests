from tabnanny import check

import pytest
import allure
import uuid
from models.user import User
from models.payment_card import PaymentCard
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.shopping_cart_page import ShoppingCartPage
from pages.login_page import LoginPage
from pages.acc_created_page import AccCreatedPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from pages.payment_done_page import PaymentDonePage
from pages.deleteacc_page import DeleteAccPage
from tests.BaseTest import BaseTest

@allure.feature("Add product to cart")
@allure.severity(allure.severity_level.NORMAL)
class TestAddToCart(BaseTest):

    def test_register_while_checkout(self, page):
        with allure.step("register_while_checkout"):
            home_page = HomePage(page)
            home_page.navigate_to_home()
            home_page.verify_home_page_loaded()

            home_page.add_product_to_cart()
            home_page.go_to_cart()

            cart_page = ShoppingCartPage(page)
            cart_page.verify_shopping_cart_displayed()
            cart_page.click_to_checkout()
            cart_page.click_to_Register()

            login_page = LoginPage(page)
            login_page.fill_name("Toby")
            login_page.fill_email(f"{uuid.uuid4()}@example.com")
            login_page.click_Signup()

            signup_page = SignupPage(page)
            user = User(
                "Toby",
                "Styd",
                "automation123!",
                "1",
                "1",
                "1990",
                "Test ARLOYS",
                "123 Rodeo Drive",
                "122 Rodeo Drive1",
                "United States",
                "California",
                "San Francisco",
                "12345",
                "+1234567890")
            signup_page.enter_acc_details(user)

            acc_created = AccCreatedPage(page)
            acc_created.verify_acc_created()

            home_page.click_cart_button()
            cart_page.click_to_checkout()

            checkout_page = CheckoutPage(page)
            checkout_page.verify_checkout_page(user)
            checkout_page.fill_checkout_details(page)
            checkout_page.place_order()

            payment_page = PaymentPage(page)
            card = PaymentCard(
                "Test Card",
                "4242424242424242",
                "12",
                "2028",
                "123"
            )
            payment_page.fill_payment_form(card)

            payment_done = PaymentDonePage(page)
            payment_done.payment_done_message()
            payment_done.delete_acc()

            delete_acc = DeleteAccPage(page)
            delete_acc.check_delete_message()
            delete_acc.click_continue()



