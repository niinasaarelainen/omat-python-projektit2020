
timestamp = 0
bussit_all = []
bussit = []

def readfile():   # a-kohta
    global timestamp, bussit_all
    
    f = open("data.txt", "r")   
    i = 0      
    for rivi in f:
        if i == 0: 
            timestamp = int(rivi.strip())
            i += 1
        else :
            bussit_all = rivi.strip().split(",")

def poista_xt():
    global bussit_all, bussit
    for item in bussit_all:
        if item != "x":            
            bussit.append(int(item)) 


def aikataulut():
    global bussit
    seuraava_bussi = {}  # aika: bussin_nro
    for bussi in bussit:
        t = timestamp // bussi
        aika = t * bussi + bussi
        seuraava_bussi[aika] = bussi

    waiting_time = min(seuraava_bussi) - timestamp
    print(waiting_time)
    bussi_nro = seuraava_bussi[min(seuraava_bussi)]
    print(bussi_nro)
    print(waiting_time * bussi_nro )


readfile()
poista_xt()
print(bussit)
aikataulut()
