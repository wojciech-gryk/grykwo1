# Napisz program który zapyta użytkownika o liczbę z przedziału 1 do 10
# używając funkcji do generowania liczb losowych wygeneruj liczbę z tego samego przedziału.
# https://docs.python.org/3/library/random.html#random.randint
# Porównaj liczbę od użytkownika z liczbą losową i poinformuj użytkownika czy zgadł.
# Jeśli użytkownik poda błędne dane, to poproś o podanie poprawnych.
# Niech użytkownik ma tylko 3 próby na zgadnięcie liczby. Podanie błędnych danych nie powinno liczyć się jako próba!
# Wyświetlaj użytkownikowi, którą próbę właśnie podejmuje.
import random as rd

a = rd.randint(0,9)
print(a)
x = 0

while x !=3:
    try:
        liczba = int(input("podaj swoją liczbę: "))
        if liczba == a:
            print("zgadłeś, brawo!")
            break
        else:
            x = x +1
            print(f"niestety nie zgadleś. Pozostała liczba prób to: {3-x}")
    except:
        print("to nie jest liczba!")

