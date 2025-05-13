f = open("plik.txt", "r")

while True:
    linia = f.readline().strip()
    if linia == "":
        break
    print(linia)
