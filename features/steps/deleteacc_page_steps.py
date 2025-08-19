from behave import *
import allure
from pages.deleteacc_page import DeleteAccPage

@then("I should see the message \"{message_text}\"")
def step_verify_account_deleted(context, message_text):
    with allure.step(f"I should see the message '{message_text}'"):
        context.delete_acc = DeleteAccPage(context.page)
        context.delete_acc.check_delete_message(message_text)

@then("I finish by clicking Continue")
def step_final_continue(context):
    with allure.step("I finish by clicking Continue"):
        context.delete_acc.click_continue()