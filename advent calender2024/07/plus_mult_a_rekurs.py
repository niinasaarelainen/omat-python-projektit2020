data = []

def readfile():   
    f = open("data_1.txt", "r")         
    for rivi in f:
        data.append(rivi.strip())


def tutki():
    lukujen_maarat = []
    for rivi in data:
        verrokki, luvut = rivi.split(": ")
        verrokki = int(verrokki)
        luvut = luvut.split(" ")
        lukujen_maarat.append(len(luvut))

        print(rekursoi(verrokki, luvut, luvut, luvut, luvut), verrokki)

    return lukujen_maarat


def rekursoi_no(verrokki, luvut):

    if len(luvut) == 1:
        return [int(luvut[0]), int(luvut[0]), int(luvut[0]), int(luvut[0])]

    else:
        tulos_plus1 = int(luvut[0]) + rekursoi(verrokki, luvut[1:])[0]
        tulos_plus2 = int(luvut[0]) + rekursoi(verrokki, luvut[1:])[2]
        tulos_kerto1 = int(luvut[0]) * rekursoi(verrokki, luvut[1:])[1]
        tulos_kerto2 = int(luvut[0]) * rekursoi(verrokki, luvut[1:])[3]
        return [tulos_plus1, tulos_plus2, tulos_kerto1, tulos_kerto2]

def rekursoi(verrokki, luvut1, luvut2, luvut3, luvut4):

    if len(luvut1) == 1:
        print("len1", int(luvut1[0]), int(luvut2[0]), int(luvut3[0]), int(luvut4[0]))
        return [int(luvut1[0]), int(luvut2[0]), int(luvut3[0]), int(luvut4[0])]

    else:
        summa1 = int(luvut1[0]) + int(luvut1[1])
        lista1 = luvut1[2:]
        lista1.append(str(summa1))

        summa2 = int(luvut1[0]) + int(luvut3[1])
        lista2 = luvut2[2:]
        lista2.append(str(summa2))

        tulo1 = int(luvut3[0]) * int(luvut2[1])
        lista3 = luvut3[2:]
        lista3.append(str(tulo1))

        tulo2 = int(luvut4[0]) * int(luvut4[1])
        lista4 = luvut4[2:]
        lista4.append(str(tulo2))


        int(luvut1[0]) + rekursoi(verrokki, lista1, lista2, lista3, lista4)[0]
        int(luvut2[0]) * rekursoi(verrokki, lista1, lista2, lista3, lista4)[1]
        int(luvut3[0]) + rekursoi(verrokki, lista1, lista2, lista3, lista4)[2]
        int(luvut4[0]) * rekursoi(verrokki, lista1, lista2, lista3, lista4)[3]

        return [summa1, summa2, tulo1, tulo2]
        
         

readfile()
maarat = tutki()
print(min(maarat))
print(max(maarat))