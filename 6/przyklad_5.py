def podaj_liczbe():
    wartosc = input(("podaj liczbe: "))

    try:
        wartosc_int = int(wartosc)
    except ValueError:
        print("To nie jest liczba")
        raise   # wrzucamy, żeby złapać wyjątek?  - jaki to ma sens????
    else:
        print(wartosc_int)

if __name__ == '__main__':
    podaj_liczbe()
    print("koniec")