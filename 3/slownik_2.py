slownik = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}

print(slownik["c"])
slownik["c"] = 999
print(slownik["c"])

slownik["e"] = 20
print(slownik["e"])

slownik[123] = 123
print(slownik[123])

slownik["123"] = "coś innego"
print(slownik["123"])

print(slownik)