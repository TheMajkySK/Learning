def sucet_slova(veta):
    dlzka = len(veta)
    sucet = 0
    for i in range(dlzka):
        x = veta[i]
        znak = ord(x)
        sucet += znak
    return sucet

veta = str(input("Zadaj vetu na spocitanie znakov: "))
dlzka = len(veta)
medzera = ord(" ")
index = 0
suc_komp = 0
for i in range(dlzka):
    pismeno = veta[i]
    znak = ord(pismeno)
    if znak != medzera:
        index += 1
    elif znak == medzera:
        suc_komp += sucet_slova(veta[0:index])
print(suc_komp)