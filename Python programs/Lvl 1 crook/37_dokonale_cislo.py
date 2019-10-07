"""
Dokonalé číslo má súčet vsetkych delitelov mensich ako dane cislo rovný danému číslu
"""
b = int(input("Zadaj číslo: "))
for cislo in range(1, b + 1):
    sucet = 0
    for j in range(1, cislo):
        if cislo % j == 0:
            sucet += j
    if sucet == cislo:
        print(f"Číslo {cislo} je dokonalé číslo")
    else:
        print(f"Číslo {cislo} nie je dokonalé číslo")