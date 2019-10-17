"""
každé dalšie číslo v postupnosti je súčtom 2 predchádzajúcich
program ktory najde najväčšie fibonaciho cislo ktore nieje väčšie ako 1 000 000
"""
a1 = 0
a2 = 1
a3 = 0
while a3 < 1000000:
    a3 = a1 + a2
    a1 = a2
    a2 = a3
print(a3)