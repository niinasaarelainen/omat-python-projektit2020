data = []
numerot = []

def readfile():
    global numerot
    f = open("mediaani.txt", "r")   # ULRD
    for rivi in f:
        data.append(rivi.strip())
        
    for r in data:       
        nrot = r.split("\t")
        for n in nrot:
            numerot.append(int(n))        
    numerot = sorted(numerot)


def mediaani():    
    kesk = len(numerot)//2
    print(numerot)
    print("Mediaani on", numerot[kesk])


def moodi_hash():
    montako_kutakin = {}
    for n in numerot:
        if n in montako_kutakin:
            montako_kutakin[n] += 1
        else:
            montako_kutakin[n] = 1
    print(montako_kutakin)    
    montako_kutakin = sorted(montako_kutakin.items(), key=lambda x:x[1])
    print("Yleisin luku on", montako_kutakin[-1][0])

    # EI NÄIN:
    #montako_kutakin = sorted(montako_kutakin.values(), key=lambda x:x)
    #print("Yleisin luku on", montako_kutakin[-1])

def moodi_taulukko():
    montako_kutakin = []
    print(max(numerot))
    for i in range(max(numerot) + 1):
        montako_kutakin.append(0)

    for n in numerot:
        montako_kutakin[n] += 1
    print(montako_kutakin)    
    yleisin = montako_kutakin.index(max(montako_kutakin))
    print("Yleisin luku eli moodi on", yleisin)
    

readfile()
mediaani()
moodi_hash()
moodi_taulukko()