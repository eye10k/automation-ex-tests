from behave import given, when, then
import requests
import uuid
import json
import allure

@given("I am a new visitor without an account")
def step_impl(context):
    context.email = f"testuser_{uuid.uuid4()}@example.com"
    allure.attach(context.email, name="Generated Email", attachment_type=allure.attachment_type.TEXT)

@when("I register with valid personal and contact details")
def step_impl(context):
    payload = {
        "name": "Styd",
        "email": context.email,
        "password": "automation123!",
        "title": "Mr",
        "birth_date": "01",
        "birth_month": "01",
        "birth_year": "1990",
        "firstname": "Test",
        "lastname": "User",
        "company": "Test ARLOYS",
        "address1": "123 Rodeo Drive",
        "address2": "",
        "country": "United States",
        "zipcode": "12345",
        "state": "California",
        "city": "San Francisco",
        "mobile_number": "+1234567890"
    }
    context.response = requests.post("https://automationexercise.com/api/createAccount", data=payload)

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
    assert "user" in get_data, "Expected user object in response"
    assert get_data["user"]["email"] == context.email, "Returned email does not match"
    allure.attach(get_data["user"]["email"], name="Fetched Email", attachment_type=allure.attachment_type.TEXT)
