"""
1. funkcia na vypocet obsahu obdlznika zo str. a,b
2. vypocet obsahu plochy pod grafom nejakej funkcie na intervale <x1, x2>
"""
"""
def Sobd(a,b):
    return a*b
print(Sobd(5,9))
"""
def f(x):
    return (x**2)+2
S = 0
a = 1
b = 3
dx = 0.00001
x = a
while x <= b:
    S += f(x)*dx
    x += dx
print(S)