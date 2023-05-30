import itertools

data = []
data_int = []
liters = 150
vastaukset = []
summa = 0

def readfile():
    global summa, data_int
    f = open( "data.txt", "r") 
    for rivi in f:
        rivi = rivi.strip()
        summa += int(rivi)
        data_int.append(int(rivi))
        data_int = sorted(data_int)

def muokkaa_data():
    edellinen = 0
    samoja = 0
    for rivi in data_int:
        if rivi == edellinen:
            samoja += 1
            data.append(str(rivi) + "." + str(samoja))
        else:
            data.append(str(rivi))
            samoja = 0
        edellinen = rivi



def findsubsets(str, n):    
    subsets = list(itertools.combinations(str, n))
    
    for p in subsets:
        mahtuu = liters
        astiat_muistiin = []
        for astia in p:
            mahtuu -= int(float(astia))
            if mahtuu >= 0:
                astiat_muistiin.append(astia)
            if mahtuu == 0:
                if astiat_muistiin not in vastaukset:
                    vastaukset.append(astiat_muistiin)
                continue

readfile()
muokkaa_data()
print(data)
findsubsets(data, 4)
print(vastaukset)
print(len(vastaukset))      