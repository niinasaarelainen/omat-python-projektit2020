
data = []
henkilot = {"Parta":[], "Hapan": [], "Rudolf":[]}
oikeat_vastaukset = []


def readfile():
    f = open("mini.tsv", "r") 
    for rivi in f:        
        data.append(rivi.strip())


def lue():
    for rivi in data:
        sp = rivi.split("\t")
        henkilot["Parta"].append(sp[0])
        henkilot["Hapan"].append(sp[1])
        henkilot["Rudolf"].append(sp[2])
        oikeat_vastaukset.append(sp[3])


readfile()
lue()
print(henkilot)
print(oikeat_vastaukset)