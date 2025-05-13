# Napisz klasę reprezentującą okrąg o nazwie "Okrag". Aby stworzyć okrąg należy podać promień okręgu (parametr w inicjalizatorze).
# Napisz metodę obliczającą i zwracającą obwód orkęgu o nazwie "obwod".
# Napisz metodę obliczającą i zwracającą pole okręgu o nazwie "pole".
# Pomocny w obliczeniach może być moduł math
# Nadpisz odpowiednią metodę aby print na obiekcie klasy Okrag wyświetlał się jako <okrąg: 3> gdzie 3 to promień.
# Napisz na dole pliku używając skłądni "if __name__ == '__main__'" testy klasy
# aby sprawdzić czy obiekt działa prawidłowo.
import math

class Okrag:
    def __init__(self, promien):
        self.promien = promien

    def obwod(self):
        return 2 * math.pi * self.promien

    def pole(self):
        return math.pi * self.promien ** 2

    def __str__(self):
        return f"<okrąg: {self.promien}>"


# Testy klasy
if __name__ == '__main__':
    okrag = Okrag(1)
    print(okrag)  # <okrąg: 3>

    print(f"Obwód: {okrag.obwod():.2f}")
    print(f"Pole: {okrag.pole():.2f}")


