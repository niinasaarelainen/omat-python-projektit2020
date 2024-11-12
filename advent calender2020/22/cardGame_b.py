
pakka1 = [9,2,6,3,1]
pakka2 = [5,8,4,7,10]
#pakka1 = []
#pakka2 = []


def readfile():      
    f = open("data.txt", "r")     
    eka = True    
    for rivi in f:
        if rivi.strip() == '':
            eka = False
        elif eka:
            pakka1.append(int(rivi.strip()))
        else:
            pakka2.append(int(rivi.strip()))
    print(pakka1, pakka2)


def play():
    while pakka2 != [] and pakka1 != []:
        p1 = pakka1.pop(0)
        p2 = pakka2.pop(0)
        if p1 > p2:
            pakka1.append(p1)
            pakka1.append(p2)
        else:
            pakka2.append(p2)
            pakka2.append(p1)
        print(p1, p2, pakka1, pakka2)

def score():
    kerroin = 1
    tulos = 0

    if len(pakka2) > len(pakka1):
        voittopakka = pakka2
    else:
        voittopakka = pakka1
    for card in reversed(voittopakka):
        tulos += kerroin * card
        kerroin += 1
    print(tulos)

#readfile()
play()
score()