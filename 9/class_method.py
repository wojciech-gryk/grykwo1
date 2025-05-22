class Punkt:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f"Punkt({self._x}, {self._y})"

def Punkt_zero():
    return Punkt(0,0)

if __name__ == '__main__':
    p1 = Punkt (10, 10)
    p2 = Punkt (0, 20)
    p3 = Punkt_zero()

    print(p1)
    print(p2)
    print(p3)

