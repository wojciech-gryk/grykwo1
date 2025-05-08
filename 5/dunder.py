class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self._imie = imie
        self._nazwisko = nazwisko
        self._wiek = wiek

    def __str__(self):
        return f"<Osoba: {self._imie} {self._nazwisko}"

    def __int__(self):
        return self._wiek

    def przywitaj(self):
        print(f"cześć! nazywam się {self._imie} {self._nazwisko} i mam {self._wiek} lat")

if __name__ == '__main__':
    o = Osoba("jan", "Nowak", 44)
    o1 = str(o)
    o2 = str(123)
    print(Osoba)
    print(o1, o2, type(o1), type(o2), sep=" | ")