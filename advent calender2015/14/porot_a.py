
data = []  
porot = []
matkat = []

class Reindeer:

    def __init__(self, tiedot) -> None:        
        self.nopeus = tiedot[0]
        self.liikkuu_s = tiedot[1]
        self.tauko = tiedot[2]        

    def laskuri(self, sec):   # sekunti kerrallaan
        liikunko = True
        self.sykli = self.liikkuu_s + self.tauko 
        self.moneskoSykli = 0
        self.matka = 0
        for s in range(sec):
            if s == self.liikkuu_s + (self.sykli * self.moneskoSykli):
                liikunko = False                   
            if s == self.sykli + (self.sykli * self.moneskoSykli):
                liikunko = True
                self.moneskoSykli += 1
            if liikunko:
                self.matka += self.nopeus     


def readfile():
    # Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds.
    #  0     1   2  3  4    5  6  7        8   9    10   11   12  13  14
    f = open( "data.txt", "r") 
    for rivi in f:
        sp = rivi.strip().split()
        data.append([int(sp[3]), int(sp[6]), int(sp[13])])

def luoPorot():
    """
    for poro in data:
        porot.append(Reindeer(poro))"""
    porot.append(Reindeer([14, 10, 127, "Comet"]))
    porot.append(Reindeer([16, 11, 162, "Dancer"]))
        
def laske(): 
    for poro in porot:
        poro.laskuri(140)   # 2503
        matkat.append(poro.matka)

   
readfile()
print(data)
luoPorot()
laske()
print(matkat)
#print(max(matkat))

