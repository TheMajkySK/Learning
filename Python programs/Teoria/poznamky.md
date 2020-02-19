# Siete
- **IP adresa** - 4 miestne číslo, identifikator pocitaca v sieti, od 0-255, napr. 192.164.255.0
- maska rozdeluje IP adresu tak, že prvá čast je cislo siete a druha cast cislo pocitaca

- **MAC adresa** - hardverova adresa sietovej karty v zariadeni (napr. mobil, PC, router,...)
    - napr. H3:56:E5:56:AS:5P
    - prve 3 cisla - vyrobca, dalsie 3 cisla - cislo karty u vyrobcu
## Delenie PC sietí
### 1 - podľa vzdialenosi medzi PC
- A) **LAN** - Local area network - 100m
- B) **MAN** - Metropolitan area network
- C) **WAN** - Wide area network
- D) **PAN** - Personal area network (Je to vlastne LAN)
### 2 - podľa postavenia(úlohy jednotlivych PC)
- A) peer to peer - rovny s rovnym - kazdy pc je rovnocenny
- B) sieť so serverom
- **klient**
    - A) počítač ktory vyuziva sluzby severa 
    - B) program ktory vyuziva sluzby severa(browser, Mozilla Thuinderbird)
- **server** - obsluhuju klienta
### 3 - podľa topológie(rozmiestnenie jednotlivých PC)
- **zbernicová** - PC súťažia že kto bude vysielať
- **hviezdicová** - potrebujeme switch a sietove kable su v tvare hviezdice
- **switch** - zariadenie ktore pouziva na prepojienie MAC adresy
- **stromová** - viacero switchov zapojenych na dalsi switch
- **kruhová** - karty - Token ring(spôsob prístupu k prenosovému médiu) - kto ma token môže vysielať

- **router** 
    - zariadenie, ktore prepaja rozne siete fungujuce na protokole IP, preberá údaje z jednej siete(napr. lokalnej) a posiela ichna rôzne ciele v nadradenej siete
    - môže obsahovat bezpecnostne mechanizmy chraniace vnutorne zariadenia siete pred nechcenymi prenikmi z vonkajších sietí
    - informacie posiela v paketoch
- **paketová komunikácia** 
    - dáta v sieťach sa prenášajú tak že sa rozdelia na menšie časti(pakety)
    - **paket** - ucelený blok ktorý sa prenáša ako celok
    - **hlavička** 
        - **source IP** - zdroj, odosielateľ  
        - **destination IP** - cieľ
        - **heder chcksum** - zistí či sa niečo nezmenilo
    - každý paket môže byť doručený do cieľa inou cestou a v inom poradí
    - gateway(brána) - väčšinou router, slúži ako prístupový bod pre PC do internetu, resp. do inej siete

- **DNS** 
    - domain name system
    - systém prideľovania mien k IP adresám
- **DNS Server**
    - má tabuľku mien a k nim prislúchajúce IP adresy
    - keď v prehliadači napíšeme dómenu počítač sa "opýta" DNS servera, aká je IP adresa