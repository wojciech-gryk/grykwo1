# with open("plik.txt", "r") as f:
#     lines = f.readlines()
#     print(lines)   # ten blok sam otwiera i sam zamyka plik

# to na dole działa mniej więcej tak samo jak to u góry. Zawsze zamknie plik
try:
    f = open("plik.txt", "r")
    lines = f.readlines()
    print(lines)
finally:
    f.close()

print(f.closed)

if not f.closed:
    f.close()

print(f.closed)


