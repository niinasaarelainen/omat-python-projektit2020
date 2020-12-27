import pygame, copy

class Sokoban:
    def __init__(self):
        pygame.init()
        
        self.lataa_kuvat()
        self.uusi_peli()
        
        self.korkeus = len(self.kartta)
        self.leveys = len(self.kartta[0])
        self.skaala = self.kuvat[0].get_width()

        nayton_korkeus = self.skaala * self.korkeus
        nayton_leveys = self.skaala * self.leveys
        self.naytto = pygame.display.set_mode((nayton_leveys, nayton_korkeus + self.skaala))

        self.fontti_iso = pygame.font.SysFont("Arial", 25)
        self.fontti_pieni = pygame.font.SysFont("Arial", 22)

        pygame.display.set_caption("Sokoban")

        self.silmukka()

    def lataa_kuvat(self):
        self.kuvat = []        
        self.objektit = {}
        i = 0
        for nimi in ["lattia", "seina", "kohde", "laatikko", "robo", "valmis", "kohderobo"]:
            self.kuvat.append(pygame.image.load(nimi + ".png"))
            self.objektit[nimi] = i 
            i += 1


    def uusi_peli(self):
        self.kartta = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                       [1, 2, 3, 0, 0, 0, 1, 0, 0, 1, 2, 3, 0, 0, 0, 0, 1],
                       [1, 0, 0, 1, 2, 3, 0, 2, 3, 0, 0, 0, 1, 0, 0, 0, 1],
                       [1, 0, 4, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

       
        self.siirrot = 0        
        self.liikkeet_muistiin = []

    def silmukka(self):
        while True:
            self.tutki_tapahtumat()
            self.piirra_naytto()

   

    """
    def edellinen_tilanne(self):
        print("alku", self.kartta)        
        #print(len(self.kartta_muistiin))
        self.kartta_muistiin = copy.deepcopy(self.kartta_muistiin[:-1])
        self.kartta = copy.deepcopy(self.kartta_muistiin[-1])
        #self.kartta = [rivi.copy() for rivi in self.kartta_muistiin[-1]]
        #self.kartta = copy.deepcopy(self.kartta_muistiin[-1])
        print("testi", self.kartta)        
        #print(len(self.kartta_muistiin))
        self.siirrot -= 1 
        self.piirra_naytto()
    """

    def tutki_tapahtumat(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_LEFT:
                    self.liiku(0, -1,"robotti")
                if tapahtuma.key == pygame.K_RIGHT:
                    self.liiku(0, 1, "robotti")
                if tapahtuma.key == pygame.K_UP:
                    self.liiku(-1, 0, "robotti")
                if tapahtuma.key == pygame.K_DOWN:
                    self.liiku(1, 0, "robotti")

                if tapahtuma.key == pygame.K_F2:
                    self.uusi_peli()
                if tapahtuma.key == pygame.K_BACKSPACE:
                    if not self.liikkeet_muistiin == []:
                        self.edellinen_tilanne()
                if tapahtuma.key == pygame.K_ESCAPE:
                    exit()

            if tapahtuma.type == pygame.QUIT:
                exit()

    def edellinen_tilanne(self):                ## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        vika = self.liikkeet_muistiin.pop(-1)   
        if len(vika) == 3:
            mika_liikkuu, y, x = vika
            print(mika_liikkuu, y, x)      
            self.liiku(-y, -x, mika_liikkuu, False)
        else:
            mika_liikkuu, y, x, vanha_y, vanha_x = vika
            print(mika_liikkuu, y, x, vanha_y, vanha_x)      
            self.liiku(y, x, mika_liikkuu, False, vanha_y, vanha_x)



    def liiku(self, dy, dx, mika_liikkuu, liike_muistiin = True, vanha_y = None, vanha_x = None):
        if self.peli_lapi():
            return

        if mika_liikkuu == "laatikko" and liike_muistiin == False:
            print("  laatikko", dy, dx)
            self.kartta[dy][dx] = 3
            self.kartta[vanha_y][vanha_x] = 0  
            return

        robo_y, robo_x = self.etsi_robo()
        uusi_y = robo_y + dy
        uusi_x = robo_x + dx
        

        if self.kartta[uusi_y][uusi_x] == self.objektit["seina"]:
            return

        if self.kartta[uusi_y][uusi_x] in [self.objektit["laatikko"], self.objektit["valmis"]]:
            laatikon_uusi_paikka_y = uusi_y + dy
            laatikon_uusi_paikka_x = uusi_x + dx

            if self.kartta[laatikon_uusi_paikka_y][laatikon_uusi_paikka_x] in [self.objektit["seina"], self.objektit["laatikko"],  self.objektit["valmis"]]:
                return

            if liike_muistiin:    # TODO vierekkäinen laatikko katoaa palautuksessa
                self.liikkeet_muistiin.append(("laatikko", uusi_y, uusi_x, laatikon_uusi_paikka_y, laatikon_uusi_paikka_x))


            # muuttaa tavallisen laatikon lattiaksi ja kohderuudussa olevan laatikon kohderuuduksi
            self.kartta[uusi_y][uusi_x] -= 3
            self.kartta[laatikon_uusi_paikka_y][laatikon_uusi_paikka_x] += 3

        if mika_liikkuu == "robotti":
            self.kartta[robo_y][robo_x] -= 4
            self.kartta[uusi_y][uusi_x] += 4            
        
        if liike_muistiin:
            self.liikkeet_muistiin.append((mika_liikkuu, dy, dx))
            self.siirrot += 1

        if not liike_muistiin and mika_liikkuu == "robotti":
            self.siirrot -= 1

    def etsi_robo(self):
        for y in range(self.korkeus):
            for x in range(self.leveys):
                if self.kartta[y][x] in [self.objektit["robo"], self.objektit["kohderobo"]]:
                    return (y, x)



    def piirra_naytto(self):
        self.naytto.fill((0, 0, 0))

        for y in range(self.korkeus):
            for x in range(self.leveys):
                ruutu = self.kartta[y][x]
                self.naytto.blit(self.kuvat[ruutu], (x * self.skaala, y * self.skaala))

        teksti = self.fontti_iso.render("Siirrot: " + str(self.siirrot), True, (255, 0, 0))
        self.naytto.blit(teksti, (25, self.korkeus * self.skaala + 10))

        teksti = self.fontti_pieni.render("F2 = uusi peli", True, (255, 0, 0))
        self.naytto.blit(teksti, (190, self.korkeus * self.skaala + 10))

        teksti = self.fontti_pieni.render("Esc = sulje peli", True, (255, 0, 0))
        self.naytto.blit(teksti, (360, self.korkeus * self.skaala + 10))

        teksti = self.fontti_pieni.render("Backspace = siirto taaksepäin", True, (255, 0, 0))
        self.naytto.blit(teksti, (555, self.korkeus * self.skaala + 10))

        if self.peli_lapi():
            teksti = self.fontti_iso.render("Onnittelut, läpäisit pelin!", True, (255, 0, 0))
            teksti_x = self.skaala * self.leveys / 2 - teksti.get_width() / 2
            teksti_y = self.skaala * self.korkeus / 2 - teksti.get_height() / 2
            pygame.draw.rect(self.naytto, (0, 0, 0), (teksti_x, teksti_y, teksti.get_width(), teksti.get_height()))
            self.naytto.blit(teksti, (teksti_x, teksti_y))

        pygame.display.flip()

    def peli_lapi(self):
        for y in range(self.korkeus):
            for x in range(self.leveys):
                if self.kartta[y][x] in [self.objektit["kohde"], self.objektit["kohderobo"]]:
                    return False
        return True

if __name__ == "__main__":
    Sokoban()
