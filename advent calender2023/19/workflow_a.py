import re

data = {}  
arvot = []
lopputulos = 0


def readfile():   
    f = open("data.txt", "r")         
    for rivi in f:
        sp = rivi.strip().split("{")
        data[sp[0]] = sp[1][:-1]   # vika merkki pois
    print(data)

    f = open("data_arvot.txt", "r")         
    for rivi in f:
        arvot.append(rivi.strip()[1:-1])
    print(arvot)



def kayLapi(lukusetti):
    global lopputulos
    x = int(lukusetti[0])
    m = int(lukusetti[1])
    a = int(lukusetti[2])
    s = int(lukusetti[3])
    tulos = "in"
    while tulos != "R" and tulos != "A" :
        print(tulos)
        v = data[tulos]
        ehdot = v.split(",")   # x>10:one,m<20:two,a>30:R,A
        for ehto in ehdot[0:-1]:  # kaikki paitsi vika
            if '>' in ehto:
                alku, mihin = ehto.split(":")
                aa, bee =  alku.split(">")
                if int(eval(aa)) > int(bee):           # eval !!!!!!!!!!!!!!!
                    tulos = mihin
                    break
            elif '<' in ehto:
                alku, mihin = ehto.split(":")
                aa, bee =  alku.split("<")
                if int(eval(aa)) < int(bee):
                    tulos = mihin
                    break
            tulos = ehdot[-1]
    if tulos == 'A':
        lopputulos += x
        lopputulos += m
        lopputulos += a
        lopputulos += s
        


readfile()
luvut = []
for rivi in arvot:
    setti = []
    sp = rivi.split("=")
    for item in range(1, len(sp)-1):
        setti.append(sp[item].split(",")[0])
    setti.append(sp[-1])
    luvut.append(setti)
print(luvut)
for lukusetti in luvut:
    kayLapi(lukusetti)

print(lopputulos)