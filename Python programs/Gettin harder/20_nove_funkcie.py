"""
insert() - prida prvok na dane miesto v zozname
pop() - vymaže prvok podla indexu zo zoznamu
remove() - vymaže prvok podla hodnoty
del() - vymaže podla indexu, alebo vymaže celý zoznam
"""
zoznam = ["pomaranč", "jablko", "zemiak", "mrkva"]
print(zoznam)
zoznam.insert(1, "xD")
print(zoznam)
zoznam.pop(3)
print(zoznam)
zoznam.remove("jablko")
print(zoznam)
del zoznam[0]
print(zoznam)
del zoznam #vymaže cely zoznam čiže ak ho dame vypisat dostaneme error
#print(zoznam)
zoznam = ["modra", "cervena", "zelena", "zlta"]
zoznam.clear()
print(zoznam)
zoznam = ["modra", "cervena", "zelena", "zlta"]
"""
ak dam zoznam = zoz
tak ak zoznam[2] = jablko, tak sa to nezmeni len v zoname(zoznam) ale aj v zozname(zoz) lebo je to len akoby odkaz zonamu v zoz
kopiu robíme pomocou funkcie copy()
"""
zoz = zoznam.copy()
print(zoz)
zoz2 = list(zoznam)
print(zoz2)
zoz3 = zoz + zoz2
print(zoz3)
zozx = ["neviem", "čo", "mam", "napisať"]
for x in zozx:
    zoz3.append(x)
print(zoz3)
zoz3.extend(zozx)
print(zoz3)
