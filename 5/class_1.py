class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przywitaj(self):
        print(f"cześć! nazwyam się {self.imie} i mam {self.wiek} lat")


if __name__ == '__main__':
    osoba1 = Osoba("Wojtek", "Gryk", "35")
    osoba2 = Osoba("Jan", "Nowak", "45")
    print(osoba1.imie)
    print(osoba2.imie)
    osoba1.przywitaj()
    osoba2.przywitaj()