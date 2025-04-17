# Napisz program który poprosi użytkownika o liczbę (załóż, że poda prawidłową)
# Zapisz tą liczbę w postaci int w zmiennej, następnie porównaj go z wartością zmiennej
# "magiczna_liczba". Sprawdź, czy liczba jest większa, mniejsza a może równa magicznej liczbie?

m_liczba = 10
liczba = int(input("podaj jakąs liczbę: "))

if liczba == m_liczba:
    print("liczby są identyczne")
elif liczba > m_liczba:
    print("podana liczba jest większa od \"magicznej liczby\" ")
else:
    print("podana liczba jest mniejsza od \"magicznej liczby\" ")

