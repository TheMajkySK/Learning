n = int(input("Zadaj číslo: "))
pocet_delitelov = 0
for i in range(2, n):
    if n % i == 0:
        pocet_delitelov += 1
if pocet_delitelov == 0:
    print(f"Číslo {n} je prvočíslo")
else:
    print(f"Číslo {n} nie je prvočíslo")