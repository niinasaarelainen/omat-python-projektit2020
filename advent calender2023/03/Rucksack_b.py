
data = []
kirjaimet = []
tulokset = []


def readfile():
    f = open("data.txt", "r")         
    for rivi in f:
        data.append(rivi.strip())    


def tutki():
    i = 0
    yhteiset = []
    while i <= len(data) -3:
        print(data[i])
        for kirjain in data[i]:
            if kirjain in data[i+1] and kirjain in data[i+2] :
                if kirjain not in yhteiset:  # duplikaatti pois
                    yhteiset.append(kirjain)
        kirjaimet.append(yhteiset)
        yhteiset = []            
        i += 3


def arvot():
    for array in kirjaimet:
        for k in array:
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