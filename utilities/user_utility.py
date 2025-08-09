from faker import Faker
import json

def create_user(self):
    faker = Faker()
    return json.dumps({
        "name": faker.name(),
        "email": faker.email(),
        "password": faker.password(),
        "email": self.email
    })
