import random

class Ai:

    def __init__(self, korkeus, leveys):
        self.pisin_suora = []   # useita listoja, laitetaan aina kun perakkaisia_ennatys tulee
        self.korkeus = korkeus
        self.leveys = leveys


    def nollaa(self):
        self.pisin_suora = []


    def tutki(self, kartta):        
        self.kartta = kartta
        self.vaaka()
        self.pysty()
        self.loytyi_paikka = False
        s = sorted(self.pisin_suora, key=lambda x: x[0], reverse = True)         
        print(s)

        for i in range(len(s)):
            kokelas = s[i]   
            print(kokelas)
            if not kokelas == []:
                y = kokelas[2][0]   # loppupiste
                x = kokelas[2][1]
                y2 = kokelas[1][0]   # alkupiste
                x2 = kokelas[1][1]

                if y >= 0 and y < self.korkeus and x >= 0 and x < self.korkeus:
                    if self.kartta[y][x] == 0:
                        self.kartta[y][x] = 1     # huom!  [y][x]
                        self.loytyi_paikka = True
                        break
                
                if y2 >= 0 and y2 < self.korkeus and x2 >= 0 and x2 < self.korkeus:
                    if self.kartta[y2][x2] == 0:
                        self.kartta[y2][x2] = 1 
                        self.loytyi_paikka = True
                        break                
        self.pisin_suora = []

        if not self.loytyi_paikka:
            while True:
                # random (ei reunat):
                y = random.randint(1, self.korkeus -2)
                x = random.randint(1, self.leveys -2)
                if self.kartta[y][x] == 0:
                    self.kartta[y][x] = 1 
                    break



    def mahtuuko_5_vaaka(self, perakkaisia, alkupiste, loppupiste):   
            x_raja = 4 - perakkaisia
            print(alkupiste[1], x_raja, self.leveys - loppupiste[1])   

            if alkupiste[1] < x_raja or self.leveys - loppupiste[1] < x_raja :
                return False
            return True     

    def vaaka(self):

        perakkaisia = 0  
        alkupiste = (4, 4)          # ekan robotin sijainti
        loppupiste = (4, 4)  
        for y in range(self.korkeus):
            for x in range(self.leveys):
                if self.kartta[y][x] == 1:             # robotti = 1
                    perakkaisia += 1
                    if perakkaisia == 1:
                        alkupiste = (y, x - 1)
                    loppupiste = (y, x + 1)
                    # lisätään potentiaaliset uudet sijainnit, jos kartalla:
                    alku_x = alkupiste[1]
                    loppu_x = loppupiste[1]
                    if alku_x >= 0 or loppu_x < self.korkeus :
                        if self.mahtuuko_5_vaaka(perakkaisia, alkupiste, loppupiste) and self.mahtuuko_5_pysty(perakkaisia, alkupiste, loppupiste):   
                            self.pisin_suora.append([perakkaisia, alkupiste, loppupiste])
                        else:
                            print("ei lisätty")
                else:
                    perakkaisia = 0 


    def mahtuuko_5_pysty(self, perakkaisia, alkupiste, loppupiste):   
            y_raja = 4 - perakkaisia
            print(alkupiste[0], y_raja, self.leveys - loppupiste[0])   

            if alkupiste[0] < y_raja or self.leveys - loppupiste[0] < y_raja :
                return False
            return True

    def pysty(self):

        perakkaisia = 0  
        alkupiste = (4, 4)   
        loppupiste = (4, 4)  
        for x in range(self.korkeus):
            for y in range(self.leveys):
                if self.kartta[y][x] == 1:             # robotti = 1
                    perakkaisia += 1
                    if perakkaisia == 1:
                        alkupiste = (y - 1, x)
                    loppupiste = (y + 1, x)
                    # lisätään potentiaaliset uudet sijainnit, jos kartalla:
                    alku_y = alkupiste[0]
                    loppu_y = loppupiste[0]
                    if alku_y >= 0 or loppu_y < self.korkeus :
                        if self.mahtuuko_5_pysty(perakkaisia, alkupiste, loppupiste) and self.mahtuuko_5_pysty(perakkaisia, alkupiste, loppupiste):  
                            self.pisin_suora.append([perakkaisia, alkupiste, loppupiste])
                        else:
                            print("ei lisätty")
                else:
                    perakkaisia = 0 

            
