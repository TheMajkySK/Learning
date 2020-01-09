"""
vygenerujte rastucu postupnost cisel
uzivatel zada cislo a program vlozi to cislo do vygenerovanej rastucej postupnosti a zaradi ho na taku poziciu aby vysledna postupnost bol tiez rastuca
"""
import random

rast = []
n=20
rast.append(random.randint(1,5))

for i in range(1,n):
    rast.append(random.randint(1,5) + rast[i-1])
for i in range(n):
    print(rast[i], end=", ")
print()
nove = int(input("Zadaj číslo: "))
i = 0

while i < len(rast):
    if rast[i] > nove:
        break
    i+=1
rast.insert(i,nove)
for i in range(len(rast)):
    print(rast[i], end=", ")