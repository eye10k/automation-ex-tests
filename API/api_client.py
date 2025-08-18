import requests
import json
import allure
from utilities import config_reader

class ApiClient:
    DEFAULT_BASE_URL = config_reader.API_BASE_URL

    def __init__(self, base_url=None):
        self.base_url = base_url or self.DEFAULT_BASE_URL

    def send_get_request(self, endpoint, params=None, headers=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        with allure.step(f"Send GET request to {url}"):
            allure.attach(url, name="Request URL", attachment_type=allure.attachment_type.TEXT)

            if params:
                allure.attach(json.dumps(params, indent=2), name="Request Parameters", attachment_type=allure.attachment_type.JSON)
            if headers:
                allure.attach(json.dumps(headers, indent=2), name="Request Headers", attachment_type=allure.attachment_type.JSON)
            else:
                headers = {}

            response = requests.get(url, params=params, headers=headers)

            try:
                allure.attach(json.dumps(response.json(), indent=2), name="Response Body", attachment_type=allure.attachment_type.JSON)
            except ValueError:
                allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.TEXT)

            return response

    def send_post_request(self, endpoint, payload=None, headers=None, use_json=True):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        with allure.step(f"Send POST request to {url}"):
            allure.attach(url, name="Request URL", attachment_type=allure.attachment_type.TEXT)
            if headers:
                allure.attach(json.dumps(headers, indent=2), name="Request Headers", attachment_type=allure.attachment_type.JSON)
            else:
                headers = {}

            if payload:
                if use_json:
                    allure.attach(json.dumps(payload, indent=2), name="Request Payload (JSON)", attachment_type=allure.attachment_type.JSON)
                    response = requests.post(url, json=payload, headers=headers)
                else:
                    allure.attach(str(payload), name="Request Payload (Form Data)", attachment_type=allure.attachment_type.TEXT)
                    response = requests.post(url, data=payload, headers=headers)
            else:
                response = requests.post(url, headers=headers)

            try:
                allure.attach(json.dumps(response.json(), indent=2), name="Response Body", attachment_type=allure.attachment_type.JSON)
            except ValueError:
                allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.TEXT)

            return response

    def send_put_request(self, endpoint, payload=None, headers=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        with allure.step(f"Send PUT request to {url}"):
            allure.attach(url, name="Request URL", attachment_type=allure.attachment_type.TEXT)
            if headers:
                allure.attach(json.dumps(headers, indent=2), name="Request Headers", attachment_type=allure.attachment_type.JSON)
            else:
                headers = {}

            if payload:
                allure.attach(json.dumps(payload, indent=2), name="Request Payload", attachment_type=allure.attachment_type.JSON)

            response = requests.put(url, json=payload, headers=headers)

            try:
                allure.attach(json.dumps(response.json(), indent=2), name="Response Body", attachment_type=allure.attachment_type.JSON)
            except ValueError:
                allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.TEXT)

            return response
