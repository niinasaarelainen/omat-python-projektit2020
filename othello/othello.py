import pygame
from vakiot import *


class Othello:
    def __init__(self):
        pygame.init()
        self.uusi_peli()
        
        self.korkeus = len(self.kartta)  
        self.leveys = len(self.kartta[0])
        self.skaala = 56

        self.nayton_korkeus = self.skaala * self.korkeus + REUNAN_KOKO
        self.nayton_leveys = self.skaala * self.leveys + REUNAN_KOKO
        self.naytto = pygame.display.set_mode((self.nayton_leveys, self.nayton_korkeus + 60)) # tekstikenttä alhaalla

        self.fontti_iso = pygame.font.SysFont("Arial", 25)
        self.fontti_pieni = pygame.font.SysFont("Arial", 22)

        pygame.display.set_caption("Othello")
        self.silmukka()
    


    def uusi_peli(self):
        self.kartta = []
        for i in range(3):
            self.kartta.append([0, 0, 0, 0, 0, 0, 0, 0])
        self.kartta.append([0, 0, 0, PUNAINEN, SININEN, 0, 0, 0])
        self.kartta.append([0, 0, 0, SININEN, PUNAINEN, 0, 0, 0])
        for i in range(3):
            self.kartta.append([0, 0, 0, 0, 0, 0, 0, 0])
        self.siirrot = 0
        self.vuorossa = PUNAINEN

    def silmukka(self):
        while True:
            self.tutki_tapahtumat()
            self.piirra_naytto()            

    def laillinen(self, sarake, rivi):
        #vieressä vastustaja:
        aloitussarake = max(sarake - 1, 0)
        aloitusrivi = max(rivi - 1, 0)
        vastustaja = PUNAINEN
        if self.vuorossa == PUNAINEN:
            vastustaja = SININEN
        laillinen = False
        vastustajien_sijainnit = []
        for x in range(3):
            for y in range(3): 
                if self.kartta[min(aloitusrivi, len(self.kartta) - 1)][min(aloitussarake, len(self.kartta) - 1)] == vastustaja:
                    laillinen = True
                    vastustajien_sijainnit.append((min(aloitusrivi, len(self.kartta) - 1), min(aloitussarake, len(self.kartta) - 1)))
                aloitusrivi += 1
                print("aloitusrivi:", aloitusrivi, "aloitussarake", aloitussarake)
            aloitussarake += 1
            aloitusrivi = max(rivi - 1, 0)

        # oma väri tulee vastaan
        print(vastustajien_sijainnit)
        return laillinen

    def tutki_tapahtumat(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                x = tapahtuma.pos[0]
                y = tapahtuma.pos[1]
                self.sarake  =  x // self.skaala
                self.rivi  = y // self.skaala
                if self.kartta[self.rivi][self.sarake] == 0 and self.laillinen(self.sarake, self.rivi):
                    if self.vuorossa == PUNAINEN:
                        self.kartta[self.rivi][self.sarake] = PUNAINEN   # ["tyhja", PUNAINEN, SININEN]
                        self.vuorossa = SININEN
                    else:
                        self.kartta[self.rivi][self.sarake] = SININEN
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
                vari = self.kartta[y][x]
                if vari == SININEN or vari == PUNAINEN:
                    pygame.draw.circle(self.naytto, vari[0], (x*self.skaala + P_KOKO + REUNAN_KOKO, y*self.skaala + P_KOKO + REUNAN_KOKO), P_KOKO)  

        teksti = self.fontti_pieni.render(f"Vuorossa: {self.vuorossa[1]}", True, self.vuorossa[0])
        self.naytto.blit(teksti, (33, self.nayton_korkeus + 20))

        teksti = self.fontti_pieni.render("F2 = uusi peli", True, self.vuorossa[0])
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
        kello.tick(1000)   


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

        if onko_vaaka(PUNAINEN) or onko_pysty(PUNAINEN) or onko_diagonaali(PUNAINEN):   # ["tyhja", PUNAINEN, SININEN]
            return True, "punainen voitti"

        if onko_vaaka(SININEN) or onko_pysty(SININEN) or onko_diagonaali(SININEN):   # ["tyhja", PUNAINEN, SININEN]
            return True, "sininen voitti"
        
        return False, ""


if __name__ == "__main__":
    Othello()