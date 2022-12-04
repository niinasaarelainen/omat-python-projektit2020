
data = []
dic = {}
tulos = []
laskuri = 0

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
    global laskuri, tulos
    for nro in dic[alku]:
        if nro not in tulos:
            tulos.append(nro) 
            laskuri += 1
            if laskuri < 200000:
                keraa_data(nro)


readfile()
teeDic()
print(dic)
keraa_data(0)
print(tulos)
print(len(tulos))