data = []
koordinaatit = {}
koordinaatit_etaisyydet = {}
kielletyt = []
start = (1, 1)
olet_tassa = start
ohje = ""


def readfile():  
    f = open("data_1.txt", "r")       # data_2 oikein  (8)   
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
    global start
    for y in range(len(data)): 
        for x in range(len(data[y])):  
            if '.' == data[y][x]:      
                koordinaatit[(y, x)] = '.'
            if '-' == data[y][x]:      # myötäpäivään ensin
                koordinaatit[(y, x)] = [(y, x+1), (y, x-1)]
            if '7' == data[y][x]: 
                koordinaatit[(y, x)] = [(y+1, x), (y, x-1)] 
            if 'F' == data[y][x]:  
                koordinaatit[(y, x)] = [(y, x+1), (y+1, x)] 
            if 'L' == data[y][x]:  
                koordinaatit[(y, x)] = [(y-1, x), (y, x+1)] 
            if '|' == data[y][x]: 
                koordinaatit[(y, x)] = [(y-1, x), (y+1, x)]  
            if 'J' == data[y][x]:  
                koordinaatit[(y, x)] = [(y, x-1), (y-1, x)] 
            if 'S' == data[y][x]:    
                koordinaatit[(y, x)] = []
                if data[y][x+1] != "." and x + 1 < len(data[y]):    
                    koordinaatit[(y, x)].append((y, x+1))
                if data[y][x-1] != "." and x - 1 >= 0:    
                    koordinaatit[(y, x)].append((y, x-1))
                if data[y+1][x] != "." and y + 1 < len(data):    
                    koordinaatit[(y, x)].append((y+1, x))
                if data[y-1][x] != "." and y - 1 >= 0:    
                    koordinaatit[(y, x)].append((y-1, x))
                start = (y, x)


def liiku_myota(muuvi_nro):
    global olet_tassa
    kielletyt.append(olet_tassa)
    edellinen = olet_tassa
    if koordinaatit[olet_tassa] == '.':
        return
    olet_tassa = koordinaatit[olet_tassa][0]
    print("\nolet_tassa", olet_tassa)
    if olet_tassa in kielletyt:
        olet_tassa = koordinaatit[edellinen][1]
    koordinaatit_etaisyydet[olet_tassa] = muuvi_nro + 1
    piirra()

def liiku_vasta(muuvi_nro):
    global olet_tassa
    kielletyt.append(olet_tassa)
    edellinen = olet_tassa
    if koordinaatit[olet_tassa] == '.':
        return
    olet_tassa = koordinaatit[olet_tassa][1]
    print("\nolet_tassa", olet_tassa)
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
olet_tassa = start
print("  VASTA")
kielletyt = []
for muuvi_nro in range(8):
    liiku_vasta(muuvi_nro)
print(koordinaatit_etaisyydet)
print(max(v for k, v in koordinaatit_etaisyydet.items()))