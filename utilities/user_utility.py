from faker import Faker

fake = Faker()

def generate_user_data(email: str):
    user_data = {
        "name": fake.first_name(),
        "email": email,
        "password": fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True),
        "title": "Mr",
        "birth_date": f"{fake.random_int(min=1, max=28):02d}",
        "birth_month": f"{fake.random_int(min=1, max=12):02d}",
        "birth_year": str(fake.random_int(min=1950, max=2005)),
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "company": fake.company(),
        "address1": fake.street_address(),
        "address2": fake.secondary_address(),
        "country": "United States",
        "zipcode": fake.postcode(),
        "state": fake.state(),
        "city": fake.city(),
        "mobile_number": fake.phone_number()
    }
    return user_data