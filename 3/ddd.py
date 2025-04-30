
text = input("podaj długi tekst: ")

wyrazy = []

for w in text.split(" "):
    if len(w) > 0:
        wyrazy.append(w)

for i, wyraz in enumerate(wyrazy):
    print(f"{i+1}: {wyraz}")
