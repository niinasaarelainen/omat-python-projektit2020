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
        self.vaaka()
        self.pysty()
        self.diagonaali_oikealle()
        self.loytyi_paikka = False                                     

        kp = self.leveys // 2    # self.kaikki_suorat = [perakkaisia, alkupiste, loppupiste]
        s = sorted(self.kaikki_suorat, key=lambda x: (-x[0], abs(x[2][0] - kp) + abs(x[2][1] - kp)))  # 1) eniten perkäkkäisiä
                                                                                                     # 2) keskeisin loppup. sij. ryhmän sisällä 
        #sama_maara_perakkaisia = [piste for  piste in s if piste[0] == s[0][0] ]       
        print(s)
 
        for i in range(len(s)):
            kokelas = s[i]  
            print("kokelas", kokelas)
            if not kokelas == []:
                print("abs", abs(kokelas[2][0] - kp) + abs(kokelas[2][1] - kp) ,  abs(kokelas[1][0] - kp) + abs(kokelas[1][1] - kp))
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

                if y >= 0 and y < self.korkeus and x >= 0 and x < self.korkeus:    # ensin loppupiste (yleensä)
                    if self.kartta[y][x] == 0:
                        print("x, y")
                        self.kartta[y][x] = 1     # huom!  [y][x]
                        self.loytyi_paikka = True
                        break
                    
                if y2 >= 0 and y2 < self.korkeus and x2 >= 0 and x2 < self.korkeus:  # sitten alkupiste (yleensä)
                    if self.kartta[y2][x2] == 0:
                        print("x2, y2")
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
                    break
        if not self.loytyi_paikka:
            while True:
                # random reunat:
                y = random.randint(0, self.korkeus -1)
                x = random.randint(0, self.leveys -1)
                if self.kartta[y][x] == 0:
                    self.kartta[y][x] = 1 
                    break

    """   TODO
    def onko_ykkosluokkaa_vaaka():
            ykkosluokkaa = False
            x_alku = self.alkupiste[0] -1
            x_loppu = self.loppupiste[0] +1
            y = self.alkupiste[1]
            if x_alku >= 0 and x_loppu < self.korkeus:
                if self.kartta[y][x_alku]  == 0 and self.kartta[y][x_loppu] == 0:
                    print("x_alku", x_alku, "x_loppu", x_loppu, y)
                    #print("kartta @ onko_ykkosluokkaa_vaaka:", self.kartta)
                    #print("kartta:", self.kartta[x_alku][y], self.kartta[x_loppu][y])
                    ykkosluokkaa = True
            return ykkosluokkaa
    """

    """ TODO:  nykyisin saattaa blokata ylh. alas / muun muodostuvan suoran
    def mahtuuko_5_vaaka(self, perakkaisia, alkupiste, loppupiste):   
            x_raja = 4 - perakkaisia
            #print(alkupiste[1], x_raja, self.leveys - loppupiste[1])   

            if alkupiste[1] < x_raja or self.leveys - loppupiste[1] < x_raja :
                return False
            return True     
    """

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
                        #if self.mahtuuko_5_vaaka(perakkaisia, alkupiste, loppupiste) or self.mahtuuko_5_pysty(perakkaisia, alkupiste, loppupiste):   
                        self.kaikki_suorat.append([perakkaisia, alkupiste, loppupiste])
                else:
                    perakkaisia = 0 

    """   TODO:  nykyisin saattaa blokata ylh. alas muodostuvan suoran
    def mahtuuko_5_pysty(self, perakkaisia, alkupiste, loppupiste):   
            y_raja = 4 - perakkaisia
            #print(alkupiste[0], y_raja, self.leveys - loppupiste[0])   

            if alkupiste[0] < y_raja or self.leveys - loppupiste[0] < y_raja :
                return False
            return True
    """

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
                    #    if self.mahtuuko_5_pysty(perakkaisia, alkupiste, loppupiste) or self.mahtuuko_5_vaaka(perakkaisia, alkupiste, loppupiste):  
                        self.kaikki_suorat.append([perakkaisia, alkupiste, loppupiste])
                else:
                    perakkaisia = 0 

    """ TODO:  nykyisin saattaa blokata toisen suoran
    def mahtuuko_5_d_oik(self, perakkaisia, alkupiste, loppupiste):   
            y_raja = 4 - perakkaisia
            x_raja = 4 - perakkaisia
            #print(alkupiste[0], y_raja, self.leveys - loppupiste[0])       # alkupiste = y, x

            if (alkupiste[0] < y_raja or self.korkeus - loppupiste[0] < y_raja) and (alkupiste[1] < x_raja or self.leveys - loppupiste[1] < x_raja) :
                return False
            return True
    """

    def diagonaali_oikealle(self):
        perakkaisia = 0  
        x_jatko = 0 
        y_jatko = 0     
        alkupiste = (4, 4)          # ekan robotin sijainti
        loppupiste = (4, 4)  
        for y in range(self.korkeus -3):
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
                                if (alku_x >= 0 or loppu_x < self.korkeus) and (alku_y >= 0 or loppu_y < self.korkeus) :
                                    #if self.mahtuuko_5_d_oik(perakkaisia, alkupiste, loppupiste) :   
                                    print(perakkaisia, alkupiste, loppupiste)
                                    self.kaikki_suorat.append([perakkaisia, alkupiste, loppupiste])                             
                                
                            y_jatko += 1
                            x_jatko += 1 
                else:
                    perakkaisia = 0 
            
