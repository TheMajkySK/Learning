"""
K jedntlivym znakom retazca mozeme pristupovat aj zpornýmy cislami
 P| y| t| h| o| n
 0| 1| 2| 3| 4| 5
-6|-5|-4|-3|-2|-1
"""
veta = "dnes je streda!"
#print(veta[-5])
#veta[0] = "D" #premenna typu strung je imatable, tzn. jednotlive znaky nemozeme priamo nahradit inymi znakmi
#namiesto zmeny retazca musime czdy konstruovat novy retazec
l = len(veta)
print("D",end="")
for i in range(1,l):
    print(veta[i], end="")