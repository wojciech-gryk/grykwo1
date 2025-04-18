# Stwórz listę z 5 różnymi imionami
# Poproś użytkownika, aby podał imię.
# Sprawdź, czy podane przez użytkownika imię znajduje się na liście imion.

imiona = ["Ola", "Ala", "Jan", "Maciek", "Iza"]

imie = input("Podaj imię: ")
dopasowane_imie = None

if imie.lower() in [i.lower() for i in imiona]:
    print("To imię znajduje się na liście")
else:
    print("tego imienia nie ma na liście")