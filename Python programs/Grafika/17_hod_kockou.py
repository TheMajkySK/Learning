import random

def hod_kockou():
    a = random.randint(1,6)
    b = random.randint(1,6)
    c = a + b
    return c


poc9 = 0
poc8 = 0
poc11 = 0
for i in range(100000):
    if hod_kockou() == 8:
        poc8 += 1
    elif hod_kockou() == 7 :
        poc9 += 1
    elif hod_kockou() == 6:
        poc11 += 1
print(f"Sučet 8 bol vygenerovaný {poc8}-krát, 7: {poc9}-krát, 6: {poc11}-krát")