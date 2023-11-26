
data = []  
porot = []
matkat = []

class Reindeer:

    def __init__(self, tiedot) -> None:        
        self.nopeus = tiedot[0]
        self.liikkuu_s = tiedot[1]
        self.tauko = tiedot[2]    
        self.nimi = tiedot[3]    
        self.points = 0
        self.matka = 0
        self.liikunko = True
        self.moneskoSykli = 0        

    def laskuri(self, s):   # ei lähdetä aina nollasta
        
        self.sykli = self.liikkuu_s + self.tauko         
        
        if s == self.liikkuu_s + (self.sykli * self.moneskoSykli):
            self.liikunko = False                   
        if s == self.sykli + (self.sykli * self.moneskoSykli):
            self.liikunko = True
            self.moneskoSykli += 1
        if self.liikunko:
            self.matka += self.nopeus     


def readfile():
    # Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds.
    #  0     1   2  3  4    5  6  7        8   9    10   11   12  13  14
    f = open( "data.txt", "r") 
    for rivi in f:
        sp = rivi.strip().split()
        data.append([int(sp[3]), int(sp[6]), int(sp[13]), sp[0]])

def luoPorot():
    
    for poro in data:
        porot.append(Reindeer(poro))  
    """
    porot.append(Reindeer([14, 10, 127, "Comet"]))
    porot.append(Reindeer([16, 11, 162, "Dancer"]))  """
        
def laske(): 
    global matkat
    
    for s in range(2503):
        matkat = []
        for poro in porot:
            poro.laskuri(s)
            matkat.append([poro.matka, poro.nimi, poro.points])
        matkat.sort(key=lambda x:x[0])
        maxmatka = matkat[-1][0]
        for poro in porot:  # useille pisteitä!!
            if poro.matka == maxmatka:
                poro.points += 1    

   
readfile()
luoPorot()
laske()
 
# täällä oikea pistetilanne, miksei porot järjesty?
porot.sort(key=lambda x:x.points)
print(porot[-1].points, porot[-1].nimi)  
print(sum([poro.points for poro in porot]))
for poro in porot:
    print(poro.nimi, poro.points, poro.matka)
