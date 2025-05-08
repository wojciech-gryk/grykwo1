class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self._imie = imie
        self._nazwisko = nazwisko
        self._wiek = wiek

    def przywitaj(self):
        print(f"cześć! nazywam się {self._imie} {self._nazwisko} i mam {self._wiek} lat")

    def minal_rok(self):
        self._wiek = self._wiek + 10

    def zmien_nazwisko(x, nazwisko):
        x._nazwisko = nazwisko


if __name__ == '__main__':
    osoba1 = Osoba("Wojtek", "Gryk", 35)
    # złe, dane prtywatne
    #osoba1._wiek = osoba1._wiek + 1
    osoba1.minal_rok()
    osoba1.przywitaj()