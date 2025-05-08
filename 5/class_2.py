class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przywitaj(self):
        print(f"cześć! nazywam się {self.imie} {self.nazwisko} i mam {self.wiek} lat")

    def minal_rok(self):
        self.wiek = self.wiek + 10

    def zmien_nazwisko(x, nazwisko):
        x.nazwisko = nazwisko


if __name__ == '__main__':
    osoba1 = Osoba("Wojtek", "Gryk", 35)
    osoba1.minal_rok()
    osoba1.zmien_nazwisko("Dupa1")
    osoba1.przywitaj()
