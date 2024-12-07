import math

data = []

def readfile():   
    f = open("data.txt", "r")         
    for rivi in f:
        data.append(rivi.strip())


def tutki():
    lukujen_maarat = []
    for rivi in data:
        tulos, luvut = rivi.split(": ")
        #print(luvut, tulos)
        tulos = int(tulos)
        luvut = luvut.split(" ")
        lukujen_maarat.append(len(luvut))

        if len(luvut) == 2:
            for_1(luvut, tulos)   # 1 operaatio, jos 2 lukua

        if len(luvut) == 3:
            for_2(luvut, tulos)   # 2 operaatiota, jos 3 lukua

        if len(luvut) == 4:
            for_3(luvut, tulos)   # 3 operaatiota, jos 4 lukua

    return lukujen_maarat


def for_1(luvut, tulos):
    
    for i in range(2):
        vast = int(luvut[0])
        if i == 0:
            vast += int(luvut[1])
        else:
            vast *= int(luvut[1])

        if tulos == vast:
            print(vast, "JEEEE")



def for_2(luvut, tulos):
    
    for i in range(2):
        vast = int(luvut[0])
        for j in range(2):
            if i == 0:
                vast += int(luvut[1])
            else:
                vast *= int(luvut[1])
            if j == 0:
                vast += int(luvut[2])
            else:
                vast *= int(luvut[2])

            if tulos == vast:
                print(vast, "JEEEE")


def for_3(luvut, tulos):
    for i in range(2):        
        for j in range(2):
            vast = int(luvut[0])
            for k in range(2):
                if i == 0:
                    vast += int(luvut[1])
                else:
                    vast *= int(luvut[1])
                if j == 0:
                    vast += int(luvut[2])
                else:
                    vast *= int(luvut[2])
                if k == 0:
                    vast += int(luvut[3])
                else:
                    vast *= int(luvut[3])

                if tulos == vast:
                    print(vast, "JEEEE")

readfile()
maarat = tutki()
print(min(maarat))
print(max(maarat))