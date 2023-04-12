import copy

data = []
tulokset = []
sanojen_pit = 0


def readfile():
    global sanojen_pit
    f = open("data.txt", "r") 
    for rivi in f:        
        data.append(rivi.strip())    # voi olla "monta planeettaa"

    sanojen_pit = len(data[0])


def tutki():  
    kaikki_tilastot = []
    for monesko_kirjain in range(sanojen_pit):
        tilasto = {}
        for sana in data:
            kirjain = sana[monesko_kirjain]
            if kirjain in tilasto:
                tilasto[kirjain] += 1
            else:
                tilasto[kirjain] = 1
        inverse = [(value, key) for key, value in tilasto.items()]
        kaikki_tilastot.append((max(inverse)[1]))

    return kaikki_tilastot


readfile()
print("".join(tutki()))