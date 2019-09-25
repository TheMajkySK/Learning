n = int(input("Zadaj počet riadkov: "))
for r in reversed(range(1, n + 1)):
    for m in range(0, n - r + 1):
        print(" ", end=" " )
    for h in range(1, r + 1):
        print("* ", end="")
    print()
print()

for r in reversed(range(0, n + 1)):   #skrateny zapis sa vypise rychlejsie 
    print("  " * (n-r) + "* " * r)    # a zabera menej pamäte

print()
input("Stlač ENTER pre ukončenie programu")