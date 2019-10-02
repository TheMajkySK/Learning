n = int(input("Zadaj počet riadkov: "))
for r in range(1, n + 1):
    for m in range(1, n - r + 1):
        print(" ", end = "")
    for h in range (1, r + 1):
        print("*", end="")
    print()
print()
input("Stlač ENTER pre ukončenie programu")