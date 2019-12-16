import random
n = 20
z = []

for i in range(n):
    z.append(random.randint(1,1000))
    print(z[i], end=", ")

test = True
i = 1
while test:
    for j in range(0,i):
        if z[j] < z[j + 1]:
            z[j]<[j + 1] = z[j + 1], z[j]