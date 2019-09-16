n = int(input("Zadaj faktoriál: "))
f = 1
for i in range(1, n+1):
    f = f * i
print(f"{n}! = {f}")
print()
input("Press ENTER to close program")