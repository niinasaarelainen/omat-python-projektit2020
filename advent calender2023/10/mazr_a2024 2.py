data = []


def readfile():  
    f = open("data.txt", "r")       # data_2 oikein  (8)   
    for rivi in f:
        data.append(rivi.strip())
        

def etsiS():
    global olet_tassa, start
    for y in range(len(data)): 
        for x in range(len(data[y])): 
            if "S" in data[y][x]:
                start = (y, x)


def maaritaSuunta():  # riittää 2 suuntaa, koska lenkki: voi kiertää myötä- tai vastapäivään, sama tulos 
    global start, suunta, olet_tassa    # (katsottu datasta miten luuppi menee, ei ihan yleispätevä)
    y, x = start
    if data[y][x + 1] == "J" or data[y][x + 1] == "7"  or data[y][x + 1] == "-":
        suunta = "oik"
        olet_tassa = (y, x + 1)
    elif data[y + 1][x] == "|" or data[y + 1][x] == "L" or data[y + 1][x] == "J":
        suunta = "alas"
        olet_tassa = (y + 1, x)
    


def kaanna():
    global start, olet_tassa, suunta
    montako_steppia = 1   # tehty jo 1 step maaritaSuunta():ssa
    for y in range(len(data)): 
        for x in range(len(data[y])):             
            y, x = olet_tassa            
            print("y:", y, "x:", x, data[y][x], suunta)            
            if '7' == data[y][x]: 
                if  suunta == "oik":
                    suunta = "alas"
                else:
                    suunta = "vas"
            if 'F' == data[y][x]:  
                if suunta == "vas":
                    suunta = "alas"
                else:
                    suunta = "oik"
            if 'L' == data[y][x]:  
                if suunta == "alas":
                    suunta = "oik"
                else:
                    suunta = "ylos"           
            if 'J' == data[y][x]:  
                if suunta == "oik":
                    suunta = "ylos"
                else: 
                    suunta = "vas"                    

            liiku(y, x)
            montako_steppia += 1
            if start == olet_tassa:
                return montako_steppia


def liiku(y, x):
    global olet_tassa
    if suunta == "oik":
        olet_tassa = (y, x + 1)
    elif suunta == "vas":
        olet_tassa = (y, x - 1)
    elif suunta == "ylos":
        olet_tassa = (y - 1, x)
    elif suunta == "alas":
        olet_tassa = (y + 1, x)


    

readfile()
etsiS()
maaritaSuunta()
montako = kaanna()
print(montako//2)