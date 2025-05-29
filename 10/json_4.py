import json

with open("test_2.json", "r") as f:
    content = json.load(f)

print(content)

for tel in content["tel"]:
    print("nr tel:", tel)

print("adres to:")
print("zamieszkanie", content["adres"])
#f = f"Ulica: {adres["ulica"]}"   nie działa, coś zjebałem

print(content["adres"])

