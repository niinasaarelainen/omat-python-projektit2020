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
            #print("  ehp", self.y, self.x, self.suunta)
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
            if self.suunta != "ylos":   # ylösmennessä jatkaa samaan suuntaan                
               self.suunta = "alas"

        if '-' == merkki:      
            self.edellinensuunta = self.suunta                  
            if self.suunta != "vas":    # vas mennessä jatkaa samaan suuntaan    
                self.suunta = "oik"

    def __repr__(self) -> str:
        return f'{self.id}, {self.suunta}, ({self.y}, {self.x})'


data = []
data_orig = []
beamit = []
uudet_beamit = []
id = 0
kaytetyt = []     # {} ei hyvä, koska uusi suunta söi edellisen, tietty ois voinu olla key--> taulukko

def readfile():   
    global y_max, x_max, data_orig, data
    f = open("data_1.txt", "r")         
    for rivi in f:           
        rivi = rivi.strip()
        taul = []
        for merkki in rivi:
            taul.append(merkki)
        data.append(taul)   

    y_max = len(data)
    x_max = len(data[0])
    data_orig = copy.deepcopy(data)
    

def lue():
    global beamit, uudet_beamit
    uudet_beamit = copy.deepcopy(beamit)
    beamit = []
    print("len(uudet_beamit)", len(uudet_beamit))
    for beam in uudet_beamit:
        while True:
            key = str(beam.y) + beam.suunta + str(beam.x) 
            if key in kaytetyt:     # luupinkatkaisu
                #print("key:", key)
                break
            else:
                if beam.x >= 0 and beam.y >= 0 and beam.x < x_max and beam.y < y_max :  
                    beam.kaanna(data_orig[beam.y][beam.x])   
                    uudet(data_orig[beam.y][beam.x], beam.edellinensuunta, beam.y, beam.x)       # edellinensuunta  !!!!!
                    data[beam.y][beam.x] = '#'                    
                    kaytetyt.append(key)
                beam.liiku() 
                if beam.x >= 0 and beam.y >= 0 and beam.x < x_max and beam.y < y_max :  
                    pass        
                else:
                    break   


def uudet(merkki, suunta, y, x):
    global beamit, id
    if '|' == merkki:    
        #print("|")    
        if suunta == "oik" or suunta == "vas" : 
            id += 1
            if y > 0:
                beamit.append(Beam("ylos", y, x, id))  
                #print(beamit)

    if '-' == merkki:   
                     
        if suunta == "ylos" or suunta == "alas" : 
            #print("-", y, x)    
            id += 1
            if x > 0:
                beamit.append(Beam("vas", y, x, id))  
                #print(beamit)


def piirra():
    print()
    montako = 0
    for rivi in range(len(data)): 
        for sarake in range(len(data[rivi])):   
            print(data[rivi][sarake], end="")
            if data[rivi][sarake] == '#':
                montako += 1
        print()
    print(montako)
  

readfile()  
print(y_max, x_max)

beamit.append(Beam("oik", 0, 0, id))
while len(beamit) > 0:
    lue()
    
piirra()
print(len(beamit))
#print(kaytetyt)    # 6567  too low    7884 oikein !!!!