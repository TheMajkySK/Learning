"""
na pridavanie pozuivame "a" ako append
"""
from codecs import open

subor1 = open("zoznam.txt", "a", "utf-8")

subor1.write("\n")
meno = str(input("Zadaj meno: "))
mesto = str(input("Zadaj mesto: "))
adresa = str(input("Zadaj adresu: "))
psc = str(input("Zadaj PSČ: "))
subor1.write("Meno: " + meno + "\n")
subor1.write("Mesto: " + mesto + "\n")
subor1.write("Adresa: " + adresa + "\n")
subor1.write("PSČ: " + psc + "\n")
subor1.close()