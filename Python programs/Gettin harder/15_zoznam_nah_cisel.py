"""
vytvorte zoznam nahodnych cisel z intervalu od 1 po 1000, 20 prvkovy zoznam
"""
import random
cislo = 0
#nahodne_cisla = [0]*20      # * viacnasobne zopakuje obsah premennej do novej struiktury
nahodne_cisla = []
for i in range(20):
    cislo = random.randint(1,1000)
    #nahodne_cisla[i] = cislo
    nahodne_cisla.append(random.randint(1,1000))    # .append prida hodnotu na koniec
print(nahodne_cisla)