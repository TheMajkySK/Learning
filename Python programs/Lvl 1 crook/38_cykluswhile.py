"""
počítač vygeneruje číslo z intervalu prirodzené číslo od <1, 100>,
uživatel ho bude hádať
"""
import random

nahodne_cislo = random.randint(1, 100)
print("Budeš hádať číslo na ktoré myslím")
print("Zadaj číslo v intervale <1, 100> a ja ti poviem či je väčšie alebo menšie než to na ktoré myslím: ", end="")
cislo = 0
pocet = 0
while cislo <= nahodne_cislo or cislo >= nahodne_cislo:
    cislo = int(input())
    if cislo < nahodne_cislo:
        print("Zadaj väčšie číslo: ", end="")
        pocet += 1
        continue
    elif cislo > nahodne_cislo:
        print("Zadaj menšie číslo: ", end="")
        pocet += 1
        continue
    elif cislo == nahodne_cislo:
        print("Jes ma men uhadol si xD")
        pocet += 1
        break
print(f"Dal si to na {pocet} pokusov")
if pocet == 1:
    print("Ta ty ši iny šef jako")
elif pocet <= 5:
    print("Pjekneeeeeeee")
elif pocet <= 10:
    print("Ta jako neši až taky plany")
elif pocet <= 15:
    print("Zamysli sa nad svojim životom prosím")
elif pocet <= 20:
    print("Možeš rovno skočiť z okna")
print()
input("Stlač ENTER pre ukončenie programu")