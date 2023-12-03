
target_aria = []  #4 lukua: xmin, xmax, ymin, ymax
y_liikerata_max = 0
liikeradat_lkm = 0
liikeradat = []


def readfile():   # a-kohta
    global data
    f = open("data.txt", "r")         
    for rivi in f:
        x, y = rivi.split(",")
        x = x.split("..")
        y = y.split("..")
        for nro in x:
            target_aria.append(int(nro))
        for nro in y:
            target_aria.append(int(nro))

    print(target_aria)


def liikerata(x, y):    #target  20..30, -10..-5    6,9 paras arvo   2262 too low
    global y_liikerata_max, liikeradat_lkm, liikeradat
    x_pos = 0
    y_pos = 0
    #x, y = 1,1
    onnistui = False
    y_max = 0

    for times in range(2000):
        x_pos += x  
        y_pos += y
        if y_pos > y_max:
            y_max = y_pos
        
        #print(x_pos, y_pos)
        if target_aria[0] <= x_pos <= target_aria[1]  and target_aria[2] <= y_pos <= target_aria[3] :
            onnistui = True
            liikeradat_lkm += 1
            liikeradat.append([x_pos, y_pos])
            if y_max > y_liikerata_max:
                y_liikerata_max = y_max
            break
        if x > 0:
            x -= 1
        y -= 1

    return onnistui    
        


readfile()

for x in range(target_aria[1]+1):
    for y in range(target_aria[2], abs(target_aria[2])+1):
        liikerata(x, y)

print(liikeradat_lkm)
#print(liikeradat)
