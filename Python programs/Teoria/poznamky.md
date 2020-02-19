# Siete
- IP adresa - 4 miestne číslo, identifikator pocitaca v sieti, od 0-255, napr. 192.164.255.0
- maska rozdeluje IP adresu tak, že prvá čast je cislo siete a druha cast cislo pocitaca

- MAC adresa - hardverova adresa sietovej karty v zariadeni (napr. mobil, PC, router,...)
    - napr. H3:56:E5:56:AS:5P
    - prve 3 cisla - vyrobca, dalsie 3 cisla - cislo karty u vyrobcu
## Delenie PC sietí
### 1 - podľa vzdialenosi medzi PC
- A) LAN - Local area network - 100m
- B) MAN - Metropolitan area network
- C) WAN - Wide area network
- D) PAN - Personal area network (Je to vlastne LAN)
### 2 - podľa postavenia(úlohy jednotlivych PC)
- A) peer to peer - rovny s rovnym - kazdy pc je rovnocenny
- B) sieť so serverom
- klient - A) počítač ktory vyuziva sluzby severa 
         - B) program ktory vyuziva sluzby severa(browser, Mozilla Thuinderbird)
- server - obsluhuju klienta
### 3 - podľa topológie(rozmiestnenie jednotlivých PC)
- zbernicová - PC súťažia že kto bude vysielať
- hviezdicová - potrebujeme switch a sietove kable su v tvare hviezdice
- switch - zariadenie ktore pouziva na prepojienie MAC adresy
- stromová - viacero switchov zapojenych na dalsi switch
- kruhová - karty - Token ring(spôsob prístupu k prenosovému médiu) - kto ma token môže vysielať