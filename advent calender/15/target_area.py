
target_aria = []  #4 lukua: xmin, xmax, ymin, ymax


def readfile():   # a-kohta
    global data
    f = open("data_easy.txt", "r")         
    for rivi in f:
        x, y = rivi.split(",")
        x = x.split("..")
        y = y.split("..")
        for nro in x:
            target_aria.append(int(nro))
        for nro in y:
            target_aria.append(int(nro))

    print(target_aria)


def liikerata():    #target  20..30, -10..-5
    x_pos = 0
    y_pos = 0
    x, y = 7,2
    onnistui = False

    print(x_pos, y_pos)
    for times in range(10):
        x_pos += x  
        y_pos += y
        print(x_pos, y_pos)
        if target_aria[0] < x_pos < target_aria[1]  and target_aria[2]  < y_pos < target_aria[3] :
            onnistui = True
            break

        if x > 0:
            x -= 1
        y -= 1
    return onnistui    
        


readfile()
print(liikerata())
