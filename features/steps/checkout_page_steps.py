from behave import *
import allure
from pages.checkout_page import CheckoutPage

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