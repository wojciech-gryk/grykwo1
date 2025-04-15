print("hasło musi zawierać minimum 10 znaków i kropka")
pass1 = input("podaj hasło: ")
pass2 = input("podaj ponownie hasło: ")

if pass1 == pass2:
    if len(pass1) >= 10 and pass1.count(".") > 0:
        print("hasło ustawione poprawnie")
    else:
        "hasło za krótkie lub nie kropki"
else:
    print("hasła niepoprawne")
