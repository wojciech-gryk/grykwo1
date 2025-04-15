text = "This is text"

print("text:", text, type(text))
print(text.upper())
print(text.lower())
print(text.count(("t")))

new_text = text.lower()
print(new_text.count("t"))
#skrót
print(text.lower().count("t"))
