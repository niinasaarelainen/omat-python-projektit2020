import math

data = []
low_points = []
points_lkm = 0


def readfile():   # a-kohta
    global crabs
    f = open("data_easy.txt", "r")         
    for rivi in f:
        data.append(rivi.strip())
    print(data)

def kasittele_low_points():
    global  points_lkm
    for i in range(len(data)):
        low_points.append([])
        for nro in data[i]:
            low_points[i].append(nro)

    low_point = low_points[0][0]

    for i in range(len(low_points)):
        nro_muistiin = 0
        for nro in low_points[i]:            
                if i == 0:
                    if nro < nro_muistiin:
                        nro_muistiin = nro
                        points_lkm += 1
                elif i == len(low_points) - 1 :
                    pass
                else:
                    if nro < nro_muistiin and nro < low_points[i -1][i] or nro < nro_muistiin and nro < low_points[i + 1][i]:
                        nro_muistiin = nro
                        points_lkm += 1



readfile()
kasittele_low_points()
