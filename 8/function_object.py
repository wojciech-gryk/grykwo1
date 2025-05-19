

a =1
b = "aaaa"

print(id(a))
print(type(a))

print(id(b))
print(type(b))

class Fake:
    pass

f = Fake()

print(type(f))

def func1():
    return 1

print(type(func1()))

second_name = func1()
print(type(second_name))