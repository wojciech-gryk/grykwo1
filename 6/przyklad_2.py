wartosc = "3asa"

try:
    wartosc_int = int(wartosc)
    x = 10/0
except Exception as e:
    print("Exception")
    print(e)
    print("type od exception", type(e))
except ValueError as e:
    print("VALUE")
    print(e)
    print("type od exception", type(e))