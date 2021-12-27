alkudata = [0,3,6]
alkudata= [14,3,1,0,9,5]
turns = []   #laitetaan jotain jotta eka oikea luku on indeksissä 1




def muunna():
    global alkudata, turns
    uusi_nro = -1
    for i in range(len(alkudata), 2020):   # 2020
        kasiteltava_nro = turns[0]
        if kasiteltava_nro not in turns[1:]:
            print("oli ekaa kertaa")
            turns.insert(0, 0)
        else:
            uusi_nro = turns[1:].index(kasiteltava_nro)
            print(uusi_nro + 1)
            turns.insert(0, uusi_nro + 1)

        #print(turns)
        



alkudata.reverse()
turns = alkudata
print()
muunna()
print(turns[0])
