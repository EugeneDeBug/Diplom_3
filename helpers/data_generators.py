from faker import Faker

fake = Faker(locale='ru_RU')

def generate_user_data():
    return {
        "email": fake.email(domain="yandex.ru"),
        "password": fake.password(length=10),
        "name": fake.first_name()
    }
