from codecs import open

s = open("ziaci.txt", "r", "utf-8")
print("Mená dospelých:")
for l in s:
    l = l.strip()
    sl = l.split(" ")
    if int(sl[0]) >= 18:
        print(sl[1])
print()