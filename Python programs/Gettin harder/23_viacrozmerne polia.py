import random

z = [["pes", "mačka", "mačkopes"], [5,6,7], ["Neviem", "Viem", "Neviemviem"]]
for i in range(len(z)):
    print(z[i][i])

print()

for i in z:
    print(i[0])

zoz = [[0] * 5] * 5
print(zoz)

n = 4
z = [[0] * n] * n

z = []
z1 = []
for i in range(n):
    z1.clear()
    for j in range(n):
        z1.append(random.randint(2,100))
    print(z1)
    z.append(z1)
    print("z", z)

for i in range(n):
    for j in range(n):
        print(z[i][j], end=" ")
    print()

z = [0 for i in range(3)]
print(z)
z = [i for i in range(3)]
print(z)
z = [i*2 for i in range(3)]
print(z)