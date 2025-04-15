result = input("wpisz tekst: ")
print("tekst wpisany:", result),"typ:", type(result)


tekst = input("Podaj liczbę całkowitą: ")

try:
    liczba = int(tekst)
    print("To jest liczba całkowita!")
except:
    print("To NIE jest liczba całkowita.")



