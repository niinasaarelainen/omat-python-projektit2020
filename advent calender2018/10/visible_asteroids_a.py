import copy


data = []
asteroidit = []
asteroidit_copy = []
luvut = []


def readfile():
    f = open("data_easy.txt", "r") 
    for rivi in f:
        data.append([])
        for merkki in rivi.strip():
            data[-1].append(merkki.strip())

    print(data)


def asteroidien_paikat():
    global data, asteroidit
    for rivi in range(len(data)):
        for merkki in range(len(data[0])):
            if data[rivi][merkki] == "#":
                asteroidit.append([rivi, merkki])


def tutki():
    nakyy = []
    laske_uudestaan = []
    for i in range(len(asteroidit)):
        asteroidit_copy = copy.deepcopy(asteroidit)
        tutkittava = asteroidit_copy.pop(i)
        for muu_asteroidi in asteroidit_copy:
            tutki_jaljella_olevat(tutkittava, muu_asteroidi)
            asteroidit_copy.remove(muu_asteroidi)

def tutki_jaljella_olevat(tutkittava, muu):
    global data, asteroidit_copy
    visible = 0
    row = muu[0]
    seat = muu[1]
    tutkittava_row = tutkittava[0]
    tutkittava_seat = tutkittava[1]
    





readfile()
asteroidien_paikat()
tutki()
#tutki_8_suuntaa(0, 1)
for rivi in data:
    print(rivi)