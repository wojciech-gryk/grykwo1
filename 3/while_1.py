zagadka = 5

# while True:
#     result = input("podaj jakąś liczbę: ")
#     while result == zagadka:
#         print("zgadłeś!")
#         break
#     else:
#         print("nie zgadłeś")

try:
    while True:
        result = input("podaj jakąś liczbę: ")
        if int(result) == zagadka:
            print("zgadłeś!")
            break
        print("nie zgadłeś")
except ValueError:
    print("to nie liczba!")
    result = input("podaj jakąś liczbę: ")