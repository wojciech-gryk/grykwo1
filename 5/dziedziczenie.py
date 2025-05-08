class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self._imie = imie
        self._nazwisko = nazwisko
        self._wiek = wiek

    def przywitaj(self):
        print(f"cześć! nazywam się {self._imie} {self._nazwisko} i mam {self._wiek} lat")

class Klient(Osoba):
    pass

class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, wiek, stanowisko):
        super().__init__(imie, nazwisko, wiek)
        self._stanowisko = stanowisko

    def udziela_pomocy(self, produkt):
        print(f"tpo jest produkt {produkt}")

    def przywitaj(self):
        super().przywitaj()
        print("w czym mogę pomóc?")

    def podaj_wiek(self):
        print("podaj wiek", self._wiek)


class Menadzer(Pracownik):
    def zamknij_sklep(self):
        print("sklep zamknięty")

if __name__ == '__main__':
    k = Klient("jan", "Nowak", 33)
    s = Pracownik("Jan", "Dupa", 33,  "sprzedawca")
    m = Menadzer( "ola", "DD", 33, "Manadzer")

    k.przywitaj()
    s.przywitaj()
    s.podaj_wiek()
    s.udziela_pomocy("sluchawki")
    m.przywitaj()
    m.zamknij_sklep()
