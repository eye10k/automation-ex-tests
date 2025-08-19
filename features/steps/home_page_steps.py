from behave import *
import allure
from pages.home_page import HomePage

@given("I navigate to the home page")
def step_navigate_to_home(context):
    with allure.step("I navigate to the home page"):
        context.home_page = HomePage(context.page)
        context.home_page.navigate_to_home()
        context.home_page.verify_home_page_loaded()

@when("I add products to my cart")
def step_add_products_to_cart(context):
    with allure.step("I add products to my cart"):
        context.home_page.add_product_to_cart()

@when("I go to my cart")
def step_click_cart_button(context):
    with allure.step("I go to my cart"):
        context.home_page.go_to_cart()

@when("I go back to my cart")
def step_click_cart_again(context):
    with allure.step("I go back to my cart"):
        context.home_page.click_cart_button()