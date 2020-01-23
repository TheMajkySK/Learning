z = []
n = 5
m = 3

for i in range(n):
    z.append([0]*m)

z[0] = [1,2,5]
z[1] = [3,4,7]
z[2] = [6,8,9]
z[3] = [1,2,5]
z[4] = [3,4,7]

for i in range(n):
    for j in range(m):
        print(z[i][j], end=" ")
    print()

print()

d = (z[0][0]*z[1][1]*z[2][2]) - (z[0][2]*z[1][1]*z[2][0]) + (z[1][0]*z[2][1]*z[3][2]) - (z[1][2]*z[2][1]*z[3][0]) + (z[2][0]*z[3][1]*z[4][2]) - (z[2][2]*z[3][1]*z[4][0])
print("Determinant je:", d)