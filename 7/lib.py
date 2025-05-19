#import pytest

DOMENA = "gmail.com"

def generuj_adres_email(imie, nazwisko):
    first_letter_name = imie[0]
    last_name = nazwisko
    email  = f"{first_letter_name}.{last_name}@{DOMENA}"


