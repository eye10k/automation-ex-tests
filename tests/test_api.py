import allure
import pytest
import requests
import uuid
import json

def test_register_user():
    url = "https://automationexercise.com/api/createAccount"
    email = f"testuser_{uuid.uuid4()}@example.com"

    # Логируем сгенерированный email
    with allure.step("Log generated email"):
        allure.attach(email, name="Generated Email", attachment_type=allure.attachment_type.TEXT)

    payload = {
        "name": "Styd",
        "email": email,
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
    response = requests.post(url, data=payload)

    response_text = response.text
    response_json = json.loads(response_text)
    assert response_json["responseCode"] == 201, "Expected responseCode to be 201"
    assert response.json()['message'] == "User created!"
    assert response.status_code == 200, "Expected status code to be 200"

    # Запрашиваем созданного юзера по email
    get_url = f"https://automationexercise.com/api/getUserDetailByEmail?email={email}"
    get_response = requests.get(get_url)
    get_data = get_response.json()
    #get user by email
    assert "user" in get_data, "Response JSON does not contain 'user'"

    # Сравнение email
    fetched_email = get_data["user"]["email"]
    assert fetched_email == email, f"Expected email {email}, but got {fetched_email}"

    # Логируем полученный email
    with allure.step("Log fetched email from GET"):
        allure.attach(fetched_email, name="Fetched Email", attachment_type=allure.attachment_type.TEXT)


def test_get_brands_list():
    url = "https://automationexercise.com/api/brandsList"
    response = requests.get(url)
    assert response.status_code == 200
    brands = response.json()["brands"]
    print("Available brands:", [b["brand"] for b in brands])





def test_update_brand_list_negative():
    url = "https://automationexercise.com/api/brandsList"
    response = requests.post(url)
    payload = {
         "brand": "FAKE_BRAND"
    }
    response = requests.put(url, data=payload)

    response_text = response.text
    response_json = json.loads(response_text)
    assert response_json["responseCode"] == 405, "Expected responseCode to be 405"
    assert response_json["message"] == "This request method is not supported.", "Expected message to be 'This request method is not supported'"




