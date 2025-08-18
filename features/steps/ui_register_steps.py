from behave import *
import allure
import uuid

from utilities.user_utility import generate_user, generate_user_data, generate_payment_card
from pages.signup_page import SignupPage
from pages.shopping_cart_page import ShoppingCartPage
from pages.login_page import LoginPage
from pages.acc_created_page import AccCreatedPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from pages.payment_done_page import PaymentDonePage
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
        context.user = generate_user(for_ui=True)
        context.signup_page.enter_acc_details(context.user)

@then("I should see the message \"ACCOUNT CREATED!\" and I am logged in")
def step_verify_account_created(context):
    with allure.step("I should see the message 'ACCOUNT CREATED!' and I am logged in"):
        context.acc_created = AccCreatedPage(context.page)
        context.acc_created.verify_acc_created()

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
        context.payment_card = generate_payment_card()
        context.payment_page.fill_payment_form(context.payment_card)

@then("I should see the message \"Your order has been placed successfully!\"")
def step_verify_success_message(context):
    with allure.step("I should see the message 'Your order has been placed successfully!'"):
        context.payment_done = PaymentDonePage(context.page)
        context.payment_done.payment_done_message()

@when("I delete my account")
def step_delete_account(context):
    with allure.step("I delete my account"):
        context.payment_done.delete_acc()

@then("I should see the message \"ACCOUNT DELETED!\"")
def step_verify_account_deleted(context):
    with allure.step("I should see the message 'ACCOUNT DELETED!'"):
        context.delete_acc = DeleteAccPage(context.page)
        context.delete_acc.check_delete_message()

@then("I finish by clicking Continue")
def step_final_continue(context):
    with allure.step("I finish by clicking Continue"):
        context.delete_acc.click_continue()
