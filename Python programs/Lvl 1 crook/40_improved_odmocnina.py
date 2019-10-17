cislo = float(input("Zadaj číslo pre výpočet odmocniny: "))
od = 1
do = cislo
a = 0
pocitadlo = 0
while abs(cislo-a**2) > 0.001:
    pocitadlo += 1
    if a**2 == cislo:
        break
    a = (od + do) / 2
    if a**2 > cislo:
        do = a
    else:
        od = a
    a = (od + do) / 2
print(f"Druhá odmocnina {cislo} = {a}")
print(f"Cyklus prebehol {pocitadlo}-krát")