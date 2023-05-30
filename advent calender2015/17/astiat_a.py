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


def laske_maksimiastiamaara():   # summa 416
    s = sorted(data_int)
    sum  = 0
    for i in range(len(s)):
        sum += s[i]
        print(sum)
        if sum >= 150:
            print(i)
            break
    return sum

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
                if sorted(astiat_muistiin) not in vastaukset:
                    vastaukset.append(sorted(astiat_muistiin))
                continue

readfile()
muokkaa_data()
print(data)
maksimi = laske_maksimiastiamaara()
for n in range(2, maksimi):
    findsubsets(data, n)
print(vastaukset)
print(len(vastaukset))       # 3304  too low
#print(vastaukset[-1]) 