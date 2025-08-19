from faker import Faker
from models.user import User
from models.payment_card import PaymentCard

fake = Faker()

def generate_user(email: str = None, for_ui: bool = False):
    first_name = fake.first_name()
    last_name = fake.last_name()
    password = fake.password(
        length=12, special_chars=True, digits=True, upper_case=True, lower_case=True
    )

    # День и месяц
    if for_ui:
        # Для UI: числа без ведущего нуля (чтобы селект работал)
        birth_day = str(fake.random_int(min=1, max=28))
        birth_month = str(fake.random_int(min=1, max=12))
    else:
        # Для API: формат с ведущим нулём
        birth_day = f"{fake.random_int(min=1, max=28):02d}"
        birth_month = f"{fake.random_int(min=1, max=12):02d}"

    birth_year = str(fake.random_int(min=1950, max=2005))
    company = fake.company()
    address1 = fake.street_address()
    address2 = fake.secondary_address()
    country = "United States"
    state = fake.state()
    city = fake.city()
    zipcode = fake.postcode()
    mobile = fake.phone_number()

    if for_ui:
        # Вернём объект User для UI
        return User(
            first_name,
            last_name,
            password,
            birth_day,
            birth_month,
            birth_year,
            company,
            address1,
            address2,
            country,
            state,
            city,
            zipcode,
            mobile,
        )

    # Вернём dict для API
    return {
        "name": first_name,
        "email": email or fake.email(),
        "password": password,
        "title": "Mr",
        "birth_date": birth_day,
        "birth_month": birth_month,
        "birth_year": birth_year,
        "firstname": first_name,
        "lastname": last_name,
        "company": company,
        "address1": address1,
        "address2": address2,
        "country": country,
        "zipcode": zipcode,
        "state": state,
        "city": city,
        "mobile_number": mobile,
    }

def generate_user_data(email: str):
    return generate_user(email=email, for_ui=False)

def generate_payment_card(with_zero_prefix: bool = False) -> PaymentCard:

    expire_month = f"{fake.random_int(min=1, max=12):02d}" if with_zero_prefix else str(fake.random_int(min=1, max=12))

    expire_year = str(fake.random_int(min=2030, max=2035))

    return PaymentCard(
        holder_name=fake.name(),
        card_number=fake.credit_card_number(),
        expire_month=expire_month,
        expire_year=expire_year,
        cvc=fake.credit_card_security_code()
    )