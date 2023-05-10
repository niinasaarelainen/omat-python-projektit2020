
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
        

def laske():

    tulokset = []

    for maara1 in range(100):
        for maara2 in range(100):
            for maara3 in range(100):
                for maara4 in range(100):
                    if maara1 + maara2 + maara3 + maara4 == 100:
                        valitulos = 1
                        for i in range(4):
                            yht = maarat[0][i] * maara1 + maarat[1][i] * maara2 + maarat[2][i] * maara3 + maarat[3][i] * maara4
                            valitulos *= yht
                            kalorit = maarat[0][4] * maara1 + maarat[1][4] * maara2 + maarat[2][4] * maara3 + maarat[3][4] * maara4
                            if kalorit == 500:
                                tulokset.append(valitulos)

    tulokset = sorted(tulokset)
    print(tulokset[-1])


readfile()
lue()
print(maarat)
laske()    #18965440
