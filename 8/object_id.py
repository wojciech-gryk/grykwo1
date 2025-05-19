lista1 = [1,2,3]
lista2 = lista1
lista3 = [1,2,3]

print("lista", id(lista))
print("lista", id(lista2))
print("lista", id(lista3))

if lista1 == lista3:
    print("SA RÓWNE")
else:
    print("nie są równe")

# IS pokazuje rózne obiekty bo mają rózne ID
if lista1 is lista3:
    print("SA RÓWNE")
else:
    print("nie są równe")
