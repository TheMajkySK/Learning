n = int(input("Zadaj číslo: "))
for r in range(1, n + 1):
    for i in range(1, n + 1):
        print(r * i, end=" ")
    print()
print()
input("Stlač ENTER pre ukončenie programu")