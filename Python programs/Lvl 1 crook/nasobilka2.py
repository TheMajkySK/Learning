n = int(input("Zadaj číslo pre vytvorenie nasobilky: "))
x = 0
m = " "
for i in range(1, n + 1):
    x += 1
    print(f"{m:3}", end="")
    print(f"{x:3}", end="")
print()
x = 0
for r in range(1, n + 1):
    x += 1
    print(f"{x:3}", end="")
    for i in range(1, n + 1):
        print(f"{r * i:3}", end=" ")
    print()
print()
input("Stlač ENTER pre ukončenie programu")