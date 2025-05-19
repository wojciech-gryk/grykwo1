from copy import deepcopy

lista = ["a", "b", "c"]
#lista2 = lista
lista2 = deepcopy(lista)

lista.append("d")
lista2.append("e")

print(lista)
print(lista2)

