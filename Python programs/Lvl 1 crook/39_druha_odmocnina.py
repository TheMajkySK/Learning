"""
zistite druhu odmocninu cisla x bez 
volania funkcie math.sqrt(x)
"""
cislo = int(input("Zadaj číslo na odmocnienie: "))
a = 0
while a**2 < cislo:
    a += 0.01
print(f"Druhá odmocnina čísla {cislo} = {a}")