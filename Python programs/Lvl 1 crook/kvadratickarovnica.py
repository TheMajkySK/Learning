import math

a = float(input("Zadaj a = "))
b = float(input("Zadaj b = "))
c = float(input("Zadaj c = "))
D = b ** 2 - (4 * a * c)
"""
if D < 0:
    print("Kvadratická rovnica nemá riešenie")
else:
    if D == 0:             # = je priradovaci prikaz, == sa pouziva na porovnavanie
        print("Kvadratická rovnica má jedno riešenie v R")
        x1 = -b/(2*a)
        print(f"x1 = {x1:6.3f}")
    else:
        print("Kvadratická rovnica má 2 riešenia v R")
        x1 = (-b + math.sqrt(D))/(2*a)
        x2 = (-b - math.sqrt(D))/(2*a)
        #print(f"x1 = {x1:6.3f}")
        #print(f"x2 = {x2:6.2f}")
        print("Prvé riešenie je{:5.2f}, druhé riešenie je{:6.2f}".format(x1, x2))
"""
if D < 0:
    print("Kvadratická rovnica nemá riešenie")
if D == 0:             # = je priradovaci prikaz, == sa pouziva na porovnavanie
        print("Kvadratická rovnica má jedno riešenie v R")
        x1 = -b/(2*a)
        print(f"x1 = {x1:6.3f}")
if D > 0:
    print("Kvadratická rovnica má 2 riešenia v R")
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D))/(2*a)                       #TENTO POSTUP JE NEEFEKTÍVNY LEBO AJ KED PRVÉ IF NIEJE PRAVDA BUDE POROVNÁVAŤ DALEJ
    #print(f"x1 = {x1:6.3f}")
    #print(f"x2 = {x2:6.2f}")
    print("Prvé riešenie je{:5.2f}, druhé riešenie je{:6.2f}".format(x1,x2))
print()
input("Stlač ENTER pre ukončenie programu")