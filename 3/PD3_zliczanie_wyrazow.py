# Napisz program który poprosi użytkownika o długi tekst. Następnie użyj słownika do zliczania ile razy dany
# wyraz wystąpił w tekście.
# następnie wyświetla wszystkie wyrazy wraz z ilością ich wystąpień. Nie przejmujcie się kolejnością wyrazów w wyniku.
# zabezpieczcie program tak, aby nie zliczał spacji.

# Przydatna dokumentacja
# https://docs.python.org/3.12/tutorial/datastructures.html#dictionaries
#

# przykład
# ala ma kota ala
# wynik
# ala: 2
# ma: 1
# kota: 1


tekst = input("wprowadź tekst z kilku wyrazów: ")
tekst1 = ' '.join(tekst.split())

slowa = tekst1.split(sep=" ")
i = 0

ilosc = {}

for wyraz in slowa:
    if wyraz in ilosc:
        ilosc[wyraz] = ilosc[wyraz] + 1
    else:
        ilosc[wyraz] = 1

for wyraz, ilosc in ilosc.items():
    print(wyraz , ":", ilosc)

