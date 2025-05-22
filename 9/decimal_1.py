from decimal import *
from types import prepare_class
getcontext().prec = 2

a = Decimal(0.1)
b = Decimal(0.1)
c = Decimal(0.1)
wynik = a + b + c

print(wynik)

