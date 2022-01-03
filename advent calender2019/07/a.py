
data = []
leveys =  25
korkeus = 6
layer = leveys * korkeus
layers = []

def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi.strip())


def muodosta_layerit():
    global layer, layers
    for i in range(len(data[0]) // layer):
        layers.append(data[0][i * layer: (i + 1) * layer])
   
    return layers


def tutki_layerit():
    maarat_kaikki = []
    vahiten_nollia = {}
    nollia_min = 10000
    
    for l in layers:
        maarat_nykyinen = {}
        for nro in l:
            maarat_nykyinen[nro] = l.count(nro)  
        maarat_kaikki.append(maarat_nykyinen) 
        nollia = maarat_nykyinen["0"]
        if nollia < nollia_min:
            nollia_min = nollia
            vahiten_nollia = maarat_nykyinen

    return vahiten_nollia


readfile()
print(muodosta_layerit())
l = tutki_layerit()
print(l["1"] * l["2"])
