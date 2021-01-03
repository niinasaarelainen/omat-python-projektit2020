class Ai:

    def __init__(self, korkeus, leveys, kartta):
        self.pisin_suora = {"vaaka": [], "pysty":[], "diag_oikealle":[], "diag_vasemmalle":[]} 
        self.korkeus = korkeus
        self.leveys = leveys
        self.kartta = kartta
        self.tutki()


    def tutki(self):
        self.vaaka()
        self.pysty()
        s = sorted(self.pisin_suora.items(), key=lambda x: x[1], reverse = True)              

        while True:
            kokelas = s[0][1]   # pelkkä lista
            print(kokelas)
            
            if self.kartta[kokelas[2][0]][kokelas[2][1]] == 0:
                self.kartta[kokelas[2][0]][kokelas[2][1]] = 1     # huom!  [y][x]
                break
            elif self.kartta[kokelas[1][0]][kokelas[1][1]] == 0:
                self.kartta[kokelas[1][0]][kokelas[1][1]] = 1
                break
            s.pop(0)
            print(s)


    def vaaka(self):
            perakkaisia = 0  
            perakkaisia_ennatys = 0   
            alkupiste = (3, 3)          # ekan robotin sijainti
            loppupiste = (3, 3)  
            for y in range(self.korkeus):
                for x in range(self.leveys):
                    if self.kartta[y][x] == 1:             # robotti = 1
                        perakkaisia += 1
                        if perakkaisia == 1:
                            alkupiste = (y, x)
                        if perakkaisia > perakkaisia_ennatys :  
                            perakkaisia_ennatys += 1
                            loppupiste = (y, x)
                            print("loppupiste", loppupiste)
                    else:
                        perakkaisia = 0 

            # palautetaan potentiaaliset uudet sijainnit, tarkistukset myöhemmin:
            x = alkupiste[1] - 1
            alkupiste = (alkupiste[0], x)   # vaaka = vain x muuttuu
            x = loppupiste[1] + 1
            loppupiste = (loppupiste[0], x)
            self.pisin_suora["vaaka"] = [perakkaisia_ennatys, alkupiste, loppupiste]
            print("\nvaaka", self.pisin_suora["vaaka"])
           


    def pysty(self):
            perakkaisia = 0  
            perakkaisia_ennatys = 0   
            alkupiste = (3, 3)   
            loppupiste = (3, 3)  
            for x in range(self.korkeus):
                for y in range(self.leveys):
                    if self.kartta[y][x] == 1:             # robotti = 1
                        perakkaisia += 1
                        if perakkaisia == 1:
                            alkupiste = (y, x)
                        if perakkaisia > perakkaisia_ennatys : 
                            perakkaisia_ennatys += 1
                            loppupiste = (y, x)
                    else:
                        perakkaisia = 0 
                        perakkaisia_ennatys = 0   

            # palautetaan potentiaaliset uudet sijainnit, tarkistukset myöhemmin:
            y = alkupiste[0] - 1
            alkupiste = (y, alkupiste[1])   # pysty = vain y muuttuu
            y = loppupiste[0] + 1
            loppupiste = (y, loppupiste[1])
            self.pisin_suora["pysty"] = [perakkaisia_ennatys, alkupiste, loppupiste]
            print("pysty", self.pisin_suora["pysty"])

            
            
        