from codecs import open

b = open("basen.txt", "r", "utf-8")
cp = open("kopia.txt", "w", "utf-8")

slovo = input("Zadaj slovo: ")

for l in b:
    if len(l.strip()) == 0:
        cp.write(slovo + "\n")
    else:
        cp.write(l)

b.close()
cp.close()