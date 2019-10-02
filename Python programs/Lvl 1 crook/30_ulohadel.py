#všetky parne delitelne 14 a nesudelitelne 11
for i in range(11, 101, 1):
    if i % 2 == 0 and i % 13 != 0:                     # != !-not, sa nerovná 
        print(i)                  