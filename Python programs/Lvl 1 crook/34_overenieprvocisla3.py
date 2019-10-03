import math

n = int(input("Zadaj číslo: "))
pocet_deliteliov = 0
for i in range(2, (round(math.sqrt(n))+ 1)):
    if n % i == 0:
        pocet_deliteliov += 1
    if pocet_deliteliov == 1:
        break
if pocet_deliteliov == 0:
    print(f"Cislo {n} je prvočíslo")
else:
    print(f"Cislo {n} nie je prvočíslo")