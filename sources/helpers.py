import faker
import random


def get_sign_up_data():
    fake = faker.Faker()
    first_name = 'marina'
    last_name = 'vasileva'
    cohort_number = 13
    random_digits = random.randint(100, 999)
    domain = fake.free_email_domain()
    email = f"{first_name}{last_name}{cohort_number}{random_digits}@{domain}"
    password = fake.password(length=6)
    return email, password
