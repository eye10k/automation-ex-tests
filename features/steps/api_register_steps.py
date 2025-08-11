from behave import *
import uuid
import allure
from API.api_client import ApiClient
from utilities.user_utility import generate_user_data


@given("I am a new visitor without an account")
def step_impl(context):
    context.email = f"testuser_{uuid.uuid4()}@example.com"
    allure.attach(context.email, name="Generated Email", attachment_type=allure.attachment_type.TEXT)


@when("I register with valid personal and contact details")
def step_impl(context):
    client = ApiClient(base_url="https://automationexercise.com/api")
    payload = generate_user_data(context.email)


    context.response = client.send_post_request(
        endpoint="/createAccount",
        payload=payload,
        use_json=False
    )


@then("my account should be successfully registered")
def step_impl(context):
    with allure.step("Verify account registration"):
        assert context.response.status_code == 200, "Expected HTTP 200"
        json_data = context.response.json()
        assert json_data["responseCode"] == 201, "Expected responseCode 201"
        assert json_data["message"] == "User created!", "Expected message 'User created!'"


@then("I should be able to retrieve my account details by email")
def step_impl(context):
    with allure.step("Retrieve account details by email"):
        client = ApiClient(base_url="https://automationexercise.com/api")
        params = {"email": context.email}

        get_response = client.send_get_request(
            endpoint="/getUserDetailByEmail",
            params=params
        )

        get_data = get_response.json()

        allure.attach(
            get_data["user"]["email"],
            name="Fetched Email",
            attachment_type=allure.attachment_type.TEXT
        )

        assert "user" in get_data, "Expected user object in response"
        assert get_data["user"]["email"] == context.email, "Returned email does not match"