import json
from simple_dict import example

with open("test.json", "w") as f:
    json.dump(example, f)

print(f)