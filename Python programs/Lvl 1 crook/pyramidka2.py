pocet = int(input("Zadaj počet riadkov: "))
cislo = 1
for riadok in range(1, pocet + 1):
    for stlpce in range(1, riadok + 1):
        print(cislo, end=" ")
        cislo += 1
    print()
print()
input("Stlač ENTER pre ukončenie programu")