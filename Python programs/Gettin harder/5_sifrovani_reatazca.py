"""
zašifrujte vetu tak Dnes je streda, všetky písmená zmeníme takto
DNES JE STREDA
NDSEJ  ETSERAD
"""
veta = input("Zadaj vetu na šifrovanie: ")
l = len(veta)
x = veta.upper()
for i in range(0,l,2):
    print(x[i+1], end="")
    print(x[i], end="")