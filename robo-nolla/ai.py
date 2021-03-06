import random

class Ai:

    def __init__(self, korkeus, leveys):
        self.kaikki_suorat = []  
        self.korkeus = korkeus
        self.leveys = leveys
        self.kartta = []


    def nollaa(self):
        self.kaikki_suorat = []

    def anna_kartta(self):
        return self.kartta


    # tänne tulee nykyinen alku- ja loppupiste. Pitää ensin tutkia onko pysty-vai mikä
    def esta_4_tai_3(self, alkup, loppup, kartta):   
        self.kartta = kartta
        #print(alkup, loppup)        # huom! molemmat x, y  EI  y, x !!!!!!!!!
        # vaaka:
        if alkup[1] == loppup[1]:
            y = alkup[1]            # molemmissa sama y
            x_alku = alkup[0] - 1
            x_loppu = loppup[0] + 1
            if y >= 0 and y < self.korkeus and x_alku >= 0 and x_alku < self.korkeus:
                if self.kartta[y][x_alku] == 0:
                    self.kartta[y][x_alku] = 1     # huom!  [y][x]
                    return True
            if y >= 0 and y < self.korkeus and x_loppu >= 0 and x_loppu < self.korkeus:
                if self.kartta[y][x_loppu] == 0:
                    self.kartta[y][x_loppu] = 1     # huom!  [y][x]
                    return True
                    
        # pysty:
        if alkup[0] == loppup[0]:
            x = alkup[0]            # molemmissa sama x
            y_alku = alkup[1] - 1
            y_loppu = loppup[1] + 1
            if y_alku >= 0 and y_alku < self.korkeus and x >= 0 and x < self.korkeus:
                if self.kartta[y_alku][x] == 0:
                    self.kartta[y_alku][x] = 1     # huom!  [y][x]
                    return True
            if y_loppu >= 0 and y_loppu < self.korkeus and x >= 0 and x < self.korkeus:
                if self.kartta[y_loppu][x] == 0:
                    self.kartta[y_loppu][x] = 1     # huom!  [y][x]
                    return True

        # diagonaali:
        if not alkup[1] == loppup[1] and not alkup[0] == loppup[0]:
            y_alku = alkup[1] - 1   # huom! molemmat x, y  EI  y, x !!!!!!!!!
            y_loppu = loppup[1] + 1
            x_alku = alkup[0] 
            x_loppu = loppup[0] 
            if x_loppu - x_alku < 0:
                x_alku = x_alku + 1
                x_loppu = x_loppu - 1
            else:
                x_alku = x_alku - 1
                x_loppu = x_loppu + 1
            if y_alku >= 0 and y_alku < self.korkeus and x_alku >= 0 and x_alku < self.korkeus:
                if self.kartta[y_alku][x_alku] == 0:
                    self.kartta[y_alku][x_alku] = 1     # huom!  [y][x]
                    return True
            if y_loppu >= 0 and y_loppu < self.korkeus and x_loppu >= 0 and x_loppu < self.korkeus:
                if self.kartta[y_loppu][x_loppu] == 0:
                    self.kartta[y_loppu][x_loppu] = 1     # huom!  [y][x]
                    return True

        return False
            

    # tänne tulee valmiiksi potentiaaliset uudet pisteet
    def tutki(self, kartta):        
        self.kartta = kartta
        #self.vaaka()
        #self.pysty()
        print()
        self.diagonaali_oikealle()
        self.diagonaali_vasemmalle()
        self.loytyi_paikka = False                                     

        kp = self.leveys // 2    # self.kaikki_suorat = [perakkaisia, alkupiste, loppupiste, onko_ykkösluokkaa]
        s = sorted(self.kaikki_suorat, key=lambda x: (-x[0], -x[3], abs(x[2][0] - kp) + abs(x[2][1] - kp)))  # 1) eniten perkäkkäisiä
                                                                               # 2) ykkösluokkaa  3) keskeisin loppup. sij. ryhmän sisällä 
         
        print(s)

        for i in range(len(s)):
            kokelas = s[i]  
            #print(kokelas)
            if not kokelas == []:
                #print("abs", abs(kokelas[1][0] - kp) , abs(kokelas[1][1] - kp) ,  abs(kokelas[2][0] - kp) , abs(kokelas[2][1] - kp))
                if abs(kokelas[2][0] - kp) + abs(kokelas[2][1] - kp) < abs(kokelas[1][0] - kp) + abs(kokelas[1][1] - kp):
                    y = kokelas[2][0]   # loppupiste
                    x = kokelas[2][1]
                    y2 = kokelas[1][0]   # alkupiste
                    x2 = kokelas[1][1]
                else:
                    y = kokelas[1][0]   # alkupiste
                    x = kokelas[1][1]
                    y2 = kokelas[2][0]   # loppupiste
                    x2 = kokelas[2][1]

                if y >= 0 and y < self.korkeus and x >= 0 and x < self.korkeus and self.kartta[y][x] == 0:    # ensin loppupiste (yleensä)
                    self.kartta[y][x] = 1     # huom!  [y][x]
                    self.loytyi_paikka = True
                    break
                    
                if y2 >= 0 and y2 < self.korkeus and x2 >= 0 and x2 < self.korkeus and self.kartta[y2][x2] == 0:  # sitten alkupiste (yleensä)
                    self.kartta[y2][x2] = 1 
                    self.loytyi_paikka = True
                    break    

        self.kaikki_suorat = []

        if not self.loytyi_paikka:
            while True:
                # random (ei reunat):
                y = random.randint(1, self.korkeus -2)
                x = random.randint(1, self.leveys -2)
                if self.kartta[y][x] == 0:
                    self.kartta[y][x] = 1 
                    self.loytyi_paikka = True
                    break

        if not self.loytyi_paikka:
            while True:
                # random reunat:
                y = random.randint(0, self.korkeus -1)
                x = random.randint(0, self.leveys -1)
                if self.kartta[y][x] == 0:
                    self.kartta[y][x] = 1 
                    break

    
    def onko_ykkosluokkaa_vaaka(self, alkupiste, loppupiste):
            ykkosluokkaa = False
            x_alku = alkupiste[0] -1
            x_loppu = loppupiste[0] +1
            y = alkupiste[1]
            if x_alku >= 0 and x_loppu < self.korkeus:
                if self.kartta[y][x_alku]  == 0 and self.kartta[y][x_loppu] == 0 and y >= 0:
                    #print("x_alku", x_alku, "x_loppu", x_loppu, y)
                    ykkosluokkaa = True
            return ykkosluokkaa
   

    
    def mahtuuko_5_vaaka(self, perakkaisia, alkupiste, loppupiste):   
        x_raja = 4 - perakkaisia
        if alkupiste[1] < x_raja or self.leveys - loppupiste[1] < x_raja :
            print("mahtuuko_5_vaaka  EI", x_raja)
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
                    if alku_x >= 0 or loppu_x < self.korkeus :                    # oli: and
                        if self.mahtuuko_5_vaaka(perakkaisia, alkupiste, loppupiste): 
                            self.kaikki_suorat.append([perakkaisia, alkupiste, loppupiste, self.onko_ykkosluokkaa_vaaka(alkupiste, loppupiste)])
                else:
                    perakkaisia = 0 

   
    def mahtuuko_5_pysty(self, perakkaisia, alkupiste, loppupiste):   
        y_raja = 4 - perakkaisia
        if alkupiste[0] < y_raja or self.leveys - loppupiste[0] < y_raja :
            print("mahtuuko_5_pysty  EI")
            return False
        return True
    

    def onko_ykkosluokkaa_pysty(self, alkupiste, loppupiste):
            ykkosluokkaa = False
            y_alku = alkupiste[1] -1
            y_loppu = loppupiste[1] +1
            x = alkupiste[0]
            if y_alku >= 0 and y_loppu < self.korkeus and x >= 0 :
                if self.kartta[y_alku][x]  == 0 and self.kartta[y_loppu][x] == 0:
                    ykkosluokkaa = True
            return ykkosluokkaa
    

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
                    if alku_y >= 0 or loppu_y < self.korkeus :                  # oli: and
                        if self.mahtuuko_5_pysty(perakkaisia, alkupiste, loppupiste):  
                            self.kaikki_suorat.append([perakkaisia, alkupiste, loppupiste, self.onko_ykkosluokkaa_pysty(alkupiste, loppupiste)])
                else:
                    perakkaisia = 0 

    
    def mahtuuko_5_d(self, perakkaisia, alkupiste, loppupiste):    # TODO check tyhjät !!!! mol. puolilta
        y_raja = 4 - perakkaisia
        x_raja = 4 - perakkaisia      # y, x !!!!!
        if (alkupiste[0] < y_raja or alkupiste[1] < x_raja) and self.kartta[loppupiste[0]][loppupiste[1]] == 2:
            print("  mahtuuko_5_d   eka if")
            return False            
            
        if (self.korkeus - loppupiste[0] < y_raja or self.leveys - loppupiste[1] < x_raja) and self.kartta[alkupiste[0]][alkupiste[1]] == 2 :
            print("  mahtuuko_5_d   toka if")
            return False

        print( perakkaisia, alkupiste, loppupiste)
        return True
    

    def onko_ykkosluokkaa_d_oik(self, alkupiste, loppupiste):
            ykkosluokkaa = False
            x_alku = alkupiste[1] -1
            x_loppu = loppupiste[1] +1
            y_alku = alkupiste[0] -1
            y_loppu = loppupiste[0] +1
            if x_alku >= 0 and x_loppu < self.korkeus and y_alku >= 0 and y_loppu < self.korkeus:
                if self.kartta[y_alku][x_alku]  == 0 and self.kartta[y_loppu][x_loppu] == 0:
                    ykkosluokkaa = True
            return ykkosluokkaa

    def diagonaali_oikealle(self):  
        perakkaisia = 0  
        x_jatko = 0 
        y_jatko = 0     
        alkupiste = (4, 4)          
        loppupiste = (4, 4)  
        for y in range(self.korkeus):     #  ÄLÄ  laita -3, koska esim oik. reuna voi olla diagonaalin _loppu_piste, ei vain alku-
            for x in range(self.leveys):
                if self.kartta[y][x] == 1:             # robotti = 1
                    perakkaisia = 1
                    alkupiste = (y -1 , x - 1)
                    x_jatko = x 
                    y_jatko = y      
                    for i in range(3):   # oik. alas   
                        if x_jatko + 1 < len(self.kartta) -1:                           
                            if self.kartta[y_jatko+1][x_jatko+1] == 1:         
                                perakkaisia += 1  
                                loppupiste = (y_jatko + 2 , x_jatko + 2)
                                # lisätään potentiaaliset uudet sijainnit, jos kartalla:
                                alku_x = alkupiste[1]
                                loppu_x = loppupiste[1]
                                alku_y = alkupiste[0]
                                loppu_y = loppupiste[0]
                                #print(alku_x, alku_y, "loppu:", loppu_x, loppu_y)
                                if (alku_x >= 0 or loppu_x < self.korkeus) and (alku_y >= 0 or loppu_y < self.korkeus) :
                                    if self.mahtuuko_5_d(perakkaisia, alkupiste, loppupiste) :   
                                        self.kaikki_suorat.append([perakkaisia, alkupiste, loppupiste, self.onko_ykkosluokkaa_d_oik(alkupiste, loppupiste)])        # TODO                       
                                
                                y_jatko += 1
                                x_jatko += 1 
                            else:
                                loppupiste = (y_jatko + 1 , x_jatko + 1)
                                # lisätään potentiaaliset uudet sijainnit, jos kartalla:
                                alku_x = alkupiste[1]
                                loppu_x = loppupiste[1]
                                alku_y = alkupiste[0]
                                loppu_y = loppupiste[0]
                                #print(" ! else", alku_x, alku_y, "loppu:", loppu_x, loppu_y)
                                if (alku_x >= 0 or loppu_x < self.korkeus) and (alku_y >= 0 or loppu_y < self.korkeus) and perakkaisia > 0 :
                                    if self.mahtuuko_5_d(perakkaisia, alkupiste, loppupiste) :   
                                        self.kaikki_suorat.append([perakkaisia, alkupiste, loppupiste, self.onko_ykkosluokkaa_d_oik(alkupiste, loppupiste)])        # TODO                       
                                
                                perakkaisia = 0
                else:
                    perakkaisia = 0 
            perakkaisia = 0 


    def onko_ykkosluokkaa_d_vas(self, alkupiste, loppupiste):
            ykkosluokkaa = False
            x_alku = alkupiste[1] +1
            x_loppu = loppupiste[1] -1
            y_alku = alkupiste[0] -1
            y_loppu = loppupiste[0] +1
            if x_alku >= 0 and x_loppu < self.korkeus and y_alku >= 0 and y_loppu < self.korkeus:    # TODO: ONKO OIKEIN  ??
                if self.kartta[y_alku][x_alku]  == 0 and self.kartta[y_loppu][x_loppu] == 0:
                    ykkosluokkaa = True
            return ykkosluokkaa

    def diagonaali_vasemmalle(self):
        perakkaisia = 0  
        x_jatko = 0 
        y_jatko = 0     
        alkupiste = (4, 4)          # ekan robotin sijainti
        loppupiste = (4, 4)  
        for y in range(self.korkeus):
            for x in range(self.leveys):
                if self.kartta[y][x] == 1:             # robotti = 1
                    perakkaisia = 1
                    alkupiste = (y -1 , x + 1)
                    x_jatko = x 
                    y_jatko = y      
                    for i in range(3):   # oik. alas   
                        if x_jatko + 1 < len(self.kartta) -1:                           
                            if self.kartta[y_jatko+1][x_jatko-1] == 1:         
                                perakkaisia += 1  
                                loppupiste = (y_jatko + 2 , x_jatko - 2)
                                # lisätään potentiaaliset uudet sijainnit, jos kartalla:
                                alku_x = alkupiste[1]
                                loppu_x = loppupiste[1]
                                alku_y = alkupiste[0]
                                loppu_y = loppupiste[0]
                                if (alku_x >= 0 or loppu_x < self.korkeus) and (alku_y >= 0 or loppu_y < self.korkeus) :
                                    if self.mahtuuko_5_d(perakkaisia, alkupiste, loppupiste) :  
                                        self.kaikki_suorat.append([perakkaisia, alkupiste, loppupiste, self.onko_ykkosluokkaa_d_vas(alkupiste, loppupiste)])        # TODO                      
                                
                                y_jatko += 1
                                x_jatko -= 1 
                            else:
                                loppupiste = (y_jatko + 1 , x_jatko + 1)
                                # lisätään potentiaaliset uudet sijainnit, jos kartalla:
                                alku_x = alkupiste[1]
                                loppu_x = loppupiste[1]
                                alku_y = alkupiste[0]
                                loppu_y = loppupiste[0]
                                #print(" ! else", alku_x, alku_y, "loppu:", loppu_x, loppu_y)
                                if (alku_x >= 0 or loppu_x < self.korkeus) and (alku_y >= 0 or loppu_y < self.korkeus) and perakkaisia > 0 :
                                    if self.mahtuuko_5_d(perakkaisia, alkupiste, loppupiste) :   
                                        self.kaikki_suorat.append([perakkaisia, alkupiste, loppupiste, self.onko_ykkosluokkaa_d_oik(alkupiste, loppupiste)])        # TODO                       
                                
                                perakkaisia = 0
                else:
                    perakkaisia = 0 
            perakkaisia = 0 