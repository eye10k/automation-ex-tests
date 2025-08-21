from behave import *
from API.api_client import ApiClient
from utilities.api_assertions import verify_error_response

@when("I try to update the brands list using an unsupported method")
def update_brands_list(context):
    client = ApiClient()
    payload = {"brand": "FAKE_BRAND"}
    context.response = client.send_put_request(endpoint="/brandsList", payload=payload)

@then("I should receive a method not allowed error")
def verify_method_not_allowed(context):
    verify_error_response(
        context.response,
        expected_code=405,
        expected_message="This request method is not supported."
    )