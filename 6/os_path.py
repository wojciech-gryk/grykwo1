import os

if os.path.exists("plik.txt"):
    print("plik istnieje")


a = os.path.join("test", "drugi", "trzeci")  # budowanie ścieżki  test/drugi/trzeci
b = os.path.split("/home/student/PycharmProjects/PythonProject/.venv/bin/python")
c = os.path.abspath("/home/student/PycharmProjects/PythonProject/.venv/bin/python")  # ścieżka absolutna
d = os.path.isabs("/home/student/PycharmProjects/PythonProject/.venv/bin/python") # czy ścieżka istnieje
print(a)
print(b)
print(c)
print(d)