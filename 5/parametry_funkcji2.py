def function(a,b,c=10):
    return a + b + c

if __name__ == '__main__':
    x = (1, 2, 3)
    wynik = function(*x)   # WAŻNA RZECZ !!!!! * - rozpakowuje krotkę
    print(wynik)
    y = (1, 2)
    wynik = function(*y)  # WAŻNA RZECZ !!!!! * - rozpakowuje krotkę
    print(wynik)
