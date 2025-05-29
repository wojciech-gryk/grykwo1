import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
response.raise_for_status()

users = response.json()
#print(users)

class User:
    def __init__(self, name: str, username: str, phone: str, email: str, address: str, zipcode: str):
        self._name = name
        self._username = username
        self._phone = phone
        self._email = email
        self._address = None

    @classmethod
    def fro_dict(cls, data):
        return cls(data["name"], data["username"], data["phone"], data["email"])

    @property
    def address(self):
        return self._address

# konwersja danych na stringa
    def __str__(self):
        return f"User{self._username}"

# reprezentacja danych
    def __repr__(self):
        return f"User{self._username}"

class Address:
    def __init__(self, city: str, zipcode: str):
        self._city = city
        self._zipcode = zip

    @classmethod
    def from_dict(cls):
        return cls(data["city"], data["zipcode"])


if __name__ == '__main__':
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    users = response.json()

    user_objects = []
    for user in users:
        u = User.from_dict(user)
        print(u)
