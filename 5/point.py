class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"<{self.x} {self.y}"

    def __add__(self, other):
        return Vector(self.x + other.x,  self.y + other.y)

if __name__ == '__main__':
    v1 = Vector(1, 2)
    v2 = Vector(3,5)
    print(v1 + v2)
