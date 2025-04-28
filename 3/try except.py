liczba = input("podaj liczbę: ")
try:
    wynik = int(liczba)
    print(wynik)
except ValueError:
    print("to nie liczba")
