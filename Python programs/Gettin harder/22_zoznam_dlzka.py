"""
program vygeneruje postupnost reťazcov nahodenj dlzky z intervalju (1,20)
vytvorte funkciu ktora bude mat ako parameter dany zoznam
vystup funkice bude novy zoznamktory bude obsahovat dlzky stringov ktory bude obsahovať dlžky stringov daneho zoznamu
"""
import random

def nahodne_slovo():
    dlzka = random.randint(1,15)
    slovo = ""
    for i in range(dlzka):
        if random.choice([True, False]):
            slovo += chr(random.randint(65,90))
        else:
            slovo += chr(random.randint(97,122))
    return slovo

def dlzky(zoz):
    zoznam = []
    for i in range(len(zoz)):
        zoznam.append(len(zoz[i]))
    return zoznam

n = 10

zoznam = []
for i in range(n):
    zoznam.append(nahodne_slovo())
print(zoznam)
z = dlzky(zoznam)
print(z)
mhod = max(z)
p = 0
izoz = []
for i in range(len(z)):
    if mhod != z[i]:
        p += 1
    elif mhod == z[i]:
        break
print(zoznam[p])