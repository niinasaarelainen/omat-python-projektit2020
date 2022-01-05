def tutki_8_suuntaa(row_nro, seat_nro):
    global data, data_copy
    visible = 0
    nakyy = True
    #print(row_nro, seat_nro, status)
    
    # 1) ylös
    for ylos in range(row_nro -1, -1, -1):     

        if data[ylos][seat_nro] == "#" and nakyy :
            visible += 1
            data[ylos][seat_nro] = "V"
            nakyy = False
        elif data[ylos][seat_nro] == "#" and not nakyy :
            data[ylos][seat_nro] = "_"

    # 2) oik. d ylös
    nakyy = True
    for oikealle in range(1, len(data[0])):
        rw_nr = row_nro
        if rw_nr - oikealle >= 0 and seat_nro + oikealle <= len(data) - 1 :
            rw_nr -= oikealle 
            if data[rw_nr][seat_nro + oikealle] == "#" and nakyy:
                visible += 1
                data[rw_nr][seat_nro + oikealle] = "V"
                nakyy = False
            elif data[rw_nr][seat_nro + oikealle] == "#" and not nakyy :
                data[rw_nr][seat_nro + oikealle] = "_"

    # 3) oik.    
    nakyy = True
    for oikealle in range(seat_nro +1, len(data[0])):
        if data[row_nro][oikealle] == "#" and nakyy :
            visible += 1  
            data[row_nro][oikealle] = "V"
            nakyy = False
        elif data[row_nro][oikealle] == "#" and not nakyy :
            data[row_nro][oikealle] = "_"

    # 4) oik. d alas
    nakyy = True
    for oikealle in range(1, len(data[0])):
        rw_nr = row_nro
        if rw_nr + oikealle <= len(data) - 1 and seat_nro + oikealle <= len(data) - 1 :
            rw_nr += oikealle 
            if data[rw_nr][seat_nro + oikealle] == "#"  and nakyy:
                visible += 1
                data[rw_nr][seat_nro + oikealle] = "V"
                nakyy = False
            elif data[rw_nr][seat_nro + oikealle] == "#" and not nakyy :
                data[rw_nr][seat_nro + oikealle] = "_"

    # 5) alas
    nakyy = True
    for alas in range(row_nro +1, len(data)):       
        if data[alas][seat_nro] == "#" and nakyy :
            visible += 1
            data[alas][seat_nro] = "V"
            nakyy = False
        elif data[alas][seat_nro] == "#" and not nakyy :
            data[alas][seat_nro] = "_"

    # 6)  vas. d alas
    nakyy = True
    for alas in range(1, len(data)):    
        st_nr = seat_nro
        if row_nro + alas <= len(data) - 1 and st_nr - alas >= 0 :
            st_nr -= alas  
            if data[row_nro + alas][st_nr] == "#" and nakyy:                
                visible += 1
                data[row_nro + alas][st_nr] = "V"
                nakyy = False
            elif data[row_nro + alas][st_nr] == "#" and not nakyy :
                data[row_nro + alas][st_nr] = "_"

    # 7) vas.
    nakyy = True
    for vasemmalle in range(seat_nro -1, -1, -1):         
        if data[row_nro][vasemmalle] == "#" and nakyy:
            visible += 1
            data[row_nro][vasemmalle] = "V"
            nakyy = False
        elif data[row_nro][vasemmalle] == "#" and not nakyy :
            data[row_nro][vasemmalle] = "_"

    # 8)  vas. d ylös
    nakyy = True
    for vasemmalle in range(1, len(data[0])):
        rw_nr = row_nro         
        if rw_nr - vasemmalle >= 0 and seat_nro - vasemmalle >= 0 :
            rw_nr -= vasemmalle 
            if data[rw_nr][seat_nro - vasemmalle] == "#" and nakyy :
                data[rw_nr][seat_nro - vasemmalle] = "V"
                visible += 1
                nakyy = False
            elif data[rw_nr][seat_nro - vasemmalle] == "#" and not nakyy :
                data[rw_nr][seat_nro - vasemmalle] = "_"

    print("visible", visible)
    