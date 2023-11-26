
data = []
henkilot = {"Parta":[], "Hapan": [], "Rudolf":[]}
oikeat_vastaukset = []
alueet = {"metropolitan": [], "atlantic": [], "central": [], "pacific": []}


def readfile():
    f = open("maxi.tsv", "r") 
    for rivi in f:        
        data.append(rivi.strip())


def lue_data():
    global henkilot, alueet, oikeat_vastaukset
    extra_tab = 0
    for i in range(4):   # 4 aluetta, yksi kerrallaan valmiiksi
        if i >= 1:
            extra_tab += 1
        for rivi_nro in range(len(data)):
            if rivi_nro > 2 and rivi_nro < 11:            
                sp = data[rivi_nro].split("\t")
                henkilot["Parta"].append(sp[i*4 + extra_tab + 0].strip().upper())        
                henkilot["Hapan"].append(sp[i*4 + extra_tab + 1].strip().upper())        
                henkilot["Rudolf"].append(sp[i*4 + extra_tab + 2].strip().upper())        
                oikeat_vastaukset.append(sp[i*4 + extra_tab + 3].strip().upper())

        henkilot["Parta"].append(0)
        henkilot["Hapan"].append(0)
        henkilot["Rudolf"].append(0)

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

               

def pisteet():
    for alue in alueet:
        henkilot = alueet[alue][0]
        oikeat_vastaukset = alueet[alue][1]
        print()
        print(alue)
        for ind in range(len(oikeat_vastaukset)):
            for henkilo in henkilot:
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

        print("Parta", henkilot["Parta"][-1])
        print("Hapan", henkilot["Hapan"][-1])
        print("Rudolf",  henkilot["Rudolf"][-1])  


readfile()
lue_data()
#print(alueet)
pisteet()
