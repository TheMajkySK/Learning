import math
a = float(input("Zadaj stranu a: ")) #pretypovanie hodnoty a na float
b = float(input("Zadaj stranu b: ")) #pretypovanie hodnoty b na float
x = a**2+b**2
c = math.sqrt(x)
print("Prepona je ", c)
print()
input("Pre ukončenie stlač ENTER")