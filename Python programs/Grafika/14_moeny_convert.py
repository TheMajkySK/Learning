"""
funkcia ktora prevedie CZK na EUR
kurz 25,5 CZK za 1 EUR
"""
def prevod(CZK):
    EUR = round(CZK/25.5, 2)
    return EUR
suma = float(input("Zadaj pocet CZK pre konvertovanie na EUR: "))
print(prevod(suma))