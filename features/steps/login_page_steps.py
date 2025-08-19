from behave import *
import allure
import uuid
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from utilities.user_utility import generate_user
from faker import Faker
fake = Faker()

@when("I sign up and create my account")
def step_fill_signup_form(context):
    with allure.step("I sign up and create my account"):
        context.login_page = LoginPage(context.page)
        context.login_page.fill_name(fake.name())
        context.login_page.fill_email(f"{uuid.uuid4()}@example.com")
        context.login_page.click_Signup()

        context.signup_page = SignupPage(context.page)
        context.user = generate_user(for_ui=True)
        context.signup_page.enter_acc_details(context.user)