class A:
    def test(self):
        pass

class B(A):
    def test(self):
        pass

class C(A):
    def test(self):
        pass

class D(B, C):
    def test(self):
        super().test()

class E(D, C):
    def test(self):
        super().test()

if __name__ == '__main__':
    d = D()
    d.test()
    print(d)