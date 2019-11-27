"""
vstup - uživatel zada vetu
vystup - zasifrovana veta tak ze za kazde pismeno vo vete sa vlozi nahodne vyhenerovany znak a vsetko zmenime na velke pismena
"""
import random
veta = input("Zadaj vetu pre šifrátor: ")
veta = veta.upper()
dlzka_vety = len(veta)
for i in range(dlzka_vety):
    znak = random.randint(65,90)
    print(veta[i] + chr(znak), end="")