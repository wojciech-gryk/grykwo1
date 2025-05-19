from dataclasses import dataclass, field

@dataclass
class Osoba:
    imie: str
    nazwisko: str
    wiek: int
    _pesel: str = field(repr=False)

    def przywitaj(self):
        print(f"Cześć. Nazywams się {self.imie} i mam {self.wiek} lat.")

if __name__ == '__main__':
    osoba1 = Osoba("jan", "Nowak", 22, 45114154541)
    print(osoba1.imie)
    osoba1.przywitaj()
    print(osoba1)