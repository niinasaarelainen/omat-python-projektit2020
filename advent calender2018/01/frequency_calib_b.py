
data = []
freq = 0
tulos = None
kahdesti = []


def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        luku = rivi.replace("+", "")
        data.append(int(luku.strip()))


def lista_kokonaan():
    global freq, kahdesti    
    for luku in data:
        freq += luku
        if freq not in kahdesti:
            kahdesti.append(freq)
            #print(kahdesti)
        else:
            #print("freq", freq)
            return freq

def laske():
    global freq, kahdesti, tulos   

    while tulos == None:
        tulos = lista_kokonaan()
        print(tulos)

    return tulos
        


readfile()
print(laske())
