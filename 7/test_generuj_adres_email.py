from lib import  generuj_adres_email

def test_czy_dziala():
    rezult = generuj_adres_email("jan","nowak")

    assert  rezult != None
    assert type("") == type(rezult)

def test_czy_funcja_zwraca_prawidlowy_adres():
    rezult = generuj_adres_email("jan", "nowak")

    assert  rezult == "j.nowak@gmail.com"



