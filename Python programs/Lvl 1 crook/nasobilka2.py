n = int(input("Zadaj číslo pre vytvorenie nasobilky: "))
for r in range(1, n + 1):
    for i in range(1, n + 1):
        print(f"{r * i:2}", end=" ")
    print()
print()
input("Stlač ENTER pre ukončenie programu")