import pygame, math  

class Viisari:

    def __init__(self, viisarin_pituus, nopeus, alkuaika, paksuus, piirranko):
        self.viisarin_pituus = viisarin_pituus
        self.kulma = 2* math.pi / 60 * (alkuaika -15) # 0-kulma on varttia yli
        self.nopeus = nopeus
        self.paksuus = paksuus
        self.piirranko = piirranko
        self.historia = []

    def liikuta(self, x_alku, y_alku):
        self.kulma += self.nopeus
        self.x = x_alku + math.cos(self.kulma)*self.viisarin_pituus
        self.y = y_alku + math.sin(self.kulma)*self.viisarin_pituus
        if self.piirranko:
            self.draw_circle()

    def koordinaatit(self):
        return self.x, self.y

    def draw_circle(self):
        pos = (int(self.x), int(self.y))
        if pos not in self.historia:
            self.historia.append(pos)
        for p in self.historia:
            pygame.draw.circle(naytto, BLUE, p, 1)

# END class Viisari     

background_color = ( 60,  10,  10)
BLUE = (0, 0, 244)
pygame.init()
naytto = pygame.display.set_mode((700, 700))
keskus_x = 700 // 2
keskus_y = 700 // 2
naytto.fill(background_color)
kello = pygame.time.Clock()

viisarit = []
viisarit.append(Viisari(13, -2 * math.pi / 1000, 1, 1, False))# pit, nopeus, alkuaika, paksuus, piirranko
viisarit.append(Viisari(120, 2 * math.pi / 900, 1, 1, False))   
viisarit.append(Viisari(110, -2 * math.pi / 400, 1, 1, True))   # miinus =  vastapäivään
viisarit.append(Viisari(40, -2 * math.pi / 300, 1, 1, True)) 

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
    naytto.fill(background_color)  
    alku_x = keskus_x
    alku_y = keskus_y    

    for viisari in viisarit:
        viisari.liikuta(alku_x, alku_y)
        x, y = viisari.koordinaatit()
        pygame.draw.line(naytto, (0, 255, 0), (x, y), (alku_x, alku_y), viisari.paksuus)
        alku_x = x
        alku_y = y
    
    pygame.display.flip()     
    kello.tick(5000)