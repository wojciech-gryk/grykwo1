def func(l=[]):
    return l

if __name__ == '__main__':
    l1 = func()
    l2 =  func()
    
    l1.append("a")

    print(l1)
    print(l2)
