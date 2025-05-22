lista = ["a", "b", "c", "d"]

for x in lista:
    print(x)

#lista.__iter__()
i = iter(lista)
print(i)
print(type(i))
print(type(lista))

#i.__next__()
temp_i = next(i)
print(temp_i)

temp_i = next(i)
print(temp_i)

temp_i = next(i)
print(temp_i)

temp_i = next(i)
print(temp_i)