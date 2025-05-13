def podaj_liczbe():
    wartosc = input(("podaj liczbe: "))

    try:
        wartosc_int = int(wartosc)
        10 / 0
    except ValueError as e:
        print("To nie jest liczba")
    else:
        print(wartosc_int)
    finally:
        print("to sie wykona zawsze")

if __name__ == '__main__':
    podaj_liczbe()
    print("koniec")