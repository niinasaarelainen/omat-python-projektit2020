#alkudata = [0,3,6]
alkudata= [14,3,1,0,9,5]
#turns = {0:2, 3:1}  
turns = {14:5,3:4,1:3,0:2,9:1}



def muunna():
    global alkudata, turns

    edellinen_lisatty = alkudata[-1]
    kasiteltava_nro = -1

    for i in range(2014):   # 2020
        kasiteltava_nro = edellinen_lisatty
        print("\nkasiteltava_nro", kasiteltava_nro)
        if kasiteltava_nro not in turns:
            print("oli ekaa kertaa")
            turns[kasiteltava_nro] = 0  # "indeksiin" nolla eli "listan" alkuun
            edellinen_lisatty = 0
        else:
            edellinen_lisatty = turns[kasiteltava_nro]    # +1 ????
            turns[kasiteltava_nro] = 0

        for item in turns:
            turns[item] += 1

        #print(turns)
    return kasiteltava_nro
        



#alkudata.reverse()
#turns = alkudata
print()
muunna()
print(muunna())
