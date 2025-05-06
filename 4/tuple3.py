def test():
    return  1, "test"

x, y = test()
print(x, y)
z = test()
print(z, type(z))