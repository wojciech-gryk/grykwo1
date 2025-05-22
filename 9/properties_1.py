class Osoba:
    def __init__(self, imie: str, nazwisko: str, pesel: str):
        self._imie = imie
        self._nazwisko = nazwisko
        self._pesel = pesel

    @property
    def imie(self):
        return self._imie

    @imie.setter
    def imie(self, value):
        self._imie = value.capitalize()

    def get_imie(self):
        return self._imie

    def set_imie(self, value):
        self._imie = value

if __name__ == '__main__':
    o = Osoba("Jan", "Nowak", "12345678910")
    print(o.get_imie())
    print(o._imie)
    print((o.imie))
    o.imie = "stefan"
    print(o)