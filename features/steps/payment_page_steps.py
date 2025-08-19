from behave import *
import allure
from utilities.user_utility import generate_payment_card
from pages.payment_page import PaymentPage

@when("I provide my payment details")
def step_provide_payment_details(context):
    with allure.step("I provide my payment details"):
        context.payment_page = PaymentPage(context.page)
        context.payment_card = generate_payment_card()
        context.payment_page.fill_payment_form(context.payment_card)