from decimal import *
getcontext().prec = 2

a = 0.1
b = 0.1
c = 0.1

ad = round(Decimal(0.12),2)
bd = Decimal(0.12)
cd = Decimal(0.12)
wynik = ad + bd + cd

print(ad, bd, cd, wynik)

