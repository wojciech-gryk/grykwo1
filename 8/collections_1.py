#from email.policy import default
from collections import defaultdict

zdanie = "ala ma kota kot ma ale ale ala nie ma kota"

slownik = {}

for wyraz in zdanie.split(" "):
    if wyraz in slownik:
        slownik[wyraz] += 1
    else:
        slownik[wyraz] = 1

print(slownik)

def nowa_liczba():
    return 0

slownik2 = defaultdict(nowa_liczba)

for wyraz in zdanie.split(" "):
    slownik2[wyraz] += 1

print(slownik2)

