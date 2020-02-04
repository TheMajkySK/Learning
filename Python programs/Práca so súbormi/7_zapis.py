"""
pomocou "w" zapisujeme
"""
from codecs import open

subor1 = open("zoznam.txt", "w", "utf-8")
subor1.write("Ahoj\n")
subor1.write("maturanti")
#subor1.close() - vo visual studio code to netreba