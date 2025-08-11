from behave import *
import allure
from API.api_client import ApiClient

@when("I try to update the brands list using an unsupported method")
def step_impl_update_brands_list(context):
    client = ApiClient(base_url="https://automationexercise.com/api")
    payload = {"brand": "FAKE_BRAND"}
    context.response = client.send_put_request(endpoint="/brandsList", payload=payload)

@then("I should receive a method not allowed error")
def step_impl_verify_method_not_allowed(context):
    with allure.step("Verify response status and error message"):
        response_json = context.response.json()

        assert context.response.status_code == 200, "Expected status code 200 (note: API does not return 405 here)"
        assert response_json["responseCode"] == 405, "Expected responseCode to be 405"
        assert response_json["message"] == "This request method is not supported.", \
            "Expected error message about unsupported method"