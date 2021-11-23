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

class Asteroidi:  # 11 x 3  rivistö
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.nopeus = 0.3
        self.gameover = False
        
    
    def liiku(self, liike):
        if liike == 0:
            self.y += 5
        else:
            self.x += liike
        if self.y + ast.get_height() >= HEIGHT:
            self.gameover = True
        return self.gameover


#######################################################################################

def luo_asteroidit():
    for rivissa in range(11):
        for riveja in range(3):
            asteroidit.append(Asteroidi(rivissa * 50 + 75, riveja * 50))


def game_over():
    fontti_iso = pygame.font.SysFont("Arial", 64)
    teksti = fontti_iso.render("Game Over", True, (205, 205, 205))
    naytto.blit(teksti, (140, 140))
    
    teksti = fontti.render(f"Score: {pisteet}", True, (205, 205, 205))
    naytto.blit(teksti, (260, 220))
    pygame.display.update()
    
    while True:
       for event in pygame.event.get():            
          if event.type == pygame.QUIT:
             pygame.quit()

               

pygame.init()
WIDTH = 650
HEIGHT = 450
naytto = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroidit")

robo = pygame.image.load("robo.png")
ast = pygame.image.load("ship.png").convert_alpha()   # ELI VIHOLLISALUS
asteroidien_liikerata = [-5, -5, -5, -5, -5, -5, -5, -5, 0, 5, 5, 5, 5, 5, 5, 5, 5, 0]   # -5 = vas  0= alas  5 = oik

kello = pygame.time.Clock()
pisteet = 0
fontti = pygame.font.SysFont("Arial", 24)
WHITE = (222, 222, 222)

r = Robotti()
asteroidit = []
pygame.mouse.set_pos([WIDTH+1, HEIGHT+1])  # hiiri pois ruudulta
luo_asteroidit()
kierros_nro = 0

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
        for ammus in r.ammutut:
            pygame.draw.circle(naytto, WHITE, (ammus),  3)        
            if ammus[1] == asteroidi.y + ast.get_height() and (ammus[0] >= asteroidi.x  and ammus[0] <= asteroidi.x + ast.get_width())  :
                pisteet += 1
        
        naytto.blit(ast, (asteroidi.x, asteroidi.y))
    
    if kierros_nro % 20 == 0:       
        asteroidien_liikerata.remove(liike)
        asteroidien_liikerata.append(liike)
        print(asteroidien_liikerata)

    for ammus in r.ammutut:
        ammus[1] -= 2
         
    
    pist = "Pisteet: " + str(pisteet)
    teksti = fontti.render(pist, True, (255, 0, 0))
    naytto.blit(teksti, (510, 40))

    pygame.display.flip()     
    kello.tick(70)

