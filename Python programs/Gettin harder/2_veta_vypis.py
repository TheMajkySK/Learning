"""
uživatel zada nejaku vetu a program vypise tu veto do riadku pod seba kazdym pismenom
funkcia len() nam zisti kolko znakov sa nachaddza v znakovom retazci
aky index ma posledny znak v zadanom reťazci ak jeho dlzka je l
"""
veta  = str(input("Zadaj vetu a ja ti ju napisem pod seba do riadku: "))
"""
dlzka_retazca = len(veta)
for i in range(dlzka_retazca):
    print(veta[i])
"""
#ZJEDNODUŠENIE
for i in range(len(veta)):
    print(veta[i])