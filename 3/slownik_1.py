slownik = {
    "a" : 1,
    "b" : None,
    "c" : "test",
    "d" : [1,2,3],
    10  : 0.4
}

print(slownik[10])
print(slownik["c"])

v = slownik["d"]
print("d3:", v[2])
print("d3:", slownik["d"][2])