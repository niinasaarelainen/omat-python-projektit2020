
data = []
henkilot = {"Parta":[], "Hapan": [], "Rudolf":[]}
oikeat_vastaukset = []
alueet = {"metropolitan": [], "atlantic": [], "central": [], "pacific": []}


def readfile():
    f = open("mini.tsv", "r") 
    for rivi in f:        
        data.append(rivi.strip())


def lue_data():
    for rivi in data:
        for i in range(4):   # 4 aluetta
            sp = rivi.split("\t")
            henkilot["Parta"].append(sp[0])        
            henkilot["Hapan"].append(sp[1])        
            henkilot["Rudolf"].append(sp[2])        
            oikeat_vastaukset.append(sp[3])
            if i == 0:
                alueet["metropolitan"].append(henkilot)
                alueet["metropolitan"].append(oikeat_vastaukset)
            elif i == 1:
                alueet["atlantic"].append(henkilot)
                alueet["atlantic"].append(oikeat_vastaukset)
            elif i == 2:
                alueet["central"].append(henkilot)
                alueet["central"].append(oikeat_vastaukset)
            elif i == 3:
                alueet["pacific"].append(henkilot)
                alueet["pacific"].append(oikeat_vastaukset)
            henkilot = {"Parta":[], "Hapan": [], "Rudolf":[]}
            oikeat_vastaukset = []
            
    henkilot["Parta"].append(0)
    henkilot["Hapan"].append(0)
    henkilot["Rudolf"].append(0)

def pisteet():
    for ind in range(len(oikeat_vastaukset)):
        for henkilo in henkilot:
            print(henkilo)
            if oikeat_vastaukset[ind] == henkilot[henkilo][ind]:
                henkilot[henkilo][-1] += 2

            if ind == 0: # ekalla vain 1 naapuri
                if oikeat_vastaukset[ind] == henkilot[henkilo][ind + 1]:
                    henkilot[henkilo][-1] += 1
            elif ind == len(oikeat_vastaukset) - 1:  # vikalla vain 1 naapuri
                if oikeat_vastaukset[ind] == henkilot[henkilo][ind - 1]:
                    henkilot[henkilo][-1] += 1
            else:
                if oikeat_vastaukset[ind] == henkilot[henkilo][ind + 1]:
                    henkilot[henkilo][-1] += 1
                if oikeat_vastaukset[ind] == henkilot[henkilo][ind - 1]:
                    henkilot[henkilo][-1] += 1



    


readfile()
lue_data()
print(henkilot)
print(oikeat_vastaukset)
pisteet()
print("Parta", henkilot["Parta"][-1])
print("Hapan", henkilot["Hapan"][-1])
print("Rudolf",  henkilot["Rudolf"][-1])
