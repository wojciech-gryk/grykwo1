lista = ["a", "b", "c", "d"]

for x in lista:
    print(x)


# tak działa powyższa pętla
i = iter(lista)
while True:
    try:
        v = next(i)
        print(v)
    except StopIteration:
        break