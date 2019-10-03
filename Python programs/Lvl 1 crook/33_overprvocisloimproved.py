import math

n = int(input("Zadaj číslo: "))
pocet_delitelov = 0
for i in range(2, (round(math.sqrt(n))+0)):
    if n % i == 0:
        pocet_delitelov += 1
if pocet_delitelov == 0:
    print(f"Cislo {n} je prvočíslo")
else:
    print(f"Cislo {n} nie je prvočíslo") 