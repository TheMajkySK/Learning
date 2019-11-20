"""
každý znak v stringu(reťazci) má priradene poradové číslo(index znaku)
poradie číslujeme od 0
ak chceme vypísať písmeno zo stringu tak zadáme premennu a  do [] napíšeme index znaku
aj medzeru ratame ako znak
na stringy mozeme pozerat ako na pole znakov
"""

a = "Dnes je streda"
print(a[12])

"""
vypiste znaky Dnes je streda pod seba
"""
p = 0
for i in range(14):
    print(a[i])