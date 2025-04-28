liczba = input("podaj liczbę: ")

try:
    wynik = int(liczba)
except ValueError:
    print("to nie liczba")
else:
    print(f"wszystko było ok", "\n" , {wynik})
