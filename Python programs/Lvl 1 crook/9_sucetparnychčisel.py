sucet = 0
n = 1001
for i in range(2, n, 2):
    sucet = sucet + i
    print(i, end = " ")
print(f"Súčet párnych čísel od 1 po {n} je: {sucet}")
print()
input("Press ENTER to close program")