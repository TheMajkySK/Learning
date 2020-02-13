"""
Napíšte program, ktorý vygenerujte všetky päťciferné palindromy (t. j. čísla, ktoré majú cifru na miesta desaťtisícok rovnakú ako na
mieste jednotiek a cifru na mieste tisícok rovnakú ako na mieste desiatok napr. 52125 ) a zapíše ich do textového súboru D:\maturita\palindr.txt, každý na jeden riadok.
"""
pal = 99999
erst = 999
print(pal)
while pal != 10001:
    temp = ""
    erst -= 1
    temp = str(erst)
    temp = temp + temp[1] + temp[0]
    pal = int(temp)
    print(pal)