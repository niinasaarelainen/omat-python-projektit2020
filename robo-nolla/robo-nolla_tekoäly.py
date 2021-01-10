import pygame
from ai import *


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
        self.pisteet = []
        self.viivansuunta = "" 
        self.montako_kerataan  = 5

        self.ai = Ai(self.korkeus, self.leveys)         # luodaan tekoäly
  

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
        for i in range(10):
            self.kartta.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.siirrot = 0
        self.kartta[4][4] = 1
        self.vuorossa = "nolla"

        

    def silmukka(self):
        while True:
            self.tutki_tilanne()            
            self.piirra_naytto()
    

    def tutki_tilanne(self):          

        if self.vuorossa == "robo":
            self.vuorossa = "nolla"

            # estetään nollan neljän suorat....
            self.pisteet = []
            lapi4, lapi_teksti = self.peli_lapi(4)    
            print(self.pisteet)


            for piste in self.pisteet:
                self.alkupiste = piste[0]
                self.loppupiste = piste[1]
                if not self.pisteet == [] :
                    print("  4:   self.alkupiste", self.alkupiste, "self.loppupiste", self.loppupiste )  
                    if self.ai.esta_4_tai_3(self.alkupiste, self.loppupiste, self.kartta):    
                        print("4 suoritettu")
                        self.kartta = self.ai.anna_kartta()
                        return
            
            # estetään nollan kolmen suorat....
            self.pisteet = []
            lapi3, lapi_teksti = self.peli_lapi(3)    


            ### testing
            self.pisteet = sorted(self.pisteet, key=lambda piste: piste[2])   # True / False
            print(self.pisteet)


            for piste in self.pisteet:
                self.alkupiste = piste[0]
                self.loppupiste = piste[1]       
                print("      3 :self.alkupiste", self.alkupiste, "self.loppupiste", self.loppupiste )  
                if self.ai.esta_4_tai_3(self.alkupiste, self.loppupiste, self.kartta):                        
                    print("3 suoritettu")
                    self.kartta = self.ai.anna_kartta()
                    print(self.kartta)
                    return 

            # ... tai laitetaan robo parhaimpaan paikkaan
            print( " ai.tutki \n")
            self.ai.tutki(self.kartta)                    
            

        if self.vuorossa == "nolla":
            self.tutki_tapahtumat()   # vain nollan vuorossa tutkitaan hiiren tapahtumat


    def tutki_tapahtumat(self):
        
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                x = tapahtuma.pos[0]
                y = tapahtuma.pos[1]
                self.sarake  = x // self.skaala
                self.rivi  = y // self.skaala
                if self.kartta[self.rivi][self.sarake] == 0:
                    self.kartta[self.rivi][self.sarake] = 2
                    self.vuorossa = "robo"

            elif tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_F2:
                    self.uusi_peli()                    
                    self.ai.nollaa()

            if tapahtuma.type == pygame.QUIT:
                exit()
   

    def piirra_naytto(self):
        self.naytto.fill((0, 0, 0))

        for y in range(self.korkeus):
            for x in range(self.leveys):
                ruutu = self.kartta[y][x]
                self.naytto.blit(self.kuvat[ruutu], (x * self.skaala, y * self.skaala))

        teksti = self.fontti_pieni.render("Viisi samaa voittaa", True, (65, 200, 55))
        self.naytto.blit(teksti, (115, self.korkeus * self.skaala + 25))

        teksti = self.fontti_pieni.render(f"Vuoro: {self.vuorossa}", True, (255, 0, 0))
        self.naytto.blit(teksti, (55, self.korkeus * self.skaala + 60))

        teksti = self.fontti_pieni.render("F2 = uusi peli", True, (255, 0, 0))
        self.naytto.blit(teksti, (250, self.korkeus * self.skaala + 60))

        """
        lapi, lapi_teksti = self.peli_lapi(self.montako_kerataan)
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
        """
        pygame.display.flip()

    

    def peli_lapi(self, montako):
        self.alkupiste = (0, 0)
        self.loppupiste = (0, 0)

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

        def onko_vaaka(pelaaja):
            perakkaisia = 0
            alkupiste = []        # piirretään voittoviiva        
            for y in range(self.korkeus):
                for x in range(self.leveys):
                    if self.kartta[y][x] == pelaaja:
                        perakkaisia += 1
                        if perakkaisia == 1:
                            alkupiste.append((x, y))
                        if perakkaisia == montako:
                            self.alkupiste = alkupiste[0]
                            self.loppupiste = (x, y)   
                            if montako == self.montako_kerataan :
                                self.viivansuunta = "vaaka"                         
                                return True
                            else:     
                                self.pisteet.append([self.alkupiste, self.loppupiste,  onko_ykkosluokkaa_vaaka()])    # !!!!!!
                                self.alkupiste = (0, 0)
                                self.loppupiste = (0, 0)
                                perakkaisia = 0  
                                alkupiste = []
                    else:
                        perakkaisia = 0   
                        alkupiste = []   
                perakkaisia = 0    # muuten vaakasuora voi jatkua riviltä toiselle !
                alkupiste = []
            return False    

        def onko_ykkosluokkaa_pysty():
            ykkosluokkaa = False
            y_alku = self.alkupiste[1] -1
            y_loppu = self.loppupiste[1] +1
            x = self.alkupiste[0]
            if y_alku >= 0 and y_alku < self.korkeus:
                if self.kartta[y_alku][x]  == 0 and self.kartta[y_loppu][x] == 0:
                    ykkosluokkaa = True
            return ykkosluokkaa

        def onko_pysty(pelaaja):
            perakkaisia = 0
            alkupiste = []  
            for y in range(self.korkeus):
                for x in range(self.leveys):
                    if self.kartta[x][y] == pelaaja:
                        perakkaisia += 1
                        if perakkaisia == 1:
                            alkupiste.append((y, x))
                        if perakkaisia == montako:
                            self.alkupiste = alkupiste[0]
                            self.loppupiste = (y, x) 
                            if montako == self.montako_kerataan :     
                                self.viivansuunta = "pysty"  
                                return True
                            else:
                                self.pisteet.append([self.alkupiste, self.loppupiste, onko_ykkosluokkaa_pysty()])
                                self.alkupiste = (0, 0)
                                self.loppupiste = (0, 0)
                                perakkaisia = 0  
                                alkupiste = []
                    else:
                        perakkaisia = 0    
                        alkupiste = []  
                perakkaisia = 0
                alkupiste = []
            return False    

        def onko_diagonaali_oikealle(pelaaja):
            perakkaisia = 0
            alkupiste = []  
            x_jatko = 0
            y_jatko = 0
            for y in range(self.korkeus - montako):       # oli -1
                for x in range(self.leveys):
                    if self.kartta[y][x] == pelaaja:
                        x_jatko = x 
                        y_jatko = y      
                        for i in range(montako -1):   # oik. alas   
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
                                if perakkaisia == montako -1:  # -1 eri laskusysteemi kuin pysty-vaaka
                                    self.alkupiste = alkupiste[0]
                                    self.loppupiste = (x_jatko, y_jatko)
                                    if montako == self.montako_kerataan : 
                                        self.viivansuunta = "diagonaali"     
                                        return True
                                    else:
                                        self.pisteet.append([self.alkupiste, self.loppupiste, False])    # TODO
                                        self.alkupiste = (0, 0)
                                        self.loppupiste = (0, 0)
                                        perakkaisia = 0  
                                        alkupiste = []
                    else:
                        perakkaisia = 0   
                        alkupiste = []
                perakkaisia = 0
                alkupiste = []
            return False  


        def onko_diagonaali_vasemmalle(pelaaja):
            perakkaisia = 0
            alkupiste = []  
            x_jatko = 0
            y_jatko = 0
            for y in range(self.korkeus - montako):     # oli -1
                for x in range(self.leveys):
                    if self.kartta[y][x] == pelaaja:
                        y_jatko = y   # vas. alas
                        x_jatko = x
                        for i in range(montako -1):   
                            if self.kartta[y_jatko+1][x_jatko-1] == pelaaja:                                
                                perakkaisia += 1        
                                y_jatko += 1
                                x_jatko -= 1
                            else:
                                perakkaisia = 0   
                                alkupiste = []   
                            if perakkaisia == 1:
                                alkupiste.append((x, y))
                            if perakkaisia == montako -1:   # -1 eri laskusysteemi kuin pysty-vaaka
                                self.alkupiste = alkupiste[0]
                                self.loppupiste = (x_jatko, y_jatko) 
                                if montako == self.montako_kerataan :
                                    self.viivansuunta = "diagonaali"    
                                    return True
                                else:                                    
                                    self.pisteet.append([self.alkupiste, self.loppupiste, False])   # TODO
                                    self.alkupiste = (0, 0)
                                    self.loppupiste = (0, 0)
                                    perakkaisia = 0 
                                    alkupiste = [] 
                    else:
                        perakkaisia = 0   
                        alkupiste = []
                perakkaisia = 0
                alkupiste = []
            return False  

        # ["tyhja", "robo", "nolla"]
        if onko_vaaka(2) or onko_pysty(2) or onko_diagonaali_oikealle(2) or onko_diagonaali_vasemmalle(2):   
            return True, "Nolla voitti"

        if montako == self.montako_kerataan and (onko_vaaka(1) or onko_pysty(1) or onko_diagonaali_oikealle(1) or onko_diagonaali_vasemmalle(1)):  
            return True, "Robo voitti"        
        
        return False, ""


if __name__ == "__main__":
    RoboNolla()