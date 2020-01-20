"""
vygenerujte dvojrozmerne pole ktore bude mat len 0 a 1, uživatel zada suradnice a ked tam je 0 tak to zmeni na 1 a naopak
"""
import random

z = []
n = 4
for i in range(n):
    z.append([0]*n)
z[0] = [0,1,1,0]
z[1] = [1,0,0,1]
z[2] = [0,1,0,1]
z[3] = [0,0,1,0]
for i in range(n):
    for j in range(n):
        print(z[i][j], end=" ")
    print()
x = int(input("Zadaj suradnicu x:"))
y = int(input("Zadaj suradincu y:"))
if z[x][y] == 0:
    z[x][y] = 1
elif z[x][y] == 1:
    z[x][y] = 0
for i in range(n):
    for j in range(n):
        print(z[i][j], end=" ")
    print()