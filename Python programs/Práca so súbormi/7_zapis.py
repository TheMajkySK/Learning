"""
pomocou "w" zapisujeme
"""
from codecs import open

subor1 = open("zoznam.txt", "w", "utf-8")
subor1.write("Ahoj")
subor1.close()