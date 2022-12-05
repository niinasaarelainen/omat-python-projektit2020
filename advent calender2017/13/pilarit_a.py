class Pilari:

    def __init__(self, ind, depth):
        self.indeksi = ind
        self.depth = depth
        self.positio = 0
        self.suunta = "alas"

    def seuraava_positio(self):
        if self.suunta == "alas":
            if self.positio + 1 == self.depth:
                self.positio -= 1
                self.suunta = "ylös"
            else:
                self.positio += 1
        elif self.suunta == "ylös":
            if self.positio - 1 == -1:
                self.positio += 1
                self.suunta = "alas"
            else:
                self.positio -= 1



data = []
dict = {}  # pilarin indeksi --> Pilari
pilarit = []
nrot = []

def readfile():
    f = open("data.txt", "r")  # e riviä
    for rivi in f:
        data.append(rivi.strip())


def muodosta_dict_ja_pilarit():
    for rivi in data:
        ind, depth = rivi.split(": ")
        ind, depth = int(ind), int(depth)
        p  = Pilari(ind, depth)
        pilarit.append(p)
        dict[ind] = p
        
    #print([p.indeksi for p in pilarit])

def move():
    global nrot
    tila = 0
    print([p.positio for p in pilarit])   
    while tila <= pilareita :   # joka pilarissa ollaan 2 vuoroa
        if tila in dict:
            if dict[tila].positio == 0:
                nrot.append(tila)
        for p in pilarit:
            p.seuraava_positio()
        print([p.positio for p in pilarit])    
        tila += 1


readfile()
muodosta_dict_ja_pilarit()
pilareita = max(dict.keys()) 
move()
print(sum([nro * dict[nro].depth for nro in nrot]))