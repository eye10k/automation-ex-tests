import allure

# utilities/api_assertions.py
import allure


def verify_error_response(response, expected_code: int, expected_message: str):

    with allure.step("Verify error response"):
        response_json = response.json()
        assert response_json.get("responseCode") == expected_code, (
            f"Expected responseCode {expected_code}, got {response_json.get('responseCode')}"
        )
        assert response_json.get("message") == expected_message, (
            f"Expected message '{expected_message}', got '{response_json.get('message')}'"
        )