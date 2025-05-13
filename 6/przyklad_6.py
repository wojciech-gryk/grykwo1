x = 3

class ZleIDUzytkownika(Exception):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"błędne ID: {self.id}"

uzytkownicy = [
    {"imie": "jakub"},
    {"imię": "kasia"}
]

def podaj_dane_uzytkownika(id):
    try:
        uzytkownik = uzytkownicy[id]
    except IndexError:
        raise ZleIDUzytkownika(id)
    else:
        return uzytkownik


if __name__ == '__main__':
    u = podaj_dane_uzytkownika(x)