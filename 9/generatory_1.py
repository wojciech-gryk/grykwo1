lista = [1, 2]

for x in range(10, 14):
    print(x)

# nieoptymalne podejście !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def gen_numbers(start: int, to: int):
    result = []
    i = start
    while True:
        result.append((i))
        i += 1
        if i >= to:
            break
    return result

# nieoptymalne podejście !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def gen_numbers(start: int, to: int):
    i = start
    while True:
        yield i
        i += 1
        if i >= to:
            break




lista2 = gen_numbers(10, 20)
print(lista2)

for x in gen_numbers(10, 14):
    print(x)