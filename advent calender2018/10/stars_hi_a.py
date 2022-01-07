import copy

data_orig = []
data = []
leveys = 0
korkeus = 0
kuva = []


def readfile():
    f = open("data_easy.txt", "r") 
    for rivi in f:
        sp = rivi.strip().split("=")
        pos = sp[1]
        velo = sp[2]

        sp= pos.split(",")
        x = int(sp[0][1:3].strip())     # position=< 9,  1> velocity=< 0,  2>
        y = int(sp[1].strip().split(">")[0])
 
        sp= velo.split(",")
        velo_x = int(sp[0][1:3].strip())
        velo_y = int(sp[1].strip().split(">")[0])   

        data.append([x, y, velo_x, velo_y])
        data_orig.append([x, y, velo_x, velo_y])



def min_max():
    global data, korkeus, leveys
    x_min = sorted(data)[0][0]
    x_max = sorted(data)[-1][0]
    leveys = x_max - x_min + 1

    data.sort(key = lambda x: x[1])
    y_min = data[0][1]
    y_max = data[-1][1]
    korkeus = y_max - y_min + 1

    return x_min, x_max, y_min, y_max


def alusta_matriisi():
    global kuva
    for rivi in range(korkeus):
        kuva.append([])
        for sarake in range(leveys):
            kuva[-1].append(".")
    piirra()
    
def tyhjenna_matriisi():
    global kuva
    for rivi in range(korkeus):
        for sarake in range(leveys):
            kuva[rivi][sarake] = "."

def piirra():
    print()
    global kuva
    for rivi in range(korkeus):
        print(kuva[rivi])


def initial_piC(x_min, y_min):
    global kuva
    
    for i in range(4):  # montako eri kuvaa   
        tyhjenna_matriisi()
        for r in data_orig:               
            y = r[1] - y_min
            x = r[0] - x_min
            y_vlo = r[3]
            x_vlo = r[2]
            #print(y_vlo, x_vlo)
            kuva[y + (i * y_vlo)][x + (i * x_vlo)] = "#"
            #print(i * y_vlo, i * x_vlo)
        
        piirra()
        


readfile()
x_min, x_max, y_min, y_max = min_max()
alusta_matriisi()
initial_piC(x_min, y_min)

