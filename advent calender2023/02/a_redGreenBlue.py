data = []
pallot = {}
max = {"red": 12, "green": 13, "blue": 14}


def readfile():
    f = open("data_1.txt", "r") 
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
        for i in range(0, len(sp), 2):  # 2 = joka toinen alkio (joka toinen väri)
            if int(sp[i]) > 12:
                if int(sp[i]) > max[sp[i+1]]:   # i+1 = väri
                    print(sp[i+1])
                    indeksit_muistiin.append(ind)
    return indeksit_muistiin

def mahdolliset(kielletyt):
    mahd = []
    for ind in pallot:
        if ind not in kielletyt:
            mahd.append(ind)
    print(mahd)
    print(sum(mahd))

def mahdolliset2(kielletyt):
    sum = 0
    for ind in pallot:
        if ind not in kielletyt:
            sum += ind
    print(sum)



readfile() 
makeHash()
#print(pallot)
ind = tutki()
print("ind", ind)
mahdolliset(list(set(ind)))
