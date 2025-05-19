def add(a: int, b: int) -> int:
    return a + b

if __name__ == '__main__':
    res = add(3,5)
    print(res)
    res2 = add( 3.4, 23.55)  # podkreśla, bo to nie są inty
    print(res2)
    res3 = add("aaa", "www")
    print(res3)