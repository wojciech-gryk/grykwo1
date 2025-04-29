# Napisz program, który wczytuje od użytkownika długość boku a i b prostokąta.
# Wartości przypisz do zmiennych "bok_a" oraz "bok_b" jako typy float.
# Zapewnij, aby użytkownik był pytany o dane, dopóki nie poda prawidłowych wartości
# Oblicz oraz wypisz na konsoli pole i obwód prostokąta
# Wyświetl komunikat, jeśli podany prostokąt jest kwadratem

def podaj_bok(bok):
    while True:
        try:
            dlugosc = float(input("podaj długość boku: "))
            if dlugosc <=0:
                print("długość boku musi być większa od zera")
            else:
                return dlugosc
        except:
            print("wartość boku nie jest liczbą")

a = podaj_bok("a")
#print(a)
b = podaj_bok("b")
#print(b)

if a == b:
    print(f"\nfigura jest kwadratem o obwodzie ={2*a + 2*b} i polu powierzchni = {a*b}.")
else:
    print(f"\nfigura jest prostokątem o obwodzie ={2 * a + 2 * b} i polu powierzchni = {a * b}.")