



lista = [1,2,3]

for x in lista:
    print(x)

def func1():
    return  1

print("func1")
c = func1
res = c()

print(res)

if callable(c):
    print("is collable")
else:
    print("not collable")