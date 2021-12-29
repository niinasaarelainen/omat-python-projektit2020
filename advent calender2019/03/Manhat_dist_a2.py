paths = []
ship_x = 1000
ship_y = 2000
ship_x_orig = 1000
ship_y_orig = 2000
ship_reitit = []
koordinaatit = []


def readfile():
    f = open("data.txt", "r")    # 1= 6,  2 = 159   3 = 135
    for rivi in f:
        paths.append([])
        sp = rivi.strip().split(",")
        for komento in sp:
            ohje = komento[:1]
            nro  = int(komento[1:].strip())
            paths[-1].append([ohje, nro])
    print(paths)



def laske():
    global ship_y, ship_x, ship_x_orig, ship_y_orig
    crosspoints = []

    for reitti in paths:
        ship_x = ship_x_orig
        ship_y = ship_y_orig
        for ohje, nro in reitti:
            for i in range(nro):
                if ohje == "U":
                    ship_y -= 1

                if ohje == "D":
                    ship_y += 1

                if ohje == "L":
                    ship_x -= 1

                if ohje == "R":
                    ship_x += 1
                
                if [ship_y,ship_x] not in koordinaatit: 
                    koordinaatit.append([ship_y,ship_x])
                else:
                    crosspoints.append([ship_y, ship_x]) 
            #print(ship_y, ship_x)
        #print(" 2. reitti:")
    return crosspoints    


def print_list():
    for rivi in ship_reitit:
        print(rivi)


def laske_Manhattans(crosspoints):
    pienin = 1000
    for y, x in crosspoints:
        
        #print(abs(y- ship_y_orig))
        #print(abs(x - ship_x_orig))
        m = abs(y- ship_y_orig) + abs(x - ship_x_orig)
        if m < pienin:
            pienin = m
            print(y, x)

    return pienin
        

readfile()
crosspoints = laske()
m = laske_Manhattans(crosspoints)
#print_list()
print(m)
