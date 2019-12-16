import random

def druhe_najmensie(cis):
    prvy = cis[0]
    druhy = cis[1]

    for c in cis:
        if c < prvy:
            druhy = prvy
            prvy = c

    return druhy





cislo = 0
nahodne_cisla = []
for i in range(20):
    cislo = random.randint(1,1000)
    nahodne_cisla.append(random.randint(1,1000))
print(nahodne_cisla)
print(druhe_najmensie(nahodne_cisla))