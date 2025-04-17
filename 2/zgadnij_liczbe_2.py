# Napisz program który zapyta użytkownika o liczbę z przedziału 1 do 10
# używając funkcji do generowania liczb losowych wygeneruj liczbę z tego samego przedziału.
# https://docs.python.org/3/library/random.html#random.randint
# Porównaj liczbę od użytkownika z liczbą losową i poinformuj użytkownika czy zgadł.

import random

x = random.randint(1, 10)
print(x)
liczba = int(input("Podaj liczbę: "))

if liczba == x:
    print("Brawo! Zgadłeś!")
elif liczba < x:
    print("Twoja liczba jest mniejsza od wylosowanej")
else:
    print("Twoja liczba jest większa od wylosowanej")
