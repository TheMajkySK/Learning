"""
.readline - funkcia vrati znakovy retazec - precitany riadok aj s koncovym znakom "\n"
"""

subor = open("xd.txt", "r")


r = subor.readline()
print(r)
print("dlzka riadka:", len(r))
r = subor.readline()
print(r)
print("dlzka ridaka:", len(r))
r = subor.readline()
print(r)
print("dlzka ridaka:", len(r))
r = subor.readline()
print(r)
print("dlzka ridaka:", len(r))
r = subor.readline()
print(r)
print("dlzka ridaka:", len(r))