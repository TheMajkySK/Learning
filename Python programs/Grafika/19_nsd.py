"""
vytvorte funkciu NSD(A,B) - najväčší spoločný deliteľ

NSD(132, 56)

132 = 56*2 + 20
56 = 20*2 + 16
20 = 16*1 + 4
16 = 4*4 + 0
"""
def NSD(a, b):
    zvysok = 1
    while zvysok > 0:
        zvysok = a % b
        a = b
        b = zvysok
    return a

c1 = int(input("Zadaj prvé číslo: "))
c2 = int(input("Zadaj druhé číslo: "))

print(f"Najväčším spolocným deliteľom čísla {c1} a čísla {c2} je {NSD(c1, c2)}")