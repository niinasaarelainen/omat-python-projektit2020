import pygame


class TicTac:
    def __init__(self):
        pygame.init()
        self.CLOCK = pygame.time.Clock()
        
        self.lataa_kuvat()
        self.uusi_peli()
        
        self.korkeus = len(self.kartta)
        self.leveys = len(self.kartta[0])
        self.skaala = self.kuvat[3].get_width() + 10  # kolmantena isoin kuva
        self.alkupiste = (0, 0)
        self.loppupiste = (0, 0)
        self.viivansuunta = ""         

        nayton_korkeus = self.skaala * self.korkeus
        nayton_leveys = self.skaala * self.leveys
        self.naytto = pygame.display.set_mode((nayton_leveys, nayton_korkeus + self.skaala * 2))
        self.varit = {"punainen": (255, 0, 0), "sininen": (0, 0, 255)}
        self.offsets = { 0: 5 , 1: 25,  2: 15, 3:5, 4: 25,  5: 15, 6:5}

        self.fontti_iso = pygame.font.SysFont("Arial", 25)
        self.fontti_pieni = pygame.font.SysFont("Arial", 20)

        pygame.display.set_caption("RoboNolla")
        self.varoitusteksti = self.fontti_pieni.render(f"Valitse ensin koko 1-3 !", True, self.varit[self.vuorossa])
        self.varoitus = False
        self.silmukka()

    def lataa_kuvat(self):
        self.kuvat = []
        kuva = pygame.image.load("tyhja.png")  
        self.kuvat.append(pygame.transform.scale(kuva, (78, 78))) 
        for i in range(1,3):
            kuva = pygame.image.load("maatuska" + str(i) + ".png")   #1 = sininen, 2 = pun
            self.kuvat.append(pygame.transform.scale(kuva, (40, 40))) 
            self.kuvat.append(pygame.transform.scale(kuva, (60, 60)))
            self.kuvat.append(pygame.transform.scale(kuva, (80, 80)))


    def uusi_peli(self):
        self.koko = -1 # = kokoa ei valittu, (koot 0-2) 
        self.kartta = []
        for i in range(3):
            self.kartta.append([0, 0, 0])
        self.siirrot = 0
        self.vuorossa = "sininen"
        self.pelaaja1_nappulat = [0, 0, 0, 1, 1, 1, 2, 2, 2]   # joka kokoa 3kpl
        self.pelaaja2_nappulat = [0, 0, 0, 1, 1, 1, 2, 2, 2]

    def silmukka(self):        
        while True:
            self.tutki_tapahtumat()
            self.piirra_naytto()


    def tutki_tapahtumat(self):        
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                if self.koko == -1:
                    self.varoitus = True
                    self.varoitus_y = tapahtuma.pos[1]
                else:                    
                    x = tapahtuma.pos[0]
                    y = tapahtuma.pos[1]
                    self.sarake  = x // self.skaala
                    self.rivi  = y // self.skaala
                    if self.vuorossa == "sininen"  and (self.kartta[self.rivi][self.sarake] in [0, 4, 5]): 
                        self.kartta[self.rivi][self.sarake] = 1 + self.koko  
                        while self.koko not in self.pelaaja1_nappulat:
                            self.tutki_tapahtumat()
                        self.pelaaja1_nappulat.remove(self.koko)
                        self.vuorossa = "punainen"
                    elif self.vuorossa == "punainen" and self.kartta[self.rivi][self.sarake] in [0, 1, 2]:
                        self.kartta[self.rivi][self.sarake] = 4 + self.koko
                        while self.koko not in self.pelaaja2_nappulat:
                            self.tutki_tapahtumat()
                        self.pelaaja2_nappulat.remove(self.koko)
                        self.vuorossa = "sininen"   
                self.koko = -1                                 

            elif tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_F2:
                    self.uusi_peli()                
                else:
                    self.varoitus = False
                    self.koko = tapahtuma.key - 49   
                    if self.vuorossa == "sininen":
                        if self.koko not in self.pelaaja1_nappulat: 
                            self.varoitusteksti = self.fontti_pieni.render(f"Tuota kokoa ei enää ole", True, self.varit[self.vuorossa])
                            self.varoitus = True
                    if self.vuorossa == "punainen":
                        if self.koko not in self.pelaaja2_nappulat: 
                            self.varoitusteksti = self.fontti_pieni.render(f"Tuota kokoa ei enää ole", True, self.varit[self.vuorossa])
                            self.varoitus = True
                    
                
            if tapahtuma.type == pygame.QUIT:
                exit()
   

    def piirra_naytto(self):        
        self.naytto.fill((244, 244, 244))
        for y in range(self.korkeus):
            for x in range(self.leveys):
                ruutu = self.kartta[y][x]
                kuva = self.kuvat[ruutu]
                offset = self.offsets[ruutu]
                self.naytto.blit(kuva, (x * self.skaala + offset, y * self.skaala + offset))        
               

        if self.varoitus:
            self.naytto.blit(self.varoitusteksti, (15, self.varoitus_y ))

        teksti = self.fontti_pieni.render(f"Vuoro: {self.vuorossa}", True, self.varit[self.vuorossa])
        self.naytto.blit(teksti, (15, self.korkeus * self.skaala + 40))

        teksti = self.fontti_pieni.render(f"1=pienin 2=keski 3=isoin", True,  self.varit[self.vuorossa])
        self.naytto.blit(teksti, (15, self.korkeus * self.skaala + 70))

        teksti = self.fontti_pieni.render("F2 = uusi peli", True, (255, 0, 220))
        self.naytto.blit(teksti, (15, self.korkeus * self.skaala + 100))

        lapi, lapi_teksti = self.peli_lapi()
        if lapi:
            teksti = self.fontti_iso.render(lapi_teksti, True, (255, 0, 0))
            teksti_x = self.skaala * self.leveys / 2 -15 - teksti.get_width() / 2
            teksti_y = self.skaala * self.korkeus / 2 - 15 - teksti.get_height() / 2
            pygame.draw.rect(self.naytto, (252, 252, 252), (teksti_x, teksti_y, teksti.get_width(), teksti.get_height()))
            self.naytto.blit(teksti, (teksti_x, teksti_y))

            if self.viivansuunta == "vaaka":
                alku_y = self.alkupiste[0] * self.skaala + (self.skaala//2)
                alku_x = self.alkupiste[1] * self.skaala 
                loppu_y = self.loppupiste[0] * self.skaala + (self.skaala//2)
                loppu_x = self.loppupiste[1] * self.skaala + self.skaala
                pygame.draw.line(self.naytto, (0, 0, 0), (alku_x, alku_y ), (loppu_x, loppu_y), 4)
            elif self.viivansuunta == "pysty":
                alku_x = self.alkupiste[0] * self.skaala + (self.skaala//2)
                alku_y = self.alkupiste[1] * self.skaala 
                loppu_x = self.loppupiste[0] * self.skaala + (self.skaala//2)
                loppu_y = self.loppupiste[1] * self.skaala + self.skaala
                pygame.draw.line(self.naytto, (0, 0, 0), (alku_x, alku_y ), (loppu_x, loppu_y), 4)
            elif self.viivansuunta == "diagonaali_vas":
                alku_y = self.alkupiste[0] * self.skaala 
                alku_x = self.alkupiste[1] * self.skaala + self.skaala
                loppu_y = self.loppupiste[0] * self.skaala + self.skaala
                loppu_x = self.loppupiste[1] * self.skaala 
                pygame.draw.line(self.naytto, (0, 0, 0), (alku_x, alku_y ), (loppu_x, loppu_y), 4)
            elif self.viivansuunta == "diagonaali_oik":
                alku_y = self.alkupiste[0] * self.skaala 
                alku_x = self.alkupiste[1] * self.skaala 
                loppu_y = self.loppupiste[0] * self.skaala + self.skaala
                loppu_x = self.loppupiste[1] * self.skaala + self.skaala
                pygame.draw.line(self.naytto, (0, 0, 0), (alku_x, alku_y ), (loppu_x, loppu_y), 4)
            

        pygame.display.flip()
        self.CLOCK.tick(1)    # ei saa olla desimaalia


    def peli_lapi(self):

        def onko_vaaka(numerot):
            perakkaisia = 0         
            for y in range(self.korkeus):
                for x in range(self.leveys):
                    if self.kartta[y][x] in numerot:
                        perakkaisia += 1  
                        if perakkaisia == 1:
                            self.alkupiste = (y, x)                        
                        if perakkaisia == 3:  
                            self.loppupiste = (y, x) 
                            self.viivansuunta = "vaaka"               
                            return True
                    else:
                        perakkaisia = 0 
                perakkaisia = 0 
            return False    

        def onko_pysty(numerot):
            perakkaisia = 0
            for y in range(self.korkeus):
                for x in range(self.leveys):
                    if self.kartta[x][y] in numerot:
                        perakkaisia += 1
                        if perakkaisia == 1:
                            self.alkupiste = (y, x)
                        if perakkaisia == 3:
                            self.loppupiste = (y, x) 
                            self.viivansuunta = "pysty"  
                            return True
                    else:
                        perakkaisia = 0   
                perakkaisia = 0 
            return False    

        def onko_diagonaali(numerot):
            perakkaisia = 0
            #  diagonaali #1 oikealle:
            for i in range(3):
                if self.kartta[i][i] in numerot:                    
                    perakkaisia += 1
                    if perakkaisia == 1:
                         self.alkupiste = (i, i)
                    if perakkaisia == 3: 
                        self.loppupiste = (i, i) 
                        self.viivansuunta = "diagonaali_oik"  
                        return True                        
                        
            #  diagonaali #2 vasemmalle:
            perakkaisia = 0 
            if self.kartta[0][2] in numerot and self.kartta[1][1] in numerot and self.kartta[2][0] in numerot:
                self.alkupiste = (0, 2)
                self.loppupiste = (2, 0) 
                self.viivansuunta = "diagonaali_vas"  
                return True         
            return False  

        if onko_vaaka([1,2,3]) or onko_pysty([1,2,3]) or onko_diagonaali([1,2,3]):   
            return True, "Sininen voitti"

        if onko_vaaka([4,5,6]) or onko_pysty([4,5,6]) or onko_diagonaali([4,5,6]):   
            return True, "Punainen voitti"
        
        return False, ""


if __name__ == "__main__":
    TicTac()