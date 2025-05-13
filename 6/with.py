f = open("plik.txt", "r")
lines = f.readlines()
print(lines)


print(f.closed)

if not f.closed:
    f.close()

print(f.closed)


