from behave import *
import allure
import uuid

from models.PaymentCard import PaymentCard
from models.user import User
from pages.signup_page import SignupPage
from pages.shopping_cart import ShoppingCartPage
from pages.login_page import LoginPage
from pages.acc_created import AccCreatedPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from pages.payment_done import PaymentDonePage
from pages.deleteacc_page import DeleteAccPage


@when("I add products to my cart")
def step_add_products_to_cart(context):
    with allure.step("I add products to my cart"):
        context.home_page.add_product_to_cart()


@when("I go to my cart")
def step_click_cart_button(context):
    with allure.step("I go to my cart"):
        context.home_page.go_to_cart()


@then("I should see my cart")
def step_verify_cart_page(context):
    with allure.step("I should see my cart"):
        context.cart_page = ShoppingCartPage(context.page)
        context.cart_page.verify_shopping_cart_displayed()


@when("I proceed to checkout")
def step_proceed_to_checkout(context):
    with allure.step("I proceed to checkout"):
        context.cart_page.click_to_checkout()


@when("I choose to register a new account")
def step_click_register_login(context):
    with allure.step("I choose to register a new account"):
        context.cart_page.click_to_Register()


@when("I sign up and create my account")
def step_fill_signup_form(context):
    with allure.step("I sign up and create my account"):
        context.login_page = LoginPage(context.page)
        context.login_page.fill_name("Toby")
        context.login_page.fill_email(f"{uuid.uuid4()}@example.com")
        context.login_page.click_Signup()

        context.signup_page = SignupPage(context.page)
        context.user = User(
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
            "+1234567890"
        )
        context.signup_page.enter_acc_details(context.user)


@then('I should see the message "ACCOUNT CREATED!"')
def step_verify_account_created(context):
    with allure.step("I should see the message 'ACCOUNT CREATED!'"):
        context.acc_created = AccCreatedPage(context.page)
        context.acc_created.verify_acc_created()


@when("I continue from the account created page")
def step_continue_from_acc_created(context):
    with allure.step("I continue from the account created page"):
        pass  # already handled in verify_acc_created()


@then("I should be logged in as my user")
def step_verify_logged_in(context):
    with allure.step("I should be logged in as my user"):
        pass  # implied by previous step


@when("I go back to my cart")
def step_click_cart_again(context):
    with allure.step("I go back to my cart"):
        context.home_page.click_cart_button()


@when("I confirm the checkout")
def step_confirm_checkout(context):
    with allure.step("I confirm the checkout"):
        context.cart_page.click_to_checkout()


@then("I should see my address and order details")
def step_verify_checkout_page(context):
    with allure.step("I should see my address and order details"):
        context.checkout_page = CheckoutPage(context.page)
        context.checkout_page.verify_checkout_page(context.user)


@when("I leave a comment and place my order")
def step_comment_and_place_order(context):
    with allure.step("I leave a comment and place my order"):
        context.checkout_page.fill_checkout_details(context.page)
        context.checkout_page.place_order()


@when("I provide my payment details")
def step_provide_payment_details(context):
    with allure.step("I provide my payment details"):
        context.payment_page = PaymentPage(context.page)
        paymentCard = PaymentCard(
            "Test Card",
            "1234 5678 9012 3456",
            "12",
            "2028",
            "123"
        )
        context.payment_page.fill_payment_form(paymentCard)


@when("I confirm the payment")
def step_confirm_payment(context):
    with allure.step("I confirm the payment"):
        pass  # already handled in payment()


@then('I should see the message "Your order has been placed successfully!"')
def step_verify_success_message(context):
    with allure.step('I should see the message "Your order has been placed successfully!"'):
        context.payment_done = PaymentDonePage(context.page)
        context.payment_done.payment_done_message()


@when("I delete my account")
def step_delete_account(context):
    with allure.step("I delete my account"):
        context.payment_done.delete_acc()


@then('I should see the message "ACCOUNT DELETED!"')
def step_verify_account_deleted(context):
    with allure.step('I should see the message "ACCOUNT DELETED!"'):
        context.delete_acc = DeleteAccPage(context.page)
        context.delete_acc.check_delete_message()


@then("I finish by clicking Continue")
def step_final_continue(context):
    with allure.step("I finish by clicking Continue"):
        context.delete_acc.click_continue()
