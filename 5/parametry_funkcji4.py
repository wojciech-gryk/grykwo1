def function(*args, **kwargs):
    print(len(args))
    for x in args:
        print("values", x)

    for k, v in kwargs.items():
        print(f"key {k}, value {v}")

if __name__ == '__main__':
    function(10, True, 123, "a", end="XXXXXXX")

if __name__ == '__main__':
    a = (1,2,3,4,5,10, True)
    slownik ={
        "end": "<koniec>"
    }
    function(*a, **slownik)