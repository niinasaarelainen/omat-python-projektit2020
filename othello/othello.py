import pygame
from vakiot import *


class Othello:
    def __init__(self):
        pygame.init()
        self.uusi_peli()
        
        self.korkeus = len(self.kartta)  # tekstikenttä alhaalla
        self.leveys = len(self.kartta[0])
        self.skaala = 57

        self.nayton_korkeus = self.skaala * self.korkeus
        self.nayton_leveys = self.skaala * self.leveys
        self.naytto = pygame.display.set_mode((self.nayton_leveys, self.nayton_korkeus + 60))

        self.fontti_iso = pygame.font.SysFont("Arial", 25)
        self.fontti_pieni = pygame.font.SysFont("Arial", 22)

        pygame.display.set_caption("Othello")
        self.silmukka()
    


    def uusi_peli(self):
        self.kartta = []
        for i in range(3):
            self.kartta.append([0, 0, 0, 0, 0, 0, 0, 0])
        self.kartta.append([0, 0, 0, 1, 2, 0, 0, 0])
        self.kartta.append([0, 0, 0, 2, 1, 0, 0, 0])
        for i in range(3):
            self.kartta.append([0, 0, 0, 0, 0, 0, 0, 0])
        self.siirrot = 0
        self.vuorossa = PUNAINEN

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
                    if self.vuorossa == PUNAINEN:
                        self.kartta[self.rivi][self.sarake] = 1   # ["tyhja", PUNAINEN, SININEN]
                        self.vuorossa = SININEN
                    else:
                        self.kartta[self.rivi][self.sarake] = 2
                        self.vuorossa = PUNAINEN

            elif tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_F2:
                    self.uusi_peli()

            if tapahtuma.type == pygame.QUIT:
                exit()
   

    def piirra_naytto(self):
        self.naytto.blit(lauta, (0,0))

        for y in range(self.korkeus):
            for x in range(self.leveys):
                ruutu = self.kartta[y][x]
                pygame.draw.circle(self.naytto, self.vuorossa[0], (x, y), P_KOKO)  

        teksti = self.fontti_pieni.render(f"Vuorossa: {self.vuorossa[1]}", True, (255, 0, 0))
        self.naytto.blit(teksti, (33, self.nayton_korkeus + 20))

        teksti = self.fontti_pieni.render("F2 = uusi peli", True, (255, 0, 0))
        self.naytto.blit(teksti, (300, self.nayton_korkeus + 20))

        """
        lapi, lapi_teksti = self.peli_lapi()
        if lapi:
            teksti = self.fontti_iso.render(lapi_teksti, True, (255, 0, 0))
            teksti_x = self.skaala * self.leveys / 2 - teksti.get_width() / 2
            teksti_y = self.skaala * self.korkeus / 2 - teksti.get_height() / 2
            pygame.draw.rect(self.naytto, (0, 0, 0), (teksti_x, teksti_y, teksti.get_width(), teksti.get_height()))
            self.naytto.blit(teksti, (teksti_x, teksti_y))    """        

        pygame.display.flip()


    def peli_lapi(self):

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
                        alkupiste = []   
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
                        alkupiste = []  
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
                                    perakkaisia += 1
                                    y_jatko += 1
                                    x_jatko += 1
                                else:
                                    perakkaisia = 0   
                                    alkupiste = []   
                                if perakkaisia == 1:
                                    alkupiste.append((x, y))
                                if perakkaisia == 3:
                                    self.alkupiste = alkupiste[0]
                                    self.loppupiste = (x_jatko, y_jatko)
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
                                alkupiste = []   
                            if perakkaisia == 1:
                                alkupiste.append((x, y))
                            if perakkaisia == 3:
                                a_x, a_y = alkupiste[0]
                                self.alkupiste = (a_x + 1, a_y)
                                self.loppupiste = (x_jatko -1, y_jatko)   
                                return True
                    else:
                        perakkaisia = 0   
            return False  

        if onko_vaaka(1) or onko_pysty(1) or onko_diagonaali(1):   # ["tyhja", PUNAINEN, SININEN]
            return True, "punainen voitti"

        if onko_vaaka(2) or onko_pysty(2) or onko_diagonaali(2):   # ["tyhja", PUNAINEN, SININEN]
            return True, "sininen voitti"
        
        return False, ""


if __name__ == "__main__":
    Othello()