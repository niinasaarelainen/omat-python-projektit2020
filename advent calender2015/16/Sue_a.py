oikea_Sue = {}

def readfile():
    f = open( "oikea_Sue.txt", "r") 
    for rivi in f:
        rivi = rivi.strip()
        sp = rivi.strip().split(": ")
        oikea_Sue[sp[0]] = int(sp[1])

    f = open( "data.txt", "r") 
    for rivi in f:
        rivi = rivi.strip()
        monesko_merkki = rivi.find(":")
        sue_nro = rivi[:monesko_merkki]
        rivi = rivi[monesko_merkki + 2:]
        tiedot = rivi.strip().split(", ")
        tutki(tiedot, sue_nro)


def tutki(tiedot, sue_nro):
    ok = 0
    for fact in tiedot:
        sp = fact.split(": ")
        if oikea_Sue[sp[0]] == int(sp[1]):
            ok += 1
            
        if ok == 3:
            print(sue_nro)


readfile()
print(oikea_Sue)