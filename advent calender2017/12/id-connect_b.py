
data = []
dic = {}
tulos = []
laskuri = 0
yli = []
montako_iteraatiota = 1
kasitellyt_nrot = []

def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        sp = rivi.strip().split(" <-> ")
        data.append(sp)

def teeDic():
    for rivi in data:
        lista = []
        arvot = rivi[1].split(", ")
        for a in arvot:
            lista.append(int(a))
        dic[int(rivi[0])] = lista

def keraa_data(alku):
    global laskuri, tulos, kasitellyt_nrot, yli
    for nro in dic[alku]:        
        if nro not in tulos and nro not in kasitellyt_nrot:
            tulos.append(nro) 
            laskuri += 1
            if laskuri < 20000:
                keraa_data(nro)
        if nro not in kasitellyt_nrot:
            kasitellyt_nrot.append(nro)


def ylijaamat():
    global yli, kasitellyt_nrot, tulos
    yli = []
    print("moi")
    for i in range(2000):      # tähän 2000 !!!!!!!!!!!!
        if i not in tulos and i not in kasitellyt_nrot:
            yli.append(i)
    print(" ylijaamat:", yli)
    print(" tulos:", tulos)
    

readfile()
teeDic()
print(dic)
keraa_data(0)
print(tulos)
print(len(tulos))
ylijaamat()


while len(yli) >= 1:    
    laskuri = 0
    alkio = yli.pop(0)
    print("alkio", alkio)
    tulos = []
    keraa_data(alkio)   
    ylijaamat()
    montako_iteraatiota += 1    # tähän ehto

print(montako_iteraatiota)