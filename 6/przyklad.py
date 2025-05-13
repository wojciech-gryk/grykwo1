wartosc = "3asa"

try:
    wartosc_int = int(wartosc)
    x = 10/0
except AttributeError as e:
    print("to nie liczba")
    print(e)
    print("typ błędu", type(e))
except ValueError as e:
    print("to nie liczba")
    print(e)
    print("typ błędu", type(e))

