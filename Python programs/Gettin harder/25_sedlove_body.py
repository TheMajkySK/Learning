"""
najdite sedlove body a vypiste ich, sedlovy bod je najmensi v riadku a sucasne najväčší v stlpci
"""
import random

n = 4
z = []
for i in range(n):
    z.append([0] * n)
z[0] = [1,0,4,8]
z[1] = [7,4,9,7]
z[2] = [3,2,1,4]
z[3] = [20,5,10,7]
for i in range(n):
    for j in range(n):
        print(z[i][j], end=" ")
    print()

for r in range(n):
    smin = z[r].index(min(z[r]))
    test = True
    for s in range(n):
        if z[r][s] > z[r][smin]:
            test = False
            break
    if test:
        print("Sedlovy bod:", z[r][smin], "je na pozícii", r,smin)