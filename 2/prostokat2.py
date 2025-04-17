bok_a = int(input("podaj długośc boku a: "))
bok_b = int(input("podaj długośc boku b: "))

if bok_a == bok_b:
    obiekt = "kwadratu"
else:
    obiekt = "prostokąta"

print(" pole ", obiekt, " : ", bok_a * bok_b, "\n", "obwód " , obiekt, " : ", 2*bok_a + 2*bok_b)