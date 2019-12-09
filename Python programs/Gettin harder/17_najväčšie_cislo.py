import random

def najmensie(cis):
    maxim = cis[0]
    for i in range(len(cis)):
        x = cis[i]
        if x > maxim:
            maxim = x
    return maxim





cislo = 0
nahodne_cisla = []
for i in range(20):
    cislo = random.randint(1,1000)
    nahodne_cisla.append(random.randint(1,1000))
print(nahodne_cisla)
print(najmensie(nahodne_cisla))