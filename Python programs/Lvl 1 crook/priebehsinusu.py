import math

for uhol in range(0, 361, 10):
    uhol_v_radianoch = math.radians(uhol)
    sin_uhla = math.sin(uhol_v_radianoch)
    stlpec = int(sin_uhla * 35 + 40)
    print(" " * stlpec + "SIN")
print()
input("Stlač ENTER pre ukončenie programu")