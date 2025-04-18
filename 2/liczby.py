# Stworz listę różnych liczb typu int oraz float
# Napisz pętlę, która zsumuje wszystkie te liczby i wypisz na końcu wynik

liczby = [3, 7.5, 33, 12.83, 4.19, 0.4]
suma = 0

for i in liczby:
    suma = suma + i

print(F"Suma liczb w liście to {round(suma,2)}")