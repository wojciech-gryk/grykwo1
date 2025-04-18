# Zmodyfikuj program z zadania 05 tak, aby podczas dodawania na listę znaków
# policzyć ile z tych znaków to wielkie litery. Wypisz ilość wielkich liter w
# ciągu znaków od użytkownika.

# Podpowiedź - znajdź metodę, która sprawdza, czy string skłąda się z wielkich liter.
znaki = input("podaj ciąg znaków: ")
lista = []
i = 0
j = 0

while i != len(znaki):
    znak =znaki[i]
    if znak.isupper():
        j = j +1
    lista.append(znaki[i])
    i = i+1

print(lista)
print("Liczba wielkich liter z liście to: ", j)