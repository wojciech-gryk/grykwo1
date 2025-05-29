import json

with open("test.json", "r") as f:
    json.content = json.load(f)

print(json.content)

with open("text_after_load.json","w") as f:
    json.dump(json.content, f)

print(json.content)