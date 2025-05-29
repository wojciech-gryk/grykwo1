import json

with open("test_3.json", "r") as f:
    content = json.load(f)

print(content)

for tel in content["tel"]:
    print("nr tel:", tel)

for adres in content["adresy"]:
    print("ulica:", adres["ulica"])
    print("dom:", adres["dom"])



