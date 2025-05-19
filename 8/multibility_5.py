def f(arg):
    arg["in function"] = "value"

if __name__ == '__main__':
    slownik = {}


slownik["test"] = "wartosc"
slownik["test2"] = [1,2,3,4]

print(slownik)

f(slownik)
print(slownik)