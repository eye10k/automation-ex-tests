from tabnanny import check

import pytest
import allure
import uuid
from Models.User import User
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.Shopping_Cart import ShoppingCart
from pages.login_page import Login_Page
from pages.acc_created import AccCreated
from pages.checkout_page import checkout
from pages.payment_page import payment
from pages.payment_done import PaymentDone
from pages.deleteacc_page import DeleteAcc
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

            cart_page = ShoppingCart(page)
            cart_page.verify_shopping_cart_displayed()
            cart_page.click_to_checkout()
            cart_page.click_to_Register()

            login_page = Login_Page(page)
            login_page.fill_name("Toby")
            login_page.fill_email(f"{uuid.uuid4()}@example.com")
            login_page.click_Signup()

            singup_page = SignupPage(page)
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
            singup_page.enter_acc_details(user)


            acc_created = AccCreated(page)
            acc_created.verify_acc_created()

            home_page.click_cart_button()
            cart_page.click_to_checkout()

            checkout_page = checkout(page)
            checkout_page.verify_checkout_page(user)
            checkout_page.fill_checkout_details(page)
            checkout_page.place_order()

            payment_page = payment(page)
            payment_page.payment()


            payment_done = PaymentDone(page)
            payment_done.payment_done_message()
            payment_done.delete_acc()


            delete_acc = DeleteAcc(page)
            delete_acc.check_delete_message()
            delete_acc.click_continue()



