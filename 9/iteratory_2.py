lista = ["a", "b", "c", "d"]

for x in lista:
    if x in ("a","b"):
        lista.remove(x)
    print(x)

for i, x in enumerate(lista):
    if x in ("a","b"):
        lista.remove(x)
    print(lista[i])
