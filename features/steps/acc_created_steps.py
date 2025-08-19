from behave import *
import allure
from pages.acc_created_page import AccCreatedPage

@then("I should see the message \"ACCOUNT CREATED!\" and I am logged in")
def step_verify_account_created(context):
    with allure.step("I should see the message 'ACCOUNT CREATED!' and I am logged in"):
        context.acc_created = AccCreatedPage(context.page)
        context.acc_created.verify_acc_created()