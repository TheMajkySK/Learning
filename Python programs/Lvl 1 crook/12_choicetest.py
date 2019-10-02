import random

slovo = ""
for i in range(3):
    spoluhlaska = random.choice("bcdfghjklmnpqrstvwxz")
    samohlaska = random.choice("aeiouy")
    slovo = slovo + spoluhlaska + samohlaska
print(slovo)
print()
input("Stlač ENTER pre ukončenie programu")