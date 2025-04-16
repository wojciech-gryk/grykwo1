l = [1, 2, 3]
result =input("podaj liczbę: ")

try:
    if int(result) in l:
        print("trafiłeś")
    else:
        print("nietrafiłeś")
except:
    print("to nie liczba")