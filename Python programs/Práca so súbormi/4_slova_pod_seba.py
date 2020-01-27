"""
napiste vsetky slova z textaku do shellu pod seba
"""
subor = open("xd.txt", "r")

while True:
    r = subor.readline()
    if len(r) == 0:
        break
    r.strip()   #odstrani medzery na zaciatku a konci retazca
    slova = r.split(" ")  #rozdeli na rezazce - deliaci znak bude medzera
    for slovo in slova:
        print(slovo)