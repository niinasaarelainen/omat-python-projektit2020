from operator import itemgetter
import random
fail = 1000


def eka_kierros():
    ajat = []
    ajat.append(["Janja", 10.522])
    ajat.append(["Jain", 11.022])
    ajat.append(["Jessica", 8.023])
    ajat.append(["Alex", 8.022])
    ajat.append(["AlexPlus", 9.929])   
    ajat.append(["AlexHidas", 17.022])   
    ajat.append(["Julia", fail])          # varaslähtö
    ajat.append(["Ihmelapsi", 7.022])
    ajat.append(["Anna", fail])
    ajat.append(["Margo", 7.922])

    ajat.sort(key=itemgetter(1))
    return ajat


def finaalikierros(sijoitukset):
    ajat = []
    for i in range(8):
        ajat.append([sijoitukset[i][0], random.randint(8000,15000)/1000])   # aikoja 8.000 .. 15.000 s

    ajat.sort(key=itemgetter(1))
    return ajat


def losers(tyypit):
    ajat = []

    for tyyppi in tyypit:
        r = random.randint(1, 4)
        if r == 1:
            ajat.append([tyyppi[0], 100])   # tarkoittaa fail
        else:
            ajat.append([tyyppi[0], random.randint(8000,15000)/1000])   # aikoja 8.000 .. 15.000 s
    
    ajat.sort(key=itemgetter(1))
    return ajat    


def winners(tyypit):
    ajat = []

    for tyyppi in tyypit:
        ajat.append([tyyppi[0], random.randint(7000,12000)/1000])   
    
    ajat.sort(key=itemgetter(1))
    return ajat    


def finaalit(winners):
    tulos = []

    # 3.-4. sija
    ajat = []
    for tyyppi in winners[2:]:
        ajat.append([tyyppi[0], random.randint(7900,11000)/1000])      
    ajat.sort(key=itemgetter(1), reverse = True)
    #print("3-4-", ajat)
    tulos += ajat       # ei voi lisätä kaikkia kerralla, koska 2. sijoittunut voi olla huonompi kuin 3.

    # 1.-2. sija
    ajat = []
    for tyyppi in winners[:2]:
        ajat.append([tyyppi[0], random.randint(7500,10000)/1000])      
    ajat.sort(key=itemgetter(1), reverse = True)
    #print("1-2-", ajat)
    tulos += ajat 

    tulos.reverse()
    return tulos

def speed_karsinta():
    alkutulos = eka_kierros()
    puolivali = int(len(alkutulos)/2)    # huom!  /2 tekee floatin vaikka tulos on int  8/2 != 4 vaan 4.0 !!! 
    losersit = losers(alkutulos[puolivali:])
    winnersit = winners(alkutulos[:puolivali])
    return finaalit(winnersit) + losersit

def speed_finaali(sijoitukset):
    alkutulos = finaalikierros(sijoitukset)
    puolivali = int(len(alkutulos)/2)    # huom!  /2 tekee floatin vaikka tulos on int  8/2 != 4 vaan 4.0 !!! 
    losersit = losers(alkutulos[puolivali:])
    winnersit = winners(alkutulos[:puolivali])
    return finaalit(winnersit) + losersit

