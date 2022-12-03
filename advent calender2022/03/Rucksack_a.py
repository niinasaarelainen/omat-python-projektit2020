
data = []
kirjaimet = []
tulokset = []


def readfile():
    f = open("data.txt", "r")         
    for rivi in f:
        data.append(rivi.strip())    


def tutki():
    for rivi in data:
        pit = int(len(rivi) / 2)
        alku = rivi[:pit]
        loppu = rivi[pit:]
        for kirjain in alku:
            if kirjain in loppu:
                kirjaimet.append(kirjain)
                break


def arvot():
    for k in kirjaimet:
        tulos = ord(k) - 96
        if tulos < 0:
            tulos += 58
            
        tulokset.append(tulos)
    print(sum(tulokset))

readfile()
print(data)
tutki()
print(kirjaimet)
arvot()