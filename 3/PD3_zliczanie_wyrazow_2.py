# Zmodyfikuj program z zadania 06 tak, aby jedynie wyrazy o długości 3 lub dłuższe były zliczane jako wyrazy
# Wyświetl ilość unikatowych wyrazów, które pojawiły się w wyniku
# Wyświetl sumę wszystkich wyrazów, które pojawiły się w w wyniku

tekst = input("wprowadź tekst z kilku wyrazów: ")
tekst1 = ' '.join(tekst.split())
print(tekst1)

slowa = tekst1.split(sep=" ")
i = 0

ilosc = {}

for wyraz in slowa:
    if wyraz in ilosc:
        if len(wyraz) >= 3:
            ilosc[wyraz] = ilosc[wyraz] + 1
    else:
        if len(wyraz) >= 3:
            ilosc[wyraz] = 1

for wyraz, ilosc in ilosc.items():
    print(wyraz , ":", ilosc)

#print("suma wszystkich wyrazów to: ", len(ilosc))

print(f"Łączna liczba słów: {len(tekst1.split())}")