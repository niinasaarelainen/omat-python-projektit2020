data = []
koordinaatit = {}
koordinaatit_etaisyydet = {}
kielletyt = []
start = (2,0)        # data_1  (1, 1)
olet_tassa = start     # TODO etsi S  !!!!!!!!!!!
ohje = ""
suunta = "oik"    # oik, alas, vas, ylos

def readfile():  
    f = open("data_2.txt", "r")       # data_2 oikein  (8)   
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
    global start, olet_tassa, suunta
    montako_steppia = 0
    for y in range(len(data)): 
        for x in range(len(data[y])):             
            y, x = olet_tassa            
            print("y:", y, "x:", x, data[y][x])
            if '-' == data[y][x]:    
                if suunta == "oik":
                    olet_tassa = (y, x + 1)
                else:
                    olet_tassa = (y, x - 1)
            if '7' == data[y][x]: 
                if  suunta == "oik":
                    olet_tassa = (y + 1, x )
                    suunta = "alas"
                else:
                    olet_tassa = (y, x - 1)
                    suunta = "vas"
            if 'F' == data[y][x]:  
                if suunta == "vas":
                    olet_tassa = (y + 1, x )
                    suunta = "alas"
                else:
                    olet_tassa = (y, x + 1)
                    suunta = "oik"
            if 'L' == data[y][x]:  
                if suunta == "alas":
                    olet_tassa = (y, x + 1)
                    suunta = "oik"
                else:
                    olet_tassa = (y - 1, x)
                    suunta = "ylos"
            if '|' == data[y][x]: 
                if suunta == "alas":
                    olet_tassa = (y + 1, x)
                else:
                    olet_tassa = (y - 1, x)
            if 'J' == data[y][x]:  
                if suunta == "oik":
                    olet_tassa = (y - 1 , x)
                    suunta == "ylos"
                else: 
                    olet_tassa = (y, x -1)
                    suunta = "vas"
                    

            montako_steppia += 1
            if start == olet_tassa:
                return montako_steppia

    print(koordinaatit)


def liiku_myota(muuvi_nro):
    global olet_tassa
    kielletyt.append(olet_tassa)
    edellinen = olet_tassa
    if koordinaatit[olet_tassa] == '.':
        return
    olet_tassa = koordinaatit[olet_tassa][0]
    print("\nolet_tassa", olet_tassa)
    #if olet_tassa in kielletyt:
    #    olet_tassa = koordinaatit[edellinen][1]
    koordinaatit_etaisyydet[olet_tassa] = muuvi_nro + 1
    piirra()


    

readfile()
montako = lue()
print(montako)