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

def move(irti):
    sykli = 0 
    mina = -1
    while sykli <= pilareita + irti :  
        if sykli >= irti:
            mina += 1  
        if mina % pilareita in dict and mina >= 0:
            if dict[mina % pilareita].positio == 0:
                #print("kolari")
                return
            
        for p in pilarit:
            p.seuraava_positio()
        
        sykli += 1
    print("success", irti)
        


readfile()
muodosta_dict_ja_pilarit()
pilareita = max(dict.keys()) + 1
for i in range(201, 400):
    move(i)
    muodosta_dict_ja_pilarit()
print("end")