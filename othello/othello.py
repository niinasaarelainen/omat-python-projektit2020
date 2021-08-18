import pygame, time
from vakiot import *


class Othello:
    def __init__(self):
        pygame.init()
        self.uusi_peli()
        
        self.korkeus = len(self.kartta)  
        self.leveys = len(self.kartta[0])
        self.skaala = 56
        self.vaihda_vari = []

        self.nayton_korkeus = self.skaala * self.korkeus + REUNAN_KOKO
        self.nayton_leveys = self.skaala * self.leveys + REUNAN_KOKO
        self.naytto = pygame.display.set_mode((self.nayton_leveys, self.nayton_korkeus + 60)) # tekstikenttä alhaalla

        self.fontti_iso = pygame.font.SysFont("Arial", 25)
        self.fontti_pieni = pygame.font.SysFont("Arial", 22)

        pygame.display.set_caption("Othello")
        self.silmukka()    


    def uusi_peli(self):
        self.kartta = []
        
        """
        for i in range(8):
             self.kartta.append([PUNAINEN, PUNAINEN, PUNAINEN, PUNAINEN, SININEN, PUNAINEN, PUNAINEN, PUNAINEN])

        """
        for i in range(3):
            #self.kartta.append([0, 0, 0, 0, 0, 0, 0, 0])
            self.kartta.append([PUNAINEN, PUNAINEN, PUNAINEN, PUNAINEN, SININEN, PUNAINEN, PUNAINEN, PUNAINEN])

        self.kartta.append([0, 0, 0, PUNAINEN, SININEN, 0, 0, 0])
        self.kartta.append([0, 0, 0, SININEN, PUNAINEN, 0, 0, 0])
        for i in range(3):
            #self.kartta.append([0, 0, 0, 0, 0, 0, 0, 0])
            self.kartta.append([PUNAINEN, PUNAINEN, PUNAINEN, PUNAINEN, SININEN, PUNAINEN, PUNAINEN, PUNAINEN])

        
        self.siirrot = 0
        self.vuorossa = PUNAINEN


    def silmukka(self):
        while True:
            self.tutki_tapahtumat()
            self.piirra_naytto()            

    def laillinen(self, sarake, rivi):

        print()

        #vieressä vastustaja:
        aloitussarake = sarake - 1
        aloitusrivi = rivi - 1
        vastustaja = PUNAINEN
        if self.vuorossa == PUNAINEN:
            vastustaja = SININEN
        laillinen_vastustaja = False
        vastustajien_sijainnit = []
        for x in range(3):   # TODO ylin rivi !! ei saa tehdä 3 riviä alasp.
            for y in range(3): 
                if  0 <= aloitusrivi < len(self.kartta) and 0 <= aloitussarake < len(self.kartta) and self.kartta[min(aloitusrivi, len(self.kartta) - 1)][min(aloitussarake, len(self.kartta) - 1)] == vastustaja:
                    laillinen_vastustaja = True
                    print(aloitusrivi, aloitussarake)
                    vastustajien_sijainnit.append((min(aloitusrivi, len(self.kartta) - 1), min(aloitussarake, len(self.kartta) - 1)))
                aloitusrivi += 1
            aloitussarake += 1
            aloitusrivi = max(rivi - 1, 0)

        # oma väri tulee vastaan
          # ei tiedä nappulan tutkintahetkellä onko siirto laillinen
        laillinen_oma_tulee_vastaan = False
        for y, x in vastustajien_sijainnit:    
            vaihda_vari_temp = [] 
            suunta_x =  x - sarake
            
            if  suunta_x > 0 :
                aloitussarake = max(sarake + suunta_x, 0)
            elif suunta_x == 0:
                aloitussarake = sarake
            else:
                aloitussarake = min(sarake + suunta_x, len(self.kartta) - 1)

            suunta_y =  y - rivi   
            if  suunta_y > 0 :
                aloitusrivi = max(rivi + suunta_y, 0)
            elif suunta_y == 0:
                aloitusrivi = rivi
            else:
                aloitusrivi = min(rivi + suunta_y, len(self.kartta) - 1)

            """
            print("vastustaja: y", y, "x", x) 
            print("pelaaja: rivi", rivi, "sarake", sarake)
            print("suunta_y", suunta_y, "suunta_x", suunta_x)       """                     
            
            for x in range(7):
                while  0 <= aloitusrivi <= len(self.kartta) - 1 and 0 <= aloitussarake <= len(self.kartta) - 1:
                    #print("aloitusrivi:", aloitusrivi, "aloitussarake", aloitussarake)
                    if self.kartta[aloitusrivi][aloitussarake] == self.vuorossa:
                        laillinen_oma_tulee_vastaan = True
                        for y, x in vaihda_vari_temp:
                            self.vaihda_vari.append((y, x))
                            #print("self.vaihda_vari.append((y, x))", y, x)   
                        break                     
                        # return laillinen_vastustaja and laillinen_oma_tulee_vastaan
                    else: 
                        vaihda_vari_temp.append((aloitusrivi,aloitussarake))
                    aloitusrivi += suunta_y
                    aloitussarake += suunta_x

        return laillinen_vastustaja and laillinen_oma_tulee_vastaan


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
                        self.kaanna()     # tämän voi tehdä vasta kun kääntämisyritys on todettu lailliseksi                 
                        self.vuorossa = SININEN
                    else:
                        self.kartta[self.rivi][self.sarake] = SININEN
                        self.kaanna()  
                        self.vuorossa = PUNAINEN            

            elif tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_F2:
                    self.uusi_peli()
                elif tapahtuma.key == pygame.K_F5:                   
                    if self.vuorossa == SININEN:
                        self.vuorossa = PUNAINEN
                    else:
                         self.vuorossa = SININEN

            if tapahtuma.type == pygame.QUIT:
                exit()

        if self.peli_lapiko():
            print("peli_lapi")
            if self.vuorossa == SININEN:
                self.vuorossa = PUNAINEN
            else:
                self.vuorossa = SININEN
            self.peli_lapi()
            self.uusi_peli()


    def peli_lapiko(self):
        for rivi in self.kartta:
            if 0 in rivi:
                return False
        return True


    def kaanna(self):
        for y, x in self.vaihda_vari:
            self.kartta[y][x] = self.vuorossa
        self.vaihda_vari = []
   

    def piirra_naytto(self):
        self.naytto.blit(lauta, (0,0))        

        for y in range(self.korkeus):
            for x in range(self.leveys):
                vari = self.kartta[y][x]
                if vari == SININEN or vari == PUNAINEN:
                    pygame.draw.circle(self.naytto, vari[0], (x*self.skaala + P_KOKO + REUNAN_KOKO, y*self.skaala + P_KOKO + REUNAN_KOKO), P_KOKO)  

        

        teksti = self.fontti_pieni.render(f"Vuoro: {self.vuorossa[1]}", True, self.vuorossa[0])
        self.naytto.blit(teksti, (25, self.nayton_korkeus + 20))

        teksti = self.fontti_pieni.render("F5 = en pysty siirtämään", True, self.vuorossa[0])
        self.naytto.blit(teksti, (210, self.nayton_korkeus + 8))     

        teksti = self.fontti_pieni.render("F2 = uusi peli", True, self.vuorossa[0])
        self.naytto.blit(teksti, (210, self.nayton_korkeus + 36))    

            
     

        pygame.display.flip()
        kello.tick(1000)   


    def peli_lapi(self):

        self.naytto.blit(lauta, (0,0))  
        for y in range(self.korkeus):
            for x in range(self.leveys):
                vari = self.kartta[y][x]
                if vari == SININEN or vari == PUNAINEN:
                    pygame.draw.circle(self.naytto, vari[0], (x*self.skaala + P_KOKO + REUNAN_KOKO, y*self.skaala + P_KOKO + REUNAN_KOKO), P_KOKO)  
     
        sinisia = 0
        punaisia = 0 

        for rivi in self.kartta:
            sinisia += rivi.count(SININEN)
            punaisia += rivi.count(PUNAINEN)

        voittoteksti = f"Voiton vei punainen: {punaisia} - {sinisia}"  
        if sinisia > punaisia:
            voittoteksti = f"Voiton vei sininen: {sinisia} - {punaisia} !"  
            

        teksti = self.fontti_iso.render(voittoteksti, True, self.vuorossa[0])
        self.naytto.blit(teksti, (30, self.nayton_korkeus + 20))

        pygame.display.flip()
        time.sleep(4)
        
        
       


if __name__ == "__main__":
    Othello()