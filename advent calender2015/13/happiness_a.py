import itertools

data = []
hap = {}

def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi.strip().replace(".", ""))

def muodostaHash():
    for rivi in data:
        h1, t1, gain, nro, t2, t3, t4, t5, t6, t7, h2 = rivi.split(" ")
        nro = int(nro)
        if gain == "lose":
            nro = -nro
        if h1 not in hap:
            hap[h1] = [[h2, nro]]
        else: 
            hap[h1].append([h2, nro])


def tutki():

    permut = list(itertools.permutations(hap.keys()))
    onnellisuudet = []

    for p in permut:
        onnellisuus_yht = 0 
        eka = p[0]
        vika = p[-1]
        for i in range(len(p)-1):             
            tyyppi1 = p[i]
            values = hap[tyyppi1]
            for v in values:                
                if v[0] == p[i+1]:   
                    #print("v[0]", v[0], "tyyppi1", tyyppi1)                 
                    onnellisuus_yht += v[1]
                    tyyppi2 = v[0]
                    values = hap[tyyppi2]
                    for v in values:                        
                        if v[0] == tyyppi1:   
                            #print("v[0]", v[0], "tyyppi2", tyyppi2)                 
                            onnellisuus_yht += v[1]

        values = hap[eka]
        for v in values:                
            if v[0] == vika:              
                onnellisuus_yht += v[1]
        
        values = hap[vika]
        for v in values:                
            if v[0] == eka:              
                onnellisuus_yht += v[1]

        onnellisuudet.append(onnellisuus_yht)

    print(onnellisuudet)
    isoin = sorted(onnellisuudet)[-1]
    print(isoin)


readfile()
muodostaHash()
print(hap)
tutki()
