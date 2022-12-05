
data_ohjeet = []
data_pinot = []
pinoja = 0
pinot = []

def readfile():
    global data_ohjeet, data_pinot
    f = open("data_ohj.txt", "r") 
    for rivi in f:
        data_ohjeet.append(rivi.replace("move ", "").strip().split(" from "))

    f = open("data_pin.txt", "r") 
    for rivi in f:
        data_pinot.append(rivi)
    data_pinot.reverse()
    

def tee_pinot():
    
    for rivi in data_pinot:
        indeksit = [i for i in range(len(rivi)) if rivi[i] == "["]
        for ind in indeksit:
            pinot[int(ind / 4) +1].append(rivi[ind + 1])
    print(pinot)


def suorita_ohjeet():
    global pinot
    for rivi in data_ohjeet:
        mista, mihin = rivi[1].split(" to ")
        mista, mihin = int(mista), int(mihin)
        maara = int(rivi[0])
        for i in range(maara):
            if len(pinot[mista]) > 0:
                s = pinot[mista].pop(-1)
                pinot[mihin].append(s)
            #print(pinot)


def tulos():
    tulos = ""
    for i in range(1, pinoja + 1):
        tulos += pinot[i][-1]
    return tulos

readfile()
pinoja = int(max(data_pinot[0]))
for i in range(pinoja + 1):
    pinot.append([])


data_pinot.pop(0)
#print(data_pinot) 

tee_pinot()
print(pinot)
suorita_ohjeet()
print(tulos())

