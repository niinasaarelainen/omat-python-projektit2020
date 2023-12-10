data = []
koordinaatit = {}
koordinaatit_etaisyydet = {}
kielletyt = []
start = (1, 1)
olet_tassa = (1, 1)
ohje = ""


def readfile():   # a-kohta
    f = open("data_1.txt", "r")         
    for rivi in f:
        data.append(rivi.strip())

def piirra():
    global ohje
    for y in range(len(data)): 
        for x in range(len(data[y])): 
            ohje = data[y][x] 
            if y == olet_tassa[0] and x == olet_tassa[1]:
                print("S", end="")
            else:           
                print(data[y][x], end="")
        print()
    


def lue():
    for y in range(len(data)): 
        for x in range(len(data[y])):  
            if '-' == data[y][x]:        # myötäpäivään ensin
                koordinaatit[(y, x)] = [(y, x+1), (y, x-1)]
            if '7' == data[y][x]: 
                koordinaatit[(y, x)] = [(y+1, x), (y, x-1)] 
            if 'F' == data[y][x]:  
                koordinaatit[(y, x)] = [(y, x+1), (y+1, x)] 
            if 'L' == data[y][x]:  
                koordinaatit[(y, x)] = [(y-1, x), (y, x+1)] 
                # mahdoton tietää kumpi suunta:
            if '|' == data[y][x]: 
                koordinaatit[(y, x)] = [(y-1, x), (y+1, x)]  
            if 'J' == data[y][x]:  
                koordinaatit[(y, x)] = [(y, x-1), (y-1, x)] 


def liiku_myota(muuvi_nro):
    global olet_tassa
    kielletyt.append(olet_tassa)
    edellinen = olet_tassa
    olet_tassa = koordinaatit[olet_tassa][0]
    print("olet_tassa", olet_tassa)
    if olet_tassa in kielletyt:
        olet_tassa = koordinaatit[edellinen][1]
    koordinaatit_etaisyydet[olet_tassa] = muuvi_nro + 1
    piirra()

def liiku_vasta(muuvi_nro):
    global olet_tassa
    kielletyt.append(olet_tassa)
    edellinen = olet_tassa
    olet_tassa = koordinaatit[olet_tassa][1]
    print("olet_tassa", olet_tassa)
    if olet_tassa in kielletyt:
        olet_tassa = koordinaatit[edellinen][0]
    if olet_tassa in koordinaatit_etaisyydet and koordinaatit_etaisyydet[olet_tassa] > muuvi_nro:
        koordinaatit_etaisyydet[olet_tassa] = muuvi_nro + 1 
    elif olet_tassa not in koordinaatit_etaisyydet:
        koordinaatit_etaisyydet[olet_tassa] = muuvi_nro + 1 
    piirra()
    

readfile()
lue()
piirra()
for muuvi_nro in range(16):
    liiku_myota(muuvi_nro)
olet_tassa = (1, 1)
print("  VASTA")
kielletyt = []
for muuvi_nro in range(8):
    liiku_vasta(muuvi_nro)
print(koordinaatit_etaisyydet)
print(max(v for k, v in koordinaatit_etaisyydet.items()))