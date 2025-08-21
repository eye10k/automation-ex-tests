from behave import *
import allure
from pages.payment_done_page import PaymentDonePage

@then('I should see success message "{message_text}"')
def step_verify_success_message(context, message_text):
    with allure.step(f"I should see success message '{message_text}'"):
        context.payment_done = PaymentDonePage(context.page)
        context.payment_done.verify_payment_done_message(message_text)

@when("I delete my account")
def step_delete_account(context):
    with allure.step("I delete my account"):
        context.payment_done.delete_acc()