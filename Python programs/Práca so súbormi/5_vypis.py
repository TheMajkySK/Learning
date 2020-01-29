"""
vypisat slova pdo seba
kolko je tam riadkov, slov, znakov
"""
from codecs import open
subor = open("xd.txt", "r", "utf-8") #pomocou importu open z codecs mi to pridalo argument na urcenie danej tabulky znakov(ASCII, UUTF-8,...)
p_slov = 0
p_riadkov = 0
p_znakov = 0
while True:
    r = subor.readline()
    p_znakov += len(r)-1
    if len(r) == 0:
        break
    r = r.strip()   #odstrani medzery na zaciatku a konci retazca, musi to byt priradene pre premennu lebo r.strip nemeni danu premennu r, on ju iba akoby nacita do novej premennej a uz bez medzier
    slova = r.split(" ")  #rozdeli na rezazce - deliaci znak bude medzera
    for slovo in slova:
        if len(slovo) > 0:
            if slovo[-1] in {",", ".", ":", ";", "?", "!"}:
                slovo.replace(slovo[-1], "")
            p_slov += 1
            print(slovo)
print("Počet slov:", p_slov)
print("Počet znakov:", p_znakov)