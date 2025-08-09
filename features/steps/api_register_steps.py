from behave import *
import requests
import uuid
import json
import allure
from utilities.user_utility import generate_user_data

@given("I am a new visitor without an account")
def step_impl(context):
    context.email = f"testuser_{uuid.uuid4()}@example.com"
    allure.attach(context.email, name="Generated Email", attachment_type=allure.attachment_type.TEXT)

@when("I register with valid personal and contact details")
def step_impl(context):
    url = "https://automationexercise.com/api/createAccount"
    payload = generate_user_data(context.email)

    context.response = requests.post(url, data=payload)
    allure.attach(url, name="Create Account URL", attachment_type=allure.attachment_type.TEXT)
    allure.attach(json.dumps(payload, indent=2), name="Request Payload", attachment_type=allure.attachment_type.JSON)
    allure.attach(context.response.text, name="Response Body", attachment_type=allure.attachment_type.TEXT)

@then("my account should be successfully registered")
def step_impl(context):
    assert context.response.status_code == 200, "Expected HTTP 200"
    json_data = context.response.json()
    assert json_data["responseCode"] == 201, "Expected responseCode 201"
    assert json_data["message"] == "User created!", "Expected message 'User created!'"

@then("I should be able to retrieve my account details by email")
def step_impl(context):
    url = f"https://automationexercise.com/api/getUserDetailByEmail?email={context.email}"
    get_response = requests.get(url)
    get_data = get_response.json()

    allure.attach(url, name="Get User Detail URL", attachment_type=allure.attachment_type.TEXT)
    allure.attach(get_data["user"]["email"], name="Fetched Email", attachment_type=allure.attachment_type.TEXT)

    assert "user" in get_data, "Expected user object in response"
    assert get_data["user"]["email"] == context.email, "Returned email does not match"
