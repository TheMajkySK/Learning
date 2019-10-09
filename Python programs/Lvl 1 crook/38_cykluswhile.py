"""
počítač vygeneruje číslo z intervalu prirodzené číslo od <1, 100>,
uživatel ho bude hádať
"""
import random

nahodne_cislo = random.randint(1, 100)
print("Budeš hádať číslo na ktoré myslím")
cislo = int(input("Zadaj číslo a ja ti poviem či je väčšie alebo menšie než to na ktoré myslím: "))
pocet = 1
while cislo == nahodne_cislo: