slownik = {
        "a": "test",
        "b": "test1",
        "list": [1,2,3]
           }

for i in slownik:
    print(slownik[i])

for klucz in slownik:
    print(klucz)

for klucz in slownik:
    print(klucz, ":", slownik[klucz])

for x in slownik.values():
    print(x)

# takie samo jak
# for i in slownik
for i in slownik.keys():
    print(i)

for k, v in slownik.items():
    print(k, v, type(k), type(v))