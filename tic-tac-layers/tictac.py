import pygame


class TicTac:
    def __init__(self):
        pygame.init()
        self.CLOCK = pygame.time.Clock()
        
        self.lataa_kuvat()
        self.uusi_peli()
        
        self.korkeus = len(self.kartta)
        self.leveys = len(self.kartta[0])
        self.skaala = self.kuvat[2].get_width()   # kolmantena isoin kuva
        self.alkupiste = (0, 0)
        self.loppupiste = (0, 0)
        self.viivansuunta = "" 

        nayton_korkeus = self.skaala * self.korkeus
        nayton_leveys = self.skaala * self.leveys
        self.naytto = pygame.display.set_mode((nayton_leveys, nayton_korkeus + self.skaala * 2))
        

        self.fontti_iso = pygame.font.SysFont("Arial", 25)
        self.fontti_pieni = pygame.font.SysFont("Arial", 22)

        pygame.display.set_caption("RoboNolla")
        self.silmukka()

    def lataa_kuvat(self):
        self.kuvat = []
        kuva = pygame.image.load("tyhja.png")  
        self.kuvat.append(pygame.transform.scale(kuva, (80, 80))) 
        for i in range(1,3):
            kuva = pygame.image.load("maatuska" + str(i) + ".png")   #1 = sininen, 2 = pun
            self.kuvat.append(pygame.transform.scale(kuva, (40, 40))) 
            self.kuvat.append(pygame.transform.scale(kuva, (60, 60)))
            self.kuvat.append(pygame.transform.scale(kuva, (80, 80)))
        print(self.kuvat)


    def uusi_peli(self):
        self.kartta = []
        for i in range(3):
            self.kartta.append([0, 0, 0])
        self.siirrot = 0
        self.vuorossa = "maatuska1"

    def silmukka(self):
        while True:
            self.tutki_tapahtumat()
            self.piirra_naytto()


    def tutki_tapahtumat(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                x = tapahtuma.pos[0]
                y = tapahtuma.pos[1]
                self.sarake  = x // self.skaala
                self.rivi  = y // self.skaala
                if self.kartta[self.rivi][self.sarake] == 0:
                    if self.vuorossa == "maatuska1":
                        self.kartta[self.rivi][self.sarake] = 1   # ["tyhja", "maatuska1", "maatuska2"]
                        self.vuorossa = "maatuska2"
                    else:
                        self.kartta[self.rivi][self.sarake] = 2
                        self.vuorossa = "maatuska1"
                print(self.kartta)

            elif tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_F2:
                    self.uusi_peli()

            if tapahtuma.type == pygame.QUIT:
                exit()
   

    def piirra_naytto(self):
        self.naytto.fill((244, 244, 244))

        for y in range(self.korkeus):
            for x in range(self.leveys):
                ruutu = self.kartta[y][x]
                print(ruutu)
                if ruutu == 2:
                    ruutu += 2   # pienin punainen
                self.naytto.blit(self.kuvat[ruutu], (x * self.skaala, y * self.skaala))        

        teksti = self.fontti_pieni.render(f"Vuoro: {self.vuorossa}", True, (255, 0, 0))
        self.naytto.blit(teksti, (15, self.korkeus * self.skaala + 40))

        teksti = self.fontti_pieni.render("F2 = uusi peli", True, (255, 0, 0))
        self.naytto.blit(teksti, (15, self.korkeus * self.skaala + 70))

        lapi, lapi_teksti = self.peli_lapi()
        if lapi:
            teksti = self.fontti_iso.render(lapi_teksti, True, (255, 0, 0))
            teksti_x = self.skaala * self.leveys / 2 - teksti.get_width() / 2
            teksti_y = self.skaala * self.korkeus / 2 - teksti.get_height() / 2
            pygame.draw.rect(self.naytto, (0, 0, 0), (teksti_x, teksti_y, teksti.get_width(), teksti.get_height()))
            self.naytto.blit(teksti, (teksti_x, teksti_y))

            if self.viivansuunta == "vaaka":
                alku_x = self.alkupiste[0] * self.skaala
                alku_y = self.alkupiste[1] * self.skaala + (self.skaala//2)
                loppu_x = self.loppupiste[0] * self.skaala + self.skaala 
                loppu_y = self.loppupiste[1] * self.skaala + (self.skaala//2)
                pygame.draw.line(self.naytto, (0, 0, 0), (alku_x, alku_y ), (loppu_x, loppu_y), 4)
            elif self.viivansuunta == "pysty":
                alku_x = self.alkupiste[0] * self.skaala + (self.skaala//2)
                alku_y = self.alkupiste[1] * self.skaala 
                loppu_x = self.loppupiste[0] * self.skaala + (self.skaala//2)
                loppu_y = self.loppupiste[1] * self.skaala + self.skaala
                pygame.draw.line(self.naytto, (0, 0, 0), (alku_x, alku_y ), (loppu_x, loppu_y), 4)
            elif self.viivansuunta == "diagonaali":
                alku_x = self.alkupiste[0] * self.skaala 
                alku_y = self.alkupiste[1] * self.skaala 
                loppu_x = self.loppupiste[0] * self.skaala + self.skaala
                loppu_y = self.loppupiste[1] * self.skaala + self.skaala
                pygame.draw.line(self.naytto, (0, 0, 0), (alku_x, alku_y ), (loppu_x, loppu_y), 4)
            

        pygame.display.flip()
        self.CLOCK.tick(2) 


    def peli_lapi(self):
        alkupiste = []     # piirretään voittoviiva

        def onko_vaaka(pelaaja):
            perakkaisia = 0         
            for y in range(self.korkeus):
                for x in range(self.leveys):
                    if self.kartta[y][x] == pelaaja:
                        if perakkaisia == 1:
                            alkupiste.append((y, x))
                        perakkaisia += 1    
                        if perakkaisia == 3:   
                            self.alkupiste = alkupiste[0]
                            self.loppupiste = (y, x) 
                            self.viivansuunta = "vaaka"               
                            return True
                        else:
                            perakkaisia = 0   
                            alkupiste = []   
            return False    

        def onko_pysty(pelaaja):
            perakkaisia = 0
            for y in range(self.korkeus):
                for x in range(self.leveys):
                    if self.kartta[x][y] == pelaaja:
                        perakkaisia += 1
                        if perakkaisia == 1:
                            alkupiste.append((y, x))
                        if perakkaisia == 3:
                            self.alkupiste = alkupiste[0]
                            self.loppupiste = (y, x) 
                            self.viivansuunta = "pysty"  
                            return True
                    else:
                        perakkaisia = 0    
                        alkupiste = []  
            return False    

        def onko_diagonaali(pelaaja):
            perakkaisia = 0
            alkupiste = [] 
            #  diagonaali #1 oikealle:
            for i in range(3):
                if self.kartta[i][i] == pelaaja:
                    perakkaisia += 1
                    if perakkaisia == 1:
                        alkupiste.append((i, i))
                    if perakkaisia == 3:
                        self.alkupiste = alkupiste[0]
                        self.loppupiste = (i, i) 
                        self.viivansuunta = "diagonaali"  
                        return True
                else:
                    perakkaisia = 0    
                    alkupiste = []  
            #  diagonaali #2 vasemmalle:
            for i in range(3, 0):       # TODO  oikea synbtaksi !=!??!?
                if self.kartta[i][i] == pelaaja:
                    perakkaisia += 1
                    if perakkaisia == 1:
                        alkupiste.append((i, i))
                    if perakkaisia == 3:
                        self.alkupiste = alkupiste[0]
                        self.loppupiste = (i, i) 
                        self.viivansuunta = "diagonaali"  
                        return True
                else:
                    perakkaisia = 0    
                    alkupiste = []              
            return False  

        if onko_vaaka(1) or onko_pysty(1) or onko_diagonaali(1):   # ["tyhja", "robo", "nolla"]
            return True, "Sininen voitti"

        if onko_vaaka(2) or onko_pysty(2) or onko_diagonaali(2):   # ["tyhja", "robo", "nolla"]
            return True, "Punainen voitti"
        
        return False, ""


if __name__ == "__main__":
    TicTac()