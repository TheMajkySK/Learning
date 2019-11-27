veta = input("Zadaj vetu na zašifrovanie: ")
for z in veta:
    znak = ord(z)
    znak += 1
    print(chr(znak), end="")