# zmodyfikuj program z zadania 05 tak, aby co druga litera znalazła się w wynikowej liście
znaki = input("podaj ciąg znaków: ")
lista = []
i = 0

while i != len(znaki):
    lista.append(znaki[i])
    i = i+2

print(lista)