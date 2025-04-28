liczba = input("podaj liczbę: ")
wynik = None

try:
    wynik = int(liczba)
    print(wynik)
except ValueError:
    print("to nie liczba")
else:
    print("wszystko jest ok")


print(wynik)