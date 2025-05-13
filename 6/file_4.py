f = open("plik.txt", "r")

f.seek(10)  # przesunięcie o 10 znaków
line = f.read(10)
print(line)

