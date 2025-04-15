tekst = "Masz na imię "

name = input("podaj swoje imię: ")
string_add = tekst + name + ". Czesc"
print(string_add)

formated = "Masz na imię: {}. Cześć".format(name)
print(formated)

formated1 = f"Masz na imię: {name}. Cześć"
print(formated1)

formated2 = f"Masz na imię: {name}. Twoje imie ma {len(name)} liter"
print(formated2)