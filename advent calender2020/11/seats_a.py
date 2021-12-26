import copy

data = []  
data_copy = []
varatut_total = 0

"""
* If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.

* If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.

* Otherwise, the seat's state does not change.    
"""


def readfile():   # a-kohta
    global data
    f = open("data.txt", "r")         
    for rivi in f: 
        rivi_uusi = []        
        for kirjain in rivi.strip():
            rivi_uusi.append(kirjain)
        data.append(rivi_uusi)    
    print(data_copy)


def tutki_viereiset(row_nro, seat_nro, status):
    global data, data_copy
    occupied = 0
    for i in range(row_nro -1, row_nro + 2):
        for j in range(seat_nro -1, seat_nro + 2):
            if i >= 0 and j >= 0 and i <= len(data)- 1 and j <= len(data[0]) - 1:
                #print(i, j)
                if data[i][j] == "#" and not (i == row_nro and j == seat_nro):
                    occupied += 1
    if status == "#" and occupied >= 4:
        data_copy[row_nro][seat_nro] = "L"
    elif status == "L" and occupied == 0:
        data_copy[row_nro][seat_nro] = "#"
    


def tutki():
    global data, data_copy
    data_copy = copy.deepcopy(data)
    for row_nro in range(len(data)):
        for seat_nro in range(len(data[0])):
            if data[row_nro][seat_nro] in ["L", "#"]:
                tutki_viereiset(row_nro, seat_nro, data[row_nro][seat_nro])
    data = copy.deepcopy(data_copy)


   
readfile()
for i in range(199):  # 99 liian vähän, 199 jo liikaa, mutta ei haittaa
    varatut_total = 0
    tutki()
    for rivi in data:
        #print(rivi)  
        varatut_total += rivi.count("#")
    print("varatut_total", varatut_total)


