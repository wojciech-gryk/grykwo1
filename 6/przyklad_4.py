haslo = 10

class WrongError(Exception):
    pass

def uwierzytelnij():
    result = input("Podaj hasło: ")
    if haslo != result:
        raise WrongError("błędne hasło")

    return {"imie": "Jakub"}


if __name__ == '__main__':
    try:
        uzytkownik = uwierzytelnij()
    except WrongError as e:
        print(e)
    else:
        print(f"witaj {uzytkownik[imie]}")

    print("koniec")

