
def f(arg):
    arg.append("c")

if __name__ == '__main__':
    lista = []
    lista2 = list()

    lista.append("a")
    lista[0] = "b"
    print(lista)

    f(lista)
    print(lista)
