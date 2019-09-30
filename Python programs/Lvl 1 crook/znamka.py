#program ma načiat max počet bodov z testu potom získaný počet bodov
#program vypočita percentualná testu a zistí či žiak dostal 5ku
mx = int(input("Zadaj maximálny počet bodov: "))
n = int(input("Zadaj počet získaných bodov: "))
x = (n / mx) * 100
if x >= 30:
    print("Známka je lepšia ako 5")
else:
    print("Známka je 5")
print()
input("Stlač ENTER pre ukončenie programu")