import pygame, math  

class Viisari:

    def __init__(self, viisarin_pituus, nopeus, alkuaika, paksuus, piirranko):
        self.viisarin_pituus = viisarin_pituus
        self.kulma = 2* math.pi / 60 * (alkuaika -15) # 0-kulma on varttia yli
        self.nopeus = nopeus
        self.paksuus = paksuus
        self.piirranko = piirranko
        self.historia = []        
        self.toistuu = False

    def liikuta(self, x_alku, y_alku):
        self.kulma += self.nopeus
        self.x = x_alku + math.cos(self.kulma)*self.viisarin_pituus
        self.y = y_alku + math.sin(self.kulma)*self.viisarin_pituus
        if self.piirranko:
            self.draw_circle()

    def koordinaatit(self):
        return self.x, self.y

    def draw_circle(self):
        self.toistuu = False
        pos = (int(self.x), int(self.y))
        if self.historia == []:
            self.ekapiste = pos 
        if pos not in self.historia:
            self.historia.append(pos)
            pygame.draw.circle(naytto, BLUE, pos, 1)
        elif pos == self.ekapiste:
            self.toistuu = True


# END class Viisari     

background_color = ( 60,  10,  10)
BLUE = (0, 0, 244)
YELLOW = (199, 199, 0)
pygame.init()
naytto = pygame.display.set_mode((810, 810))
keskus_x = 810 // 2
keskus_y = 810 // 2
kello = pygame.time.Clock()

favourites = []   # sis. valikoidut viisarit
viisarit = []
viisarit.append(Viisari(13, -2 * math.pi / 200, 1, 1, False))# pit, nopeus, alkuaika, paksuus, piirranko
viisarit.append(Viisari(120, 2 * math.pi / 90, 1, 1, False))   
viisarit.append(Viisari(110, -2 * math.pi / 400, 1, 1, True))   # miinus =  vastapäivään
viisarit.append(Viisari(40, -2 * math.pi / 300, 1, 1, True)) 

def piirra_vaiheittain():
    naytto.fill(background_color)
    lopetetaan = False  # pitää saada 2 ääntä (True-viisarien määrä)    EI TOIMI !! koska duplikaattipisteitä useita
    while lopetetaan == False:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()
        alku_x = keskus_x
        alku_y = keskus_y    

        for viisari in viisarit:
            viisari.liikuta(alku_x, alku_y)
            x, y = viisari.koordinaatit()
            alku_x = x
            alku_y = y
            if viisari.toistuu:
                lopetetaan = True
        
        pygame.display.flip()     
        kello.tick(9000)

def piirra_kerralla():
    kaksi_sekuntia = 0
    naytto.fill(background_color)
    while kaksi_sekuntia < 2:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()        
        for viisari in viisarit:
            for pos in viisari.historia:
                pygame.draw.circle(naytto, YELLOW, pos, 1)
            
        pygame.display.flip()    
        kello.tick(1) 
        kaksi_sekuntia += 1
    
piirra_vaiheittain()
favourites.append(viisarit)
piirra_kerralla()
viisarit = []   # TODO random 20...99
viisarit.append(Viisari(23, -2 * math.pi / 200, 1, 1, False))# pit, nopeus, alkuaika, paksuus, piirranko
viisarit.append(Viisari(40, 2 * math.pi / 90, 1, 1, False))   
viisarit.append(Viisari(80, -2 * math.pi / 400, 1, 1, True))   # miinus =  vastapäivään
viisarit.append(Viisari(70, -2 * math.pi / 300, 1, 1, True)) 
piirra_vaiheittain()
favourites.append(viisarit)
piirra_kerralla()

viisarit = []
viisarit.append(Viisari(99, -2 * math.pi / 200, 1, 1, False))# pit, nopeus, alkuaika, paksuus, piirranko
viisarit.append(Viisari(99, 2 * math.pi / 90, 1, 1, False))   
viisarit.append(Viisari(99, -2 * math.pi / 400, 1, 1, True))   # miinus =  vastapäivään
viisarit.append(Viisari(99, -2 * math.pi / 300, 1, 1, True)) 
piirra_vaiheittain()
favourites.append(viisarit)
piirra_kerralla()
