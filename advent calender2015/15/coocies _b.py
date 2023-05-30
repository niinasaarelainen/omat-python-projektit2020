
data = []  
maarat = []

def readfile():
    f = open( "data.txt", "r") 
    for rivi in f:
        rivi = rivi.strip()
        data.append(rivi.strip())

def lue():
    global maarat
    tama_cookie = []
    for rivi in data:
        maarat_sp = rivi.split(", ")
        for m in maarat_sp:
            luku = (m[-2] + m[-1]).strip()
            luku = int(luku)
            tama_cookie.append(luku)
        maarat.append(tama_cookie)
        tama_cookie = []


def laske_2_rivia():    # toimii vain data_1:n kanssa
    tulokset = [] 

    for maara1 in range(100):
        maara2 = 100 - maara1
        valitulos = 1
        kalorit = maarat[0][4] * maara1 + maarat[1][4] * maara2 
        if kalorit == 500:
            for i in range(4):
                yht = maarat[0][i] * maara1 + maarat[1][i] * maara2
                if yht < 0:
                    yht = 0
                valitulos *= yht

            tulokset.append(valitulos)
    tulokset = sorted(tulokset)
    print(tulokset)
    print(tulokset[-1])      

def laske():
    tulokset = []

    for maara1 in range(101):
        for maara2 in range(101):
            for maara3 in range(101):
                for maara4 in range(101):
                    if maara1 + maara2 + maara3 + maara4 == 100:
                        valitulos = 1
                        kalorit = maarat[0][4] * maara1 + maarat[1][4] * maara2 + maarat[2][4] * maara3 + maarat[3][4] * maara4
                        if kalorit == 500:
                            for i in range(4):  # 0 = capacity, 3 = texture
                                yht = maarat[0][i] * maara1 + maarat[1][i] * maara2 + maarat[2][i] * maara3 + maarat[3][i] * maara4
                                if yht < 0:
                                    yht = 0
                                valitulos *= yht                                
                            tulokset.append(valitulos)

    tulokset = sorted(tulokset)
    print(tulokset)
    print(tulokset[-1])

def laske_kalorit_mukana():   # ei tämä, koska 2 rivin mallissakaan ei ollut kalorit mukana !
    tulokset = []

    for maara1 in range(100):
        for maara2 in range(100):
            for maara3 in range(100):
                for maara4 in range(100):
                    for maara5 in range(100):
                        if maara1 + maara2 + maara3 + maara4 + maara5 == 100:
                            valitulos = 1
                            kalorit = maarat[0][4] * maara1 + maarat[1][4] * maara2 + maarat[2][4] * maara3 + maarat[3][4] * maara4
                            if kalorit == 500:
                                for i in range(5):  # 0 = capacity, 4 = calories
                                    yht = maarat[0][i] * maara1 + maarat[1][i] * maara2 + maarat[2][i] * maara3 + maarat[3][i] * maara4 
                                    valitulos *= yht                                
                                tulokset.append(valitulos)

    tulokset = sorted(tulokset)
    print(tulokset)
    print(tulokset[-1])


readfile()
lue()
print(maarat)
#laske_2_rivia()
laske()    #17694720 = väärin  too high
#laske_kalorit_mukana()   #  8847360000