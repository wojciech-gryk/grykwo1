# Rozwiń program z zadania 04 tak, aby radził sobie prawidłowo z wieloma spacjami pomiędzy wyrazami
# oraz wieloma spacjami na początku i końcu tekstu

tekst = input("wprowadź tekst z kilku wyrazów: ")
tekst1 = ' '.join(tekst.split())

slowa = tekst1.split(sep=" ")
i = 0

for i, wyraz in enumerate(slowa):
    print(i + 1, ":", wyraz)