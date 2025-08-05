from behave import when, then
import requests
import json
import allure

@when("I try to update the brands list using an unsupported method")
def step_impl_update_brands_list(context):
    with allure.step("Send a PUT request to the brands list endpoint"):
        url = "https://automationexercise.com/api/brandsList"
        payload = {
            "brand": "FAKE_BRAND"
        }
        context.response = requests.put(url, data=payload)
        allure.attach(
            json.dumps(payload, indent=2),
            name="Request Payload",
            attachment_type=allure.attachment_type.JSON
        )
        allure.attach(
            context.response.text,
            name="Response Body",
            attachment_type=allure.attachment_type.TEXT
        )

@then("I should receive a method not allowed error")
def step_impl_verify_method_not_allowed(context):
    with allure.step("Verify response status and error message"):
        response_json = context.response.json()

        assert context.response.status_code == 200, "Expected status code 200 (note: API does not return 405 here)"
        assert response_json["responseCode"] == 405, "Expected responseCode to be 405"
        assert response_json["message"] == "This request method is not supported.", \
            "Expected error message about unsupported method"