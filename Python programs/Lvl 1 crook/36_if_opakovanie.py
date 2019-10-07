b = int(input("Zadaj číslo: "))
print("Delitele: ")
for i in range(1, b + 1):
    if b % i == 0:
        print(f"{i}")