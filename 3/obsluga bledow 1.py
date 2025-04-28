lista = [1,2,3]
try:
    print(lista[20])
except IndexError:
# w razie czego łapanie dowolnego błedu
# except Exception:
    print("brak wartości")