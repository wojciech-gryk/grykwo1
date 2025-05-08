def function(a="a",b="b",c="c"):
    print(a, b, c)


if __name__ == '__main__':
    function(c="test123", a=123)
    slownik = {
        "a": "a ze słownika",
        "c": "c ze słownika"
    }

    function(**slownik)   # WAŻNA RZECZ - wypakowanie słowmika
