subor = open("xd.txt", "r")


while True:
    r = subor.readline()
    d = len(r)
    if d == 0:
        break
    print(r)
    print("dlzka riadka:", d)