"""
vstup - číslo
výstup - prvociselny rozklad čísla
c = 56
56|2
28|2
14|2
 7|7
 1|
"""
cislo = int(input("Zadaj číslo a ja ho rozložím na prvočísla: "))
p = 2
while cislo > 1:
    if cislo % p == 0:
        if cislo <= 1:
            print(p)
        else:
            print(p, end="*")
            cislo //= p
    else:
        p += 1