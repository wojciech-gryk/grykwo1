def gen_test():
    yield "a"
    yield "b"
    yield "c"

for x in gen_test():
    print(x)