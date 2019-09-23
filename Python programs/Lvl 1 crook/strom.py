n = int(input("Zadaj počet riadkov: "))
for r in range(1, n+1):
    print(" "*(n-r) + "* " * r)
print()
input("Stlač ENTER pre ukončenie programu")