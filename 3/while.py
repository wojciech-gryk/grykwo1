result = input("podaj jakąś liczbę: ")
zagadka = 5

try:
    while int(result) != zagadka:
        print("to nie ta liczba!")
        result = input("podaj jakąś liczbę: ")
except:
    print("to nie jest liczba")
    result = input("podaj jakąś liczbę: ")

print("\nzgadłeś!")