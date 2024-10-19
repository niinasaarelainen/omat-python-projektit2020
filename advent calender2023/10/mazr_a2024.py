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


def maaritaSuunta():
    global start, suunta, olet_tassa
    y, x = start
    if data[y][x + 1] == "J" or data[y][x + 1] == "7"  or data[y][x + 1] == "-":
        suunta = "oik"
        olet_tassa = (y, x + 1)
    elif data[y + 1][x] == "|" or data[y + 1][x] == "L" or data[y + 1][x] == "J":
        suunta = "alas"
        olet_tassa = (y + 1, x)
    


def liiku():
    global start, olet_tassa, suunta
    montako_steppia = 1   # tehty jo 1 step maaritaSuunta():ssa
    for y in range(len(data)): 
        for x in range(len(data[y])):             
            y, x = olet_tassa            
            print("y:", y, "x:", x, data[y][x], suunta)
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
                    suunta = "ylos"
                else: 
                    olet_tassa = (y, x -1)
                    suunta = "vas"                    

            montako_steppia += 1
            if start == olet_tassa:
                return montako_steppia


    

readfile()
etsiS()
maaritaSuunta()
montako = liiku()
print(montako//2)