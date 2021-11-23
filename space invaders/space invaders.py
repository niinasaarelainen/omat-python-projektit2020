import pygame, random

class Robotti:   # ohjataan nuolinäppäimillä

    def __init__(self):
        self.x = int(WIDTH/2)
        self.y = HEIGHT-robo.get_height()
        self.nopeus = 1
        self.oikealle = False           
        self.vasemmalle = False
        self.robon_oik_reuna = robo.get_width() - 1
        self.ammutut = []
   
    def key_events(self, tapahtuma):
        if tapahtuma.type == pygame.KEYDOWN:     
            if tapahtuma.key == pygame.K_RIGHT:
                self.oikealle = True
            if tapahtuma.key ==  pygame.K_LEFT:
                self.vasemmalle = True
            if tapahtuma.key ==  pygame.K_SPACE:
                self.ammutut.append([self.x + 15, HEIGHT - 28])  #('tuple' object does not support item assignment)
        if tapahtuma.type == pygame.KEYUP:
            if tapahtuma.key ==  pygame.K_RIGHT:
                self.oikealle = False
            if tapahtuma.key ==  pygame.K_LEFT:
                self.vasemmalle = False
                
    def liiku(self):
        if self.oikealle and self.x <= WIDTH - self.robon_oik_reuna - self.nopeus:
            self.x += self.nopeus   
        if self.vasemmalle and self.x >= self.nopeus:
            self.x -= self.nopeus


#######################################################################################     

class Asteroidi:  # 11 x 4  rivistö
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.nopeus = 0.3        
    
    def liiku(self, liike):
        if liike == 0:
            self.y += 8
        else:
            self.x += liike

    

#######################################################################################

def luo_asteroidit():
    global asteroidit
    for rivissa in range(11):
        for riveja in range(4):
            asteroidit.append(Asteroidi(rivissa * 50 + 85, riveja * 50))


def game_over(status, pisteet):
    fontti_iso = pygame.font.SysFont("Arial", 64)
    teksti = fontti_iso.render(status, True, (205, 205, 205))
    naytto.blit(teksti, (140, 140))
    
    teksti = fontti.render(f"Score: {pisteet}", True, (205, 205, 205))
    naytto.blit(teksti, (255, 220))

    teksti = fontti.render(f"New Game: Arrows", True, (205, 205, 205))
    naytto.blit(teksti, (205, 270))
    pygame.display.update()
    
    while True:
       for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:     
                if event.key in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN]:
                    pelaa()

               

pygame.init()
WIDTH = 650
HEIGHT = 450
naytto = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroidit")

robo = pygame.image.load("robo.png")
ast = pygame.image.load("ship.png").convert_alpha()   # ELI VIHOLLISALUS
asteroidien_liikerata = [-5, -5, -5, -5, -5, -5, -5, -5, -5,  0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0]   # -5 = vas  0= alas  5 = oik

kello = pygame.time.Clock()

fontti = pygame.font.SysFont("Arial", 24)
WHITE = (222, 222, 222)
GREEN = (10, 255, 10)

r = Robotti()
asteroidit = []
pygame.mouse.set_pos([WIDTH+1, HEIGHT+1])  # hiiri pois ruudulta


def pelaa():
    global asteroidit
    asteroidit = []
    luo_asteroidit()
    kierros_nro = 0
    asteroidien_ammukset = []
    pisteet = 0
    r.ammutut = []
    while True:
        kierros_nro += 1
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()
            r.key_events(tapahtuma)

        naytto.fill((0, 0, 0))          
        r.liiku()      
        naytto.blit(robo, (r.x, r.y))
        
        liike = asteroidien_liikerata[0]
        for asteroidi in asteroidit:            
            if kierros_nro % 20 == 0:                
                asteroidi.liiku(liike)
                rand = random.randint(0, 80)
                if  rand == 0:
                    asteroidien_ammukset.append([asteroidi.x, asteroidi.y])
            
            # robotin ampumat
            for ammus in r.ammutut:
                pygame.draw.circle(naytto, WHITE, (ammus),  3)        
                if ammus[1] <= asteroidi.y + ast.get_height() and ammus[1] >= asteroidi.y + ast.get_height()- 4 and ammus[0] >= asteroidi.x  and ammus[0] <= asteroidi.x + ast.get_width():
                    pisteet += 1
                    asteroidit.remove(asteroidi)
                    if len(asteroidit) == 0:
                        game_over("Winner !!!", pisteet)
                    r.ammutut.remove(ammus)
            
            naytto.blit(ast, (asteroidi.x, asteroidi.y))
        
        if kierros_nro % 20 == 0:       
            asteroidien_liikerata.remove(liike)
            asteroidien_liikerata.append(liike)

        for ammus in r.ammutut:
            ammus[1] -= 2

        # hyökkääjien ampumat
        for ammus in asteroidien_ammukset:
            pygame.draw.circle(naytto, GREEN, (ammus),  3)  
            if ammus[1] <= r.y + 5 and ammus[1] >= r.y + 2 and ammus[0] >= r.x  and ammus[0] <= r.x + robo.get_width():
                game_over("Game Over", pisteet)
            ammus[1] += 2      
            
        
        pist = "Pisteet: " + str(pisteet)
        teksti = fontti.render(pist, True, (255, 0, 0))
        naytto.blit(teksti, (510, 40))

        pygame.display.flip()     
        kello.tick(70)


pelaa()