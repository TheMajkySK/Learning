import math

for uhol in range(0, 91, 5):
    uhol_v_radianoch = math.radians(uhol)
    sinus_uhla = math.sin(uhol_v_radianoch)
    cosinus_uhla = math.cos(uhol_v_radianoch)
    print(f"Uhol={uhol} sin={sinus_uhla} cos={cosinus_uhla}")
print()
input("Stlač ENTER pre ukončenie programu")