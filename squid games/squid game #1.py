# TEE RATKAISUSI TÄHÄN:
import pygame, random
  

pygame.init()
LEVEYS =  1200
KORKEUS = 200
naytto = pygame.display.set_mode((LEVEYS, KORKEUS))
pygame.display.set_caption("Squid Game #1")

robo = pygame.image.load("robo.png")
robon_leveys = robo.get_width()
robon_korkeus = robo.get_height()
x = 0
y = KORKEUS - 100

oikealle = False
vasemmalle = False
vauhti = 0.8

kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()

        elif tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = True
                vauhti += 0.2
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = True

        elif tapahtuma.type == pygame.KEYUP:           
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = False
                vauhti += 0.2
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = False
    
        
    if oikealle and x <= LEVEYS - robon_leveys - vauhti :    #  ei saa mennä reunojen yli !
            x += vauhti   
    if vasemmalle and x >= 0 + vauhti:
            x -= vauhti
                
    naytto.fill((0, 0, 0))
    naytto.blit(robo, (x, y))
    pygame.display.flip()
    kello.tick(90)