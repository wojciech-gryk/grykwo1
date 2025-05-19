def func1():
    return 1

func2 = func1
func1 = "test"

if __name__ == '__main__':
    print(func2)
    print(type(func2))
    print(func2)

    print(func1)
    print(type(func1))