data = []
numerot = []
start_x = -1
start_y = -1
ends = []
pituus = 0
korkeus = 0

def readfile():  
    f = open("data_1.txt", "r")      
    for rivi in f:
        data.append(rivi.strip())
        

def muunnaInteiksi():
    global numerot, pituus, korkeus
    for rivi in data:
        r = []
        for str in rivi:
            r.append(int(str))            
        numerot.append(r)
        pituus = len(r)
    korkeus = len(data)


def start_and_ends():
    global start_x, start_y, ends
    for y in range(len(numerot)):
        for x in range(len(numerot[y])):
            if numerot[y][x] == 0:
                start_y = y
                start_x = x 
            if numerot[y][x] == 9:
                ends.append([y, x])


def reitti_rekursio(y, x, nro):    # 1= maali, 0 = tähän asti ok,   -1 = NO !
    print(y, x, nro)
    if numerot[y][x] == 0:
        return -1

    if numerot[y][x] == nro + 1:
        return 1

    return 0


def ysistä_nollaan():
    for end in ends:
        reitti = 0
        reitti_y = end[0]
        reitti_x = end[1]

        while reitti_y != start_y or reitti_x != start_x:
            print(reitti)
            #oik            
            print("oik")                
            while reitti >= 0:
                if reitti_x + 1 < pituus:
                    reitti_x += reitti_rekursio(reitti_y, reitti_x, numerot[reitti_y][reitti_x + 1])  
                else:
                    break  
            #vas
            print("vas")                
            while reitti >= 0:
                if reitti_x - 1 >= 0:
                    reitti_x -= reitti_rekursio(reitti_y, reitti_x, numerot[reitti_y][reitti_x - 1])  
                else:
                    break  
            #ylos            
            print("ylos")                
            while reitti >= 0:
                if reitti_y - 1 >= 0:
                    reitti_y -= 1
                    reitti_y += reitti_rekursio(reitti_y, reitti_x, numerot[reitti_y - 1][reitti_x]) 
                else:
                    break     
            #alas
            print("alas")                
            while reitti >= 0:
                if reitti_y + 1 < pituus:
                    reitti_y += 1
                    reitti_y += reitti_rekursio(reitti_y, reitti_x, numerot[reitti_y + 1][reitti_x]) 
                else:
                    break     

            if reitti == 1 or reitti == -1:
                break



readfile()
muunnaInteiksi()
print(numerot)
start_and_ends()
ysistä_nollaan()