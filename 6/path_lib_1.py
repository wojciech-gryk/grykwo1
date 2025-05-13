from  pathlib import Path

p = Path("/")
print(p)

new_p = p  / "home" / "student"
print(new_p)
print(new_p.exists())
print(new_p.is_dir())
print(new_p.is_file())
print(new_p.iterdir())
for path in new_p.iterdir():
    print(path)

for path in new_p.iterdir():
    print(path.name)