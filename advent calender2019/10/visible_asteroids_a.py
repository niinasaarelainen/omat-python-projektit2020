import copy


data = []
asteroidit = []
asteroidit_copy = []
luvut = []


def readfile():
    f = open("data_easy.txt", "r") 
    for rivi in f:
        data.append(rivi.strip())

    print(data)


def asteroidien_paikat():
    global asteroidit
    for rivi in range(len(data)):
        for merkki in range(len(data[0])):
            if data[rivi][merkki] == "#":
                asteroidit.append([rivi, merkki])



def tutki():
    nakyy = []
    laske_uudestaan = []
    for i in range(len(asteroidit)):
        asteroidit_copy = copy.deepcopy(asteroidit)
        asteroidit_copy.pop(i)
        for muut_asteroidit in asteroidit_copy:
            if len(nakyy) == 0:
                nakyy.append(muut_asteroidit)
            else:
                # APUA mitä jos lasketaan rivin vikaa.... niin ei voi mennä järjestyksessä
                for a in nakyy:
                    if 




readfile()
asteroidien_paikat()
tutki()