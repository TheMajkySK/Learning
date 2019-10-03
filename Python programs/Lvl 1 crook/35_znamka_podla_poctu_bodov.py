max_pocet = int(input("Zadaj maximálny počet bodov: "))
ziskany_pocet = int(input("Zadaj získaný počet bodov: "))
percenta = ((ziskany_pocet / max_pocet) * 100)
if percenta >= 89:
    print("Máš 1")
elif percenta >= 75:
    print("Máš 2")
elif percenta >= 50:
    print("Máš 3")
elif percenta >= 35:
    print("Máš 4")
elif percenta < 35:
    print("Máš 5")