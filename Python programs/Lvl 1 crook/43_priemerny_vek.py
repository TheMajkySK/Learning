"""
Napíšte program ktory bude od pouzivatela pytat vek a zadavanie ukonci 0.
Vypočítaj priemerny vek zo zadanych vekov.
"""

vek = int(input("Zadaj vek: "))
sucetv = vek
pocet = 1
while vek > 0:
    sucetv += vek
    pocet += 1
    vek = int(input("Zadaj vek: "))
priemer = sucetv / pocet
print(f"Priemer zadaných vekov je {priemer}")