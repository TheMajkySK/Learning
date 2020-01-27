"""
Textovy subor - Je postupnost znakov, ktora moze obsahovat aj znaky konca raidka. Väčšinou je tato postupnost ulozena na disku v subore.
Na textovy subor sa možeme pozerat ako na postupnost riadkov(može to byt aj prazdna postupnost), pricom kazdy riadok je postupnostou znakov (znakovy retazec), ktora je ukoncena
specialnym znakom "\n"
"""
subor1 = open("xd.txt", "r") #ak chcem nacitat a nieje to v zlozke z ktorej sa spsta programt ak napsiem
print(subor1.read())         # c:\\Users\\maturita\\Documents\\GitHub\\Learning\\Python programs\\Práca so súbormi\\xd.txt - cela cesta suboru, musim dat 2 lomitka alebo opacne lomitko lebo 
                                                                                                                        # jedno \ specialny znak