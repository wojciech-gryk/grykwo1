text = "This is text"

print(text[0:4])
print(len(text))

text2 = "0123456789"
print(text2[0:4])
#print(text2[4:8]) #nie działa - dopytać czemu

typ = type(text2)
print(typ)
print(typ[6:-2])


if len(text) < 12:
    print("krótszy niż 12")
elif len(text) > 12:
    print("dłuższy niż 12")
else:
    print("idealnie 12")
