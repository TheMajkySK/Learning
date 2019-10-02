a = int(input("Zadaj celé číslo a ja ti vypíšem všetky čísla deliteľné 7 a 11: "))
for i in range(2, a + 1, 2):
    if (i % 7 == 0) and (i % 11 == 0):
        print(i)