lista = [1, 2]

for x in range(10, 14):
    print(x)
# nieoptymalne podejście !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def gen_numbers(start: int, to: int):
    i = start
    while True:
        yield i
        i += 1
        if i >= to:
            break

gen = gen_numbers(10, 14)
print(gen)
print(type(gen))

v = next(gen)
print(v)

v = next(gen)
print(v)

v = next(gen)
print(v)

v = next(gen)
print(v)
