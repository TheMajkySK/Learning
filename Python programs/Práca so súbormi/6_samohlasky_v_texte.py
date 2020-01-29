"""
kolkokrat je v texte samohlaska
"""

subor = open("xd.txt", "r")

p_sam = 0
while True:
    r = subor.readline()
    if len(r) == 0:
        break
    if r in {"a","e","i","o","u"}:
        p_sam += 1
print("Počet samohlasok:", p_sam)