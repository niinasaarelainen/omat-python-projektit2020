
target_aria = []  #4 lukua: xmin, xmax, ymin, ymax
y_liikerata_max = 0


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


def liikerata(x, y):    #target  20..30, -10..-5    6,9 paras arvo
    global y_liikerata_max
    x_pos = 0
    y_pos = 0
    #x, y = 1,1
    onnistui = False
    y_max = 0

    for times in range(1000):
        x_pos += x  
        y_pos += y
        if y_pos > y_max:
            y_max = y_pos
        
        #print(x_pos, y_pos)
        if target_aria[0] <= x_pos <= target_aria[1]  and target_aria[2] <= y_pos <= target_aria[3] :
            onnistui = True
            print("y_max", y_max)
            if y_max > y_liikerata_max:
                y_liikerata_max = y_max
            break
        if x > 0:
            x -= 1
        y -= 1

    return onnistui    
        


readfile()

for x in range(target_aria[1]):
    for y in range(abs(target_aria[2])):
        liikerata(x, y)

print(y_liikerata_max)
