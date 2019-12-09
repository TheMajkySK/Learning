import random

def druhe_najmensie(cis):
    minim = cis[0]
    pocet = 0
    zoz = [0]
    for i in range(len(cis)):
        x = cis[i]
        if x < minim:
            minim = x
            zoz.append(minim)
        y = len(zoz)-1
    return zoz[y], minim





cislo = 0
nahodne_cisla = []
for i in range(20):
    cislo = random.randint(1,1000)
    nahodne_cisla.append(random.randint(1,1000))
print(nahodne_cisla)
print(druhe_najmensie(nahodne_cisla))