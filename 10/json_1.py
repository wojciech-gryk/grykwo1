import json

with open("test.json", "r") as f:
    json_file = f.read() # wczytanie jako czysty json
    json_content = json.loads(json_file) #wczytanie jako słownik

print(json_content)

with open("test.json", "r") as f:
    json_content = json.load(f)

print(json_file)
print(json_content)