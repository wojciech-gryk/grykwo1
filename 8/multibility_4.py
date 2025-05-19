from copy import deepcopy

lista  = [
    "a", "b", "c",
    [1,2,3],
    "d"
]

lista2 = lista[3]
lista2 = deepcopy(lista[3])

print(lista)
print(lista2)

print("append")
#lista2[3].append(4)
lista2.append("g")
lista2.append(4)

print(lista)
print(lista2)