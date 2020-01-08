import random

def druhe_najmensie(cis):
    m1, m2 = float('inf'), float('inf')
    for x in cis:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2


cislo = 0
nahodne_cisla = []
for i in range(20):
    cislo = random.randint(1,1000)
    nahodne_cisla.append(random.randint(1,1000))
print(nahodne_cisla)
print(druhe_najmensie(nahodne_cisla))