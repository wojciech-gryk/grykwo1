# pętla for to w zasadzie foreach

lista = ["ale", "ma", "kota"]

for x in lista:
    print("wartość: ", x)


for i, x in enumerate(lista):
    print("wartość", x, "indeks", i)


print("rewersed")
for x in reversed(lista):
    print("wartość", x)

print("enumerated reversed")
for i, x in enumerate(reversed(lista)):
    print("wartość", x, "indeks", i)