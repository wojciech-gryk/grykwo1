with open("plik.txt", "r") as f:
    lines = f.readlines()
    print(lines)   # ten blok sam otwiera i sam zamyka plik

print("po with")

print(f.closed)

if not f.closed:
    f.close()

print(f.closed)


