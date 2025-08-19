from behave import *
import allure
from pages.shopping_cart_page import ShoppingCartPage

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

@when("I confirm the checkout")
def step_confirm_checkout(context):
    with allure.step("I confirm the checkout"):
        context.cart_page.click_to_checkout()