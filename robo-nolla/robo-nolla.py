import pygame


class RoboNolla:
    def __init__(self):
        pygame.init()
        
        self.lataa_kuvat()
        self.uusi_peli()
        
        self.korkeus = len(self.kartta)
        self.leveys = len(self.kartta[0])
        self.skaala = self.kuvat[0].get_width()
        self.alkupiste = (0, 0)
        self.loppupiste = (0, 0)

        nayton_korkeus = self.skaala * self.korkeus
        nayton_leveys = self.skaala * self.leveys
        self.naytto = pygame.display.set_mode((nayton_leveys, nayton_korkeus + self.skaala * 2))

        self.fontti_iso = pygame.font.SysFont("Arial", 25)
        self.fontti_pieni = pygame.font.SysFont("Arial", 22)

        pygame.display.set_caption("RoboNolla")
        self.silmukka()

    def lataa_kuvat(self):
        self.kuvat = []
        for nimi in ["tyhja", "robo", "nolla"]:
            self.kuvat.append(pygame.image.load(nimi + ".png"))


    def uusi_peli(self):
        self.kartta = []
        for i in range(8):
            self.kartta.append([0, 0, 0, 0, 0, 0, 0, 0])
        self.siirrot = 0
        self.vuorossa = "robo"

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
                if self.vuorossa == "robo":
                    self.kartta[self.rivi][self.sarake] = 1   # ["tyhja", "robo", "nolla"]
                    self.vuorossa = "nolla"
                else:
                    self.kartta[self.rivi][self.sarake] = 2
                    self.vuorossa = "robo"

            elif tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_F2:
                    self.uusi_peli()

            if tapahtuma.type == pygame.QUIT:
                exit()
   

    def piirra_naytto(self):
        self.naytto.fill((0, 0, 0))

        for y in range(self.korkeus):
            for x in range(self.leveys):
                ruutu = self.kartta[y][x]
                self.naytto.blit(self.kuvat[ruutu], (x * self.skaala, y * self.skaala))

        teksti = self.fontti_pieni.render("Neljä samaa voittaa", True, (65, 200, 55))
        self.naytto.blit(teksti, (85, self.korkeus * self.skaala + 20))

        teksti = self.fontti_pieni.render(f"Vuoro: {self.vuorossa}", True, (255, 0, 0))
        self.naytto.blit(teksti, (25, self.korkeus * self.skaala + 60))

        teksti = self.fontti_pieni.render("F2 = uusi peli", True, (255, 0, 0))
        self.naytto.blit(teksti, (199, self.korkeus * self.skaala + 60))

        lapi, lapi_teksti = self.peli_lapi()
        if lapi:
            teksti = self.fontti_iso.render(lapi_teksti, True, (255, 0, 0))
            teksti_x = self.skaala * self.leveys / 2 - teksti.get_width() / 2
            teksti_y = self.skaala * self.korkeus / 2 - teksti.get_height() / 2
            pygame.draw.rect(self.naytto, (0, 0, 0), (teksti_x, teksti_y, teksti.get_width(), teksti.get_height()))
            self.naytto.blit(teksti, (teksti_x, teksti_y))

            alku_x = self.alkupiste[0] * self.skaala
            alku_y = self.alkupiste[1] * self.skaala + (self.skaala//2)
            loppu_x = self.loppupiste[0] * self.skaala + self.skaala 
            loppu_y = self.loppupiste[1] * self.skaala + (self.skaala//2)
            pygame.draw.line(self.naytto, (0, 0, 0), (alku_x, alku_y ), (loppu_x, loppu_y), 4)

        pygame.display.flip()


    def peli_lapi(self):
        alkupiste = []     # piirretään voittoviiva

        def onko_vaaka(pelaaja):
            perakkaisia = 0
            alkupiste = []              
            for y in range(self.korkeus):
                for x in range(self.leveys):
                    if self.kartta[y][x] == pelaaja:
                        perakkaisia += 1
                        if perakkaisia == 1:
                            alkupiste.append((x, y))
                        if perakkaisia == 4:
                            self.alkupiste = alkupiste[0]
                            self.loppupiste = (x, y)                            
                            return True
                    else:
                        perakkaisia = 0    
            return False    

        def onko_pysty(pelaaja):
            perakkaisia = 0
            alkupiste = []  
            for y in range(self.korkeus):
                for x in range(self.leveys):
                    if self.kartta[x][y] == pelaaja:
                        perakkaisia += 1
                        if perakkaisia == 1:
                            alkupiste.append((y, x))
                        if perakkaisia == 4:
                            self.alkupiste = alkupiste[0]
                            self.loppupiste = (y, x)   
                            return True
                    else:
                        perakkaisia = 0    
            return False    

        def onko_diagonaali(pelaaja):
            perakkaisia = 0
            alkupiste = []  
            x_jatko = 0
            y_jatko = 0
            for y in range(self.korkeus - 3):   # 4 sarja vika mahdollisuus alkaa
                for x in range(self.leveys):
                    if self.kartta[y][x] == pelaaja:
                        x_jatko = x 
                        y_jatko = y      
                        for i in range(3):   # oik. alas   
                            if x_jatko < len(self.kartta) -1:                           
                                if self.kartta[y_jatko+1][x_jatko+1] == pelaaja:     
                                    print(x_jatko+1, y_jatko+1)                           
                                    perakkaisia += 1
                                    y_jatko += 1
                                    x_jatko += 1
                                else:
                                    perakkaisia = 0   
                                if perakkaisia == 1:
                                    alkupiste.append((x, y))
                                if perakkaisia == 3:
                                    self.alkupiste = alkupiste[0]
                                    self.loppupiste = (x, y)   
                                    return True

                        y_jatko = y   # vas. alas
                        x_jatko = x
                        for i in range(3):   
                            if self.kartta[y_jatko+1][x_jatko-1] == pelaaja:                                
                                perakkaisia += 1        
                                y_jatko += 1
                                x_jatko -= 1
                            else:
                                perakkaisia = 0   
                            if perakkaisia == 1:
                                alkupiste.append((x, y))
                            if perakkaisia == 3:
                                self.alkupiste = alkupiste[0]
                                self.loppupiste = (x, y)   
                                return True
                    else:
                        perakkaisia = 0   
            return False  

        if onko_vaaka(1) or onko_pysty(1) or onko_diagonaali(1):   # ["tyhja", "robo", "nolla"]
            return True, "Robo voitti"

        if onko_vaaka(2) or onko_pysty(2) or onko_diagonaali(2):   # ["tyhja", "robo", "nolla"]
            return True, "Nolla voitti"
        
        return False, ""


if __name__ == "__main__":
    RoboNolla()