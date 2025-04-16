text = "ale ma kota"
list = ["ale", "ma", "kota"]

for x in text:
    print("x: ", x)
    print("x: ", type(x))

for i, x in enumerate(text):
    print("i: ", i, "x: ", x)

for x in list:
    for y in x:
        print("y: ", y, type(y))