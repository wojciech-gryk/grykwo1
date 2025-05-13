from  pathlib import Path

p = Path("plik.txt")
print(p)

with p.open("r") as f:
    print(f.readlines())

if p.exists():
    print("ścieżka istnieje")