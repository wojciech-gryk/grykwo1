def func(l=None):
    if l is None:
        l = []
    print(id(l))
    l.append(1)
    return l

if __name__ == '__main__':
    my_list = func(["a","b","c"])
    print(my_list)
    my_list = func(my_list)
    print(my_list)

if __name__ == '__main__':
    my_list = func()
    print(my_list)

    a = func()
    print(a)