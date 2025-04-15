imie = input("Podaj swoje imię: ")
nazwisko = input("Podaj swoje nazwisko: ")

email = imie[0]+imie[-1]+nazwisko+"@gmail.com"
print("\n" + email.lower())