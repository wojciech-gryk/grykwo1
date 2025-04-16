list = ["ale", "ma", "kota", "kot", "ma", "Alę"]

# iteracja po przystych elementach listy
print("1")
for i, x in enumerate(list):
    if i % 2:
        continue
    print("i: ", i, "x: ", x)

#`print("2")
#for i, x in enumerate(list):
#    print("i: ", i, "x: ", x)
#    if i>=1:
#        break
#