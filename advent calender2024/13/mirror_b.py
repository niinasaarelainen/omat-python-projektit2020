data = []
kuva = []
tulos = 0
alkuper = 0

def readfile():  
    global data, kuva 
    f = open("data.txt", "r")         
    for rivi in f:
        if rivi.strip() == "":
            data.append(kuva)
            kuva = []
        else:
            kuva.append(list(rivi.strip()))
    data.append(kuva)


def tutki_x(data):
    global tulos
    inds = {}
    for rivi in data:  
        for ind in range(len(data[0])):
            jatketaanko = True
            x = 0
            while jatketaanko and x < len(rivi):
                if ind-x >= 0 and ind + x + 1 < len(rivi) and rivi[ind-x] == rivi[ind + x + 1]:
                    #print(rivi[ind-x], rivi[ind + x + 1])   
                    if ind in inds and inds[ind] != -1:
                        inds[ind] = ind
                    if ind not in inds:
                        inds[ind] = ind

                elif ind-x >= 0 and ind + x + 1 < len(rivi) and rivi[ind-x] != rivi[ind + x + 1]:
                    inds[ind] = -1
                    jatketaanko = False       
                x += 1
            ind += 1            

    #print("tutki_x", inds.values())  
    if max(inds.values()) + 1 == alkuper:
        inds[alkuper - 1] = -1
    return max(inds.values()) + 1


def tutki_y(data):
    global tulos, alkuper
    inds = {}
    
    for y in range(len(data)):
        ind = 0
        jatketaanko = True
        while jatketaanko and ind < len(data):
            #print("ind", ind, "y", y) 
            x = 0
            while jatketaanko and x < len(data[0]):
                if y-ind >= 0 and y + ind + 1 < len(data) and data[y-ind][x] == data[y + ind + 1][x]:
                    inds[y] = y
                    #print("ind", ind, "y", y)
                elif y-ind >= 0 and y + ind + 1 < len(data) and data[y-ind][x] != data[y + ind + 1][x]:
                    inds[y] = -1   
                    jatketaanko = False
                x += 1
            ind += 1

    #print("tutki_y", inds.values())  
    if 100 * (max(inds.values()) + 1)  == alkuper:
        inds[(alkuper - 100) // 100] = -1
    #print("tutki_y", inds.values())      
    return 100 * (max(inds.values()) + 1)



readfile()

for kuva in data:
    alkuper = 0
    if tutki_y(kuva) > 0:
        alkuper += tutki_y(kuva)               
    if tutki_x(kuva) > 0:
        alkuper += tutki_x(kuva) 

    print("alkuper", alkuper)
    print(len(kuva[0]))

    jatketaan = True
    y = 0
    while jatketaan and y < len(kuva):
        x = 0
        while jatketaan and x < len(kuva[0]):
            if kuva[y][x]== ".":
                kuva[y][x] = "#"
            elif kuva[y][x]== "#":
                kuva[y][x] = "."

            
            y_result = tutki_y(kuva)
            if y_result != alkuper and y_result > 0:
                tulos += y_result  
                print("y_res", y_result)
                jatketaan = False

            x_result = tutki_x(kuva)
            if x_result != alkuper and x_result > 0:
                tulos += x_result  
                print("x_res", x_result)
                jatketaan = False  

            if kuva[y][x]== ".":
                kuva[y][x] = "#"
            elif kuva[y][x]== "#":
                kuva[y][x] = "."

            x += 1
        y += 1

print(tulos)   # 32562  too low, 37962 too low , 37982