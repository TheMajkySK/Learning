# === Úloha 2===
# Napíšte program, ktorý  nájde v súbore vzor.txt najdlhšie slovo, vypíše ho a vypíše aj číslo riadka, na ktorom sa nachádza.
from codecs import open

subor = open("vzor.txt", "r", "utf-8")
riadky = subor.readlines()

najdlhsie_slovo = ""
riadok_najdlhsieho = 0

for i in range(len(riadky)):
    s_riadky = riadky[i].strip()
    slova = s_riadky.split(" ")

    for slovo in slova:
        if len(slovo) >= len(najdlhsie_slovo):
            najdlhsie_slovo = slovo
            riadok_najdlhsieho = i+1

print(f"Najdlhšie slovo je {najdlhsie_slovo}")
print(f"Je na riadku {riadok_najdlhsieho}")