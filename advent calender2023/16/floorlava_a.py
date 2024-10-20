class Beam:

    def __init__(self, suunta, y, x) :
        self.suunta = suunta      # oik, vas, ylos, alas
        self.y = y
        self.x = x
        self.uudet_beamit = []

    def liiku(self):
        if self.suunta == "oik":
            self.x += 1
        elif self.suunta == "vas":
            print("hep")
            self.x -= 1
        elif self.suunta == "ylos":
            self.y -= 1
        elif self.suunta == "alas":
            self.y += 1

    def kaanna(self, merkki):  
        print(merkki, self.y, self.x)     

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
            print("hep")
            if self.suunta == "oik":
                self.suunta = "ylos"
            elif self.suunta == "alas":
                self.suunta = "vas"
            elif self.suunta == "vas":
                self.suunta = "alas"
            elif self.suunta == "ylos":
                self.suunta = "oik"

        if '|' == merkki:    
            self.suunta = "alas"  
            if self.suunta == "vas" or self.suunta == "oik": 
                self.uudet_beamit.append(Beam("ylos", self.y, self.x))  

        if '-' == merkki:    
            self.suunta = "oik"     
            if self.suunta == "alas" or self.suunta == "ylos": 
                self.uudet_beamit.append(Beam("vas", self.y, self.x))  


data = []
beamit = []


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
    for beam in beamit:
        while True:  
            if beam.x >= 0 and beam.y >= 0 and beam.x < x_max and beam.y < y_max :  
                data[beam.y][beam.x] = '#'
            else:
                break
            beam.liiku() 
            if beam.x >= 0 and beam.y >= 0 and beam.x < x_max and beam.y < y_max :  
                beam.kaanna(data[beam.y][beam.x])
            
        for beam_u in beam.uudet_beamit:
            while True:  
                if beam.x >= 0 and beam.y >= 0 and beam.x < x_max and beam.y < y_max :  
                    data[beam.y][beam.x] = '#'
                else:
                    break
                beam.liiku() 
                if beam.x >= 0 and beam.y >= 0 and beam.x < x_max and beam.y < y_max :  
                    beam.kaanna(data[beam.y][beam.x])

               
            

def piirra():
    print()
    for rivi in range(len(data)): 
        for sarake in range(len(data[rivi])):   
            print(data[rivi][sarake], end="")
        print()
  

readfile()  
for rivi in data:
    print(rivi) 
beamit.append(Beam("oik", 0, 0))
lue()
piirra()