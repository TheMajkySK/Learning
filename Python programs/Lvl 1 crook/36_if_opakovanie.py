b = int(input("Zadaj číslo: "))
sucet = 0
print("Delitele: ")
for i in range(1, b + 1):
    if b % i == 0:
        print(f"{i}")
        sucet += i
print(f"Sučet delitelov je {sucet}")