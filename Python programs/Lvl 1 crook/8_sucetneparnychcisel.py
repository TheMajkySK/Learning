n = int(input("Zadaj číslo na výpocet súčtu nepárnych čísel: "))
sucet = 0
for i in range(0, n, 2):
    sucet = sucet + 1
    print(i, end = " ")
print(f"\nSúčet nepárnych čísel od 1 do {n} je: {sucet}")
print()
input("Press ENTER to close program")