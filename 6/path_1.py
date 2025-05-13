from  pathlib import Path

p =Path("plik.txt")

with open(p, "r") as f:
    print(f.readlines())

with p.open("r") as f:
    print(f.readlines())