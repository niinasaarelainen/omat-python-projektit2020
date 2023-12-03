data = []
pallot = {}
max = {"red": 12, "green": 13, "blue": 14}


def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        rivi = rivi.replace(",", "").replace(";", "")
        data.append(rivi.strip().split(":"))   


def makeHash():
    for rivi in data:
        game, nro = rivi[0].split(" ")
        pallot[int(nro)] = rivi[1].strip()

def tutki():
    indeksit_muistiin = []
    for ind in pallot:
        sp = pallot[ind].split(" ")
        for i in range(0, len(sp), 2):  # 2 = joka toinen alkio
            if int(sp[i]) > 12:
                if int(sp[i]) > max[sp[i+1]]:
                    print(sp[i+1])
                    indeksit_muistiin.append(ind)
    return indeksit_muistiin

def mahdolliset(kielletyt):
    mahd = []
    for ind in pallot:
        if ind not in kielletyt:
            mahd.append(ind)
    print(sum(mahd))



readfile() 
makeHash()
#print(pallot)
ind = tutki()
mahdolliset(list(set(ind)))
