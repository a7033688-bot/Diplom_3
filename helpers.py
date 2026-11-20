import random
import string


def generate_user():
    email = ''.join(random.choices(string.ascii_lowercase, k=6)) + '@yandex.ru'
    password = str(random.randint(1000,9999))
    name = ''.join(random.choices(string.ascii_lowercase, k=8))
    return {
            "email": email,
            "password": password,
            "name": name
    }