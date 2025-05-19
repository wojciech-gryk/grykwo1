class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self._imie = imie
        self._nazwisko = nazwisko
        self._wiek = wiek

class Sprzedawca(Osoba):
    pass

if __name__ == '__main__':
    o = Osoba("jan", "Nowak", 22)
    s = Sprzedawca("Ola", "dupa", 17)

    if isinstance(o, Osoba):
        print("o to osoba")
    else:
        print("o to nie osoba")

    if isinstance(s, Osoba):
        print("s to osoba")
    else:
        print("s to nie osoba")
