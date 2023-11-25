
data = []
henkilot = {"Parta":[], "Hapan": [], "Rudolf":[]}
pisteet = {"Parta":0, "Hapan": 0, "Rudolf":0}
oikeat_vastaukset = []


def readfile():
    f = open("mini.tsv", "r") 
    for rivi in f:        
        data.append(rivi.strip())


def lue_data():
    for rivi in data:
        sp = rivi.split("\t")
        henkilot["Parta"].append(sp[0])        
        henkilot["Hapan"].append(sp[1])        
        henkilot["Rudolf"].append(sp[2])        
        oikeat_vastaukset.append(sp[3])
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
