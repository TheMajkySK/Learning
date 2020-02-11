"""
Napíšte program, ktorý vygeneruje a vypíše postupnosť 50 celých čísel z intervalu 
<-7000, 7000>, potom vypíše všetky záporné čísla z postupnosti na obrazovku a do textového súboru d:\maturita\zaporne.txt.
"""
import random
from codecs import open

z = []
for i in range(50):
    z.append(random.randint(-7000,7000))

for i in range(len(z)):
    print(z[i], end=", ")
print()
print()
print("Záporné čísla:", end=" ")

txt = open("d:\maturita\zaporne.txt", "w", "utf-8")
for i in range(len(z)):
    if z[i] < 0:
        print(z[i], end=", ")
        txt.write(str(z[i]) + " ")
txt.close()