"""
8 miestne heslo pozostavajuce z malych znakov
"""
import random
for i in range(8):
    a = random.randint(ord("a"), ord("z"))
    print(chr(a), end="")