# Napisz program, który poprosi użytkownika o liczbę. Jeśli użytkownik wypisał złe dane, poproś aby podał je ponownie
# Zapisz tę liczbę w postaci int w zmiennej, następnie porównaj go z wartością zmiennej
# "magiczna_liczba". Sprawdź, czy liczba jest większa, mniejsza a może równa magicznej liczbie?
# Pytaj o liczbę, dopóki użytkownik nie trafi.

magiczna_liczba = 5

while True:
    try:
        a = int(input("podaj jakąś liczbe: "))
        if a < magiczna_liczba:
            print("\nTwoja liczba jest za mała")
        elif a > magiczna_liczba:
            print("\nTwoja liczba jest za duża")
        else:
            print("\nbrawo! zgadłeś!")
            break
    except:
        print("to nie jest liczba!")

print(f"\npodana przez Ciebie liczba to {a}, a magiczna liczba to {magiczna_liczba}")