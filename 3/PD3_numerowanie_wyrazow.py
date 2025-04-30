# Napisz program, który wczyta od użytkownika fragment tekstu.
# Podziel ten tekst na wyraz (warto skorzystać z tego, co dostarcza python)
# Wydrukuj wszystkie wyrazy razem z numerem porządkowym wyrazu w ciągu znaków.

# przykład
# użytkownik wpisał "ala ma kota"
# program powinien wyświetlić
# 1: ala
# 2: ma
# 3: kota

# Dokumentacja przydatna do zadania:
# https://docs.python.org/3.12/library/stdtypes.html#textseq
# oraz
# https://www.w3schools.com/python/python_ref_string.asp

tekst = input("wprowadź tekst z kilku wyrazów: ")
tekst1 = ' '.join(tekst.split())

slowa = tekst1.split(sep=" ")
i = 0

for i, wyraz in enumerate(slowa):
    print(i + 1, ":", wyraz)
