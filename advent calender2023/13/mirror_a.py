
data = []
kuva = []
tulos = 0

def readfile():  
    global data, kuva 
    f = open("data.txt", "r")         
    for rivi in f:
        if rivi.strip() == "":
            data.append(kuva)
            kuva = []
        else:
            kuva.append(rivi.strip())
    data.append(kuva)


def tutki_x(data):
    global tulos
    inds = {}
    for rivi in data:
        print(rivi)        
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

    print("tutki_x", inds.values())  
    tulos += max(inds.values()) + 1


def tutki_y(data):
    global tulos
    inds = {}
    
    for y in range(len(data)):
        ind = 0
        jatketaanko = True
        while jatketaanko and ind < len(data):
            #print("ind", ind, "y", y) 
            x = 0
            while jatketaanko and x < len(data[0]):
                if y-ind >= 0 and y + ind + 1 < len(data) and data[y-ind][x] == data[y + ind + 1][x]:
                    #print(data[y-ind], data[y + ind + 1])   
                    inds[y] = y
                    #print("ind", ind, "y", y)
                elif y-ind >= 0 and y + ind + 1 < len(data) and data[y-ind][x] != data[y + ind + 1][x]:
                    inds[y] = -1   # alueen ylitys ei pitäisi tuottaa -1  !!!  laillisten vertailu kylläkin 
                    jatketaanko = False
                    #print("  hep")
                x += 1
            ind += 1

    print("tutki_y", inds.values())  
    tulos += 100 * (max(inds.values()) + 1)



readfile()
print(data)
for kuva in data:
    tutki_y(kuva)
    tutki_x(kuva)
    print()

print(tulos) # 49382  too high, 35100 too low, 35232