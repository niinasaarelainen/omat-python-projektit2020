import copy

class Beam:

    def __init__(self, suunta, y, x, id) :
        self.suunta = suunta      # oik, vas, ylos, alas
        self.edellinensuunta = suunta
        self.y = y
        self.x = x    
        self.id = id

    def liiku(self):
        #print(" liiku:", self.y, self.x, self.suunta)     
        if self.suunta == "oik":
            self.x += 1
        elif self.suunta == "vas":
            self.x -= 1
        elif self.suunta == "ylos":
            self.y -= 1
        elif self.suunta == "alas":           
            self.y += 1

    def kaanna(self, merkki):  
        #print(" kaanna:",merkki, self.y, self.x, self.suunta)     

        if '\\' == merkki: 
            if self.suunta == "oik":
                self.suunta = "alas"                
            elif self.suunta == "alas":
                self.suunta = "oik"
            elif self.suunta == "vas":
                self.suunta = "ylos"
            elif self.suunta == "ylos":                
                self.suunta = "vas"

        if '/' == merkki:  
            if self.suunta == "oik":
                self.suunta = "ylos"
            elif self.suunta == "alas":
                self.suunta = "vas"
            elif self.suunta == "vas":
                self.suunta = "alas"
            elif self.suunta == "ylos":
                self.suunta = "oik"

        if '|' == merkki:     
            self.edellinensuunta = self.suunta           
            self.suunta = "alas"

        if '-' == merkki:      
            self.edellinensuunta = self.suunta                  
            self.suunta = "oik"

    def __repr__(self) -> str:
        return f'{self.id}, {self.suunta}, {self.y}, {self.x}'


data = []
beamit = []
uudet_beamit = []
id = 0

def readfile():   
    global y_max, x_max
    f = open("data_1.txt", "r")         
    for rivi in f:           
        rivi = rivi.strip()
        taul = []
        for merkki in rivi:
            taul.append(merkki)
        data.append(taul)   
    y_max = len(data)
    x_max = len(data[0])
    

def lue():
    global beamit, uudet_beamit
    uudet_beamit = copy.deepcopy(beamit)
    print(len(uudet_beamit))
    for beam in uudet_beamit:
        beam.tuhoaMinut = False
        while True:  
            #print("alussa:", beam)    # TODO mistä miinusmerkkiset sijainnit tulevat !?!?!?!?!?
            if beam.x >= 0 and beam.y >= 0 and beam.x < x_max and beam.y < y_max :  
                uudet(data[beam.y][beam.x], beam.edellinensuunta, beam.y, beam.x)       # edellinensuunta  !!!!!
                data[beam.y][beam.x] = '#'
            beam.liiku() 
            if beam.x >= 0 and beam.y >= 0 and beam.x < x_max and beam.y < y_max :  
                beam.kaanna(data[beam.y][beam.x])                
            else:
                beam.tuhoaMinut = True   # tarvitaanko
                break
            #print("lopussa:", beam)
        if not beam.tuhoaMinut:
            beamit.append(beam)
        print(beam)


def uudet(merkki, suunta, y, x):
    global beamit, id
    if '|' == merkki:   
        #print("@uudet: |", suunta)             
        if suunta == "oik" or suunta == "vas" : 
            id += 1
            beamit.append(Beam("ylos", y, x, id))  

    if '-' == merkki:   
        print("@uudet: -", suunta)                    
        if suunta == "ylos" or suunta == "alas" : 
            id += 1
            beamit.append(Beam("vas", y, x, id))  


def piirra():
    print()
    for rivi in range(len(data)): 
        for sarake in range(len(data[rivi])):   
            print(data[rivi][sarake], end="")
        print()
  

readfile()  

beamit.append(Beam("oik", 0, 0, id))
#while beamit != []:
for i in range(5):
    lue()
    piirra()