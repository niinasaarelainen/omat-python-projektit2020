data = []
winning = []
omat_numerot = []
montako_oikein = {}

def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        alku, loppu = rivi.strip().split(": ")   # alku turha
        data.append(loppu.strip().split(" | "))  


def teeTietorakenteet():  
    global winning, omat_numerot
    for rivi in data:
        win = rivi[0].replace("  ", " ").split(" ")
        omat = rivi[1].replace("  ", " ").split(" ")
        winning.append(win)
        omat_numerot.append(omat)

def montakoOikein():
    global montako_oikein
    for ind in range(len(data)):
        oikein = 0
        
        for nro in winning[ind]:
            if nro in omat_numerot[ind]:
                oikein += 1
        
        if oikein > 0:
            print("oikein", oikein)
            montako_oikein[ind + 1] = kerroKahdella(oikein -1)
        else:
            montako_oikein[ind + 1] = 0


def kerroKahdella(n ):
    if (n == 0):
        return 1
    else:
        return 2* kerroKahdella(n - 1)



readfile()
teeTietorakenteet()
print(winning)
montakoOikein()
print(montako_oikein)
print( sum([v for v in montako_oikein.values()])) # 35585 too high

#print(kerroKahdella(12-1))
#print(kerroKahdella(10-1))   # 512 pitäisi olla max !!!
#print(kerroKahdella(5-1))
