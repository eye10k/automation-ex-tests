class User:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        password: str,
        birth_day: str,
        birth_month: str,
        birth_year: str,
        company: str,
        address: str,
        address2: str,
        country: str,
        state: str,
        city: str,
        zipcode: str,
        mobile: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.company = company
        self.address = address
        self.address2 = address2
        self.country = country
        self.state = state
        self.city = city
        self.zipcode = zipcode
        self.mobile = mobile
