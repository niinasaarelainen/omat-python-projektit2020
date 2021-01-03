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
        print(s)

        kokelas = s[0][1]
        print(kokelas)
        """
        if self.kartta[loppupiste[0] + 1][loppupiste[1]] == 0:
                self.kartta[loppupiste[0] + 1][loppupiste[1]] = 1     # huom!  [y][x]
        """

    def vaaka(self):
            perakkaisia = 0  
            perakkaisia_ennatys = 0   
            alkupiste = (0, 0)   
            loppupiste = (0, 0)  
            for y in range(self.korkeus):
                for x in range(self.leveys):
                    if self.kartta[y][x] == 1:             # robotti = 1
                        perakkaisia += 1
                        if perakkaisia > perakkaisia_ennatys :                 
                            perakkaisia_ennatys += 1
                            alkupiste = (y, x)
                            loppupiste = (y, x)
                    else:
                        perakkaisia = 0 
            self.pisin_suora["vaaka"] = [perakkaisia_ennatys, alkupiste, loppupiste]
            print("vaaka", self.pisin_suora["vaaka"])
           


    def pysty(self):
            perakkaisia = 0  
            perakkaisia_ennatys = 0   
            alkupiste = (0, 0)   
            loppupiste = (0, 0)  
            for x in range(self.korkeus):
                for y in range(self.leveys):
                    if self.kartta[y][x] == 1:             # robotti = 1
                        perakkaisia += 1
                        if perakkaisia > perakkaisia_ennatys :                 
                            perakkaisia_ennatys += 1
                            alkupiste = (y, x)
                            loppupiste = (y, x)
                    else:
                        perakkaisia = 0 
            self.pisin_suora["pysty"] = [perakkaisia_ennatys, alkupiste, loppupiste]
            print("pysty", self.pisin_suora["pysty"])

            
            
        