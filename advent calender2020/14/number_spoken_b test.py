alkudata = [0,3,6]
alkudata = [1,3,2]   # 1
alkudata = [2,1,3]   # 10
alkudata= [14,3,1,0,9,5]
turns = {}  


def rakenna_alku_turns():
    global turns

    luku = len(alkudata) - 1
    for nro in alkudata[:-1]:   # vika jää pois
        turns[nro] = luku
        luku -= 1

def muunna():
    global alkudata, turns

    edellinen_lisatty = alkudata[-1]
    kasiteltava_nro = -1

    for i in range(len(alkudata), 30000):   # 2020
        kasiteltava_nro = edellinen_lisatty
        #print("\nkasiteltava_nro", kasiteltava_nro)
        if kasiteltava_nro not in turns:
            #print("oli ekaa kertaa")
            turns[kasiteltava_nro] = 0  # "indeksiin" nolla eli "listan" alkuun
            edellinen_lisatty = 0
        else:
            edellinen_lisatty = turns[kasiteltava_nro]   
            turns[kasiteltava_nro] = 0

        for item in turns:
            turns[item] += 1

        #print(turns)
    return kasiteltava_nro
        



#alkudata.reverse()
#turns = alkudata
print()
rakenna_alku_turns()
print(muunna())
