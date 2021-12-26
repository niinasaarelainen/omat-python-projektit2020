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


def tutki_8_suuntaa(row_nro, seat_nro, status):
    global data, data_copy
    occupied = 0
    #print(row_nro, seat_nro, status)
    
    # 1) ylös
    for ylos in range(row_nro -1, -1, -1):       
        if data[ylos][seat_nro] == "#" :
            occupied += 1
            break
        elif data[ylos][seat_nro] == "L" :
            break

    # 2) oik. d ylös
    for oikealle in range(1, len(data[0])):
        rw_nr = row_nro
        if rw_nr - oikealle >= 0 and seat_nro + oikealle <= len(data) - 1 :
            rw_nr -= oikealle 
            if data[rw_nr][seat_nro + oikealle] == "#" :
                occupied += 1
                break
            elif data[rw_nr][seat_nro + oikealle] == "L" :
                break

    # 3) oik.    
    for oikealle in range(seat_nro +1, len(data[0])):
        if data[row_nro][oikealle] == "#" :
            occupied += 1  
            break
        elif data[row_nro][oikealle] == "L" :
            break

    # 4) oik. d alas
    for oikealle in range(1, len(data[0])):
        rw_nr = row_nro
        if rw_nr + oikealle <= len(data) - 1 and seat_nro + oikealle <= len(data) - 1 :
            rw_nr += oikealle 
            if data[rw_nr][seat_nro + oikealle] == "#" :
                occupied += 1
                break
            elif data[rw_nr][seat_nro + oikealle] == "L" :
                break

    # 5) alas
    for alas in range(row_nro +1, len(data)):       
        if data[alas][seat_nro] == "#" :
            occupied += 1
            break
        elif data[alas][seat_nro] == "L" :
            break

    # 6)  vas. d alas
    for alas in range(1, len(data)):    
        st_nr = seat_nro
        if row_nro + alas <= len(data) - 1 and st_nr - alas >= 0 :
            st_nr -= alas  
            if data[row_nro + alas][st_nr] == "#" :                
                occupied += 1
                break
            elif data[row_nro + alas][st_nr] == "L" :
                break

    # 7) vas.
    for vasemmalle in range(seat_nro -1, -1, -1):         
        if data[row_nro][vasemmalle] == "#" :
            occupied += 1
            break
        elif data[row_nro][vasemmalle] == "L" :
            break

    # 8)  vas. d ylös
    for vasemmalle in range(1, len(data[0])):
        rw_nr = row_nro         
        if rw_nr - vasemmalle >= 0 and seat_nro - vasemmalle >= 0 :
            #print("         ", rw_nr - vasemmalle, seat_nro - vasemmalle)  
            rw_nr -= vasemmalle 
            if data[rw_nr][seat_nro - vasemmalle] == "#" :
                #print("      hep", rw_nr , seat_nro - vasemmalle)
                occupied += 1
                break
            elif data[rw_nr][seat_nro - vasemmalle] == "L" :
                break

    #print(occupied)

    if status == "#" and occupied >= 5:
        data_copy[row_nro][seat_nro] = "L"
    elif status == "L" and occupied == 0:
        data_copy[row_nro][seat_nro] = "#"
    


def tutki():
    global data, data_copy
    data_copy = copy.deepcopy(data)
    for row_nro in range(len(data)):
        for seat_nro in range(len(data[0])):
            if data[row_nro][seat_nro] in ["L", "#"]:
                tutki_8_suuntaa(row_nro, seat_nro, data[row_nro][seat_nro])
    data = copy.deepcopy(data_copy)


def vastaus():
    f = open("vastaus.txt", "r")   
    v = []      
    for rivi in f: 
        rivi_uusi = []        

        for kirjain in rivi.strip():
            rivi_uusi.append(kirjain)
        v.append(rivi_uusi)  
    return v


   
readfile()
for i in range(233):  # 191 
    varatut_total = 0
    tutki()
    for rivi in data:
        #print(rivi)  
        varatut_total += rivi.count("#")
    print("varatut_total", varatut_total)

""" vain data_easy:n kanssa
vastaus = vastaus()
for i in range(len(data)):
    if vastaus[i] != data[i]:
        print("ERI")  """



