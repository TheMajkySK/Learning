n = int(input("Zadaj číslo na výpocet súčtu nepárnych čísel: "))
sucet = 0
for i in range(1, n, 3):
    sucet = sucet + 1
    print(i, end = " ")
print(f"Súčet nepárnych čísel od 1 do {n} je: {sucet}")
print()
input("Press ENTER to close program")