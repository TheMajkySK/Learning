a = int(input("Zadaj od: "))
b = int(input("Zadaj po: "))
print("Postupnosť je", end=" ")
for i in range(a, b + 1):
    print(i, end=" ")
print()
input("Stlač ENTER pre ukončenie programu")