import math

data = []
low_points_data = []
points = []
risk_level = []
basins = []


def readfile():   # a-kohta
    f = open("data.txt", "r")         
    for rivi in f:
        data.append(rivi.strip())
    print(data)


def kasittele_low_points_data():    # 512
    global  points
    for i in range(len(data)):
        low_points_data.append([])
        for nro in data[i]:
            low_points_data[i].append(int(nro))

    
    for rivi in range(len(low_points_data)):  
        for nro_ind in range(len(low_points_data[rivi])):             
            if nro_ind < len(low_points_data[rivi]) -1: 
                seuraava = int(low_points_data[rivi][nro_ind + 1] )    
            else:
                seuraava = 9
            if nro_ind == 0:
                edellinen = 9
            else:
                edellinen = int(low_points_data[rivi][nro_ind - 1])   
            nro = int(low_points_data[rivi][nro_ind])
            print(edellinen, nro, seuraava)
            # eka rivi:   
            if rivi == 0:
                if nro < min(edellinen, seuraava, low_points_data[rivi + 1][nro_ind]) :                    
                    points.append(nro)

            #vika rivi
            elif rivi == len(low_points_data) - 1:
                if nro < min(edellinen, seuraava, low_points_data[rivi -1][nro_ind]) :  
                    points.append(nro)

            #muut rivit
            elif nro < (min(edellinen, seuraava, low_points_data[rivi + 1][nro_ind], low_points_data[rivi -1][nro_ind])):
                #print("nro", nro,  "low_points_data[rivi + 1][nro_ind]", low_points_data[rivi + 1][nro_ind],  "low_points_data[rivi -1][nro_ind]", low_points_data[rivi -1][nro_ind])
                points.append(nro)

            print("points", points)


def risk_level_count():
    riskit= [i+1 for i in points]
    print(sum(riskit))


def basins_kasittele():
    global  basins
    for i in range(len(data)):
        low_points_data.append([])
        for nro in data[i]:
            low_points_data[i].append(int(nro))

    
    for rivi in range(len(low_points_data)):  
        for nro_ind in range(len(low_points_data[rivi])):             
            if nro_ind < len(low_points_data[rivi]) -1: 
                seuraava = int(low_points_data[rivi][nro_ind + 1] )    
            else:
                seuraava = 9
            if nro_ind == 0:
                edellinen = 9
            else:
                edellinen = int(low_points_data[rivi][nro_ind - 1])   
            nro = int(low_points_data[rivi][nro_ind])
            print(edellinen, nro, seuraava)
            # eka rivi:   
            if rivi == 0:
                if nro < min(edellinen, seuraava, low_points_data[rivi + 1][nro_ind]) :                    
                    points.append(nro)

            #vika rivi
            elif rivi == len(low_points_data) - 1:
                if nro < min(edellinen, seuraava, low_points_data[rivi -1][nro_ind]) :  
                    points.append(nro)

            #muut rivit
            elif nro < (min(edellinen, seuraava, low_points_data[rivi + 1][nro_ind], low_points_data[rivi -1][nro_ind])):
                #print("nro", nro,  "low_points_data[rivi + 1][nro_ind]", low_points_data[rivi + 1][nro_ind],  "low_points_data[rivi -1][nro_ind]", low_points_data[rivi -1][nro_ind])
                points.append(nro)

            print("points", points)


readfile()
#kasittele_low_points_data()  # a-osa
basins_kasittele()     #b-osa
risk_level_count()
