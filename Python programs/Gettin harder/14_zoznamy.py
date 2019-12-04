"""
zoznamy(list)
Zoznam je strukturovany datovy typ, ktory obsahuje postupnost dat rozneho typu.
Je to menitelny typ, tzn. mozeme zmenit hodnotu konretneho prvku pomocou indexu.
K jednotlivym polozkam zoznamu pristupujeme cez indexy v hranatych zatvorkach.
V inych prog. jazykoch je podobny typ, krory sa nazyva pole, ale polozky pola su rovnakeho typu.
Zo stringu vieme urobit zoznam
"""
cisla = [8,12,5,-3.5,-8]
print(cisla[2])   #čisluje s a od 0
clovek = ["Stivi", 18, "december", 1975, 43.9]
print(clovek[0])
s = "Jano"
z = list(s)
print(z)
for i in range(len(s)):
    print(z[i], end=" ")
    print()


veta = "Dnes je streda, 4.december 2019"
slova_vo_vete = veta.split()
print(slova_vo_vete)
print(slova_vo_vete[2])
slova_vo_vete[2] = "štvrtok"
print(slova_vo_vete)