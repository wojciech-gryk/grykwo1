# Stwórz listę zawierającą kilka wyrazów. Następnie znajdź najdłuższy wyraz na liście i wypisz
# go na konsoli razem z jego długością.


lista = ["jan", "kura", "telefon", "jezioro", "fortepian", "niezapominajka", "miś"]
j = 0
k = 0
poz = 0

for i in lista:
    k = len(i)
    if k > j:
        j = k
        poz = lista.index(i)

print(f"Najdłuższe słowo to \"{lista[poz]}\", które ma {j} liter")