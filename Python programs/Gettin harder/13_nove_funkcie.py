"""
dalsie funkice:
s.count(b) - pocet vyskytov podretazca b v retazci s
s.find(b) - výstup bude index prveho vyskytu podrezaca b v retazci s
strip(veta) - odstrani medzery na začiatku a na konci retazca a tie aj ine oddelovace, napr. /n
z = split(s) - rozdeli retazec na casti podla uvedeneho oddelovacieho znaku a vytvori zoznam stringov
s.replace("a","***") - nahradi podretazec retazcom(pismeno a nahradi ***)
formatovanie retazca 1.sposob : f"Dnes ma Jano {roky} rokov"
"""
s = "Dnes je streda"
print(s.count("s"))
print(s.find("s"))