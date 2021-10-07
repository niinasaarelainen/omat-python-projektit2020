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
jarrutan = -1
vauhdinpudotus = 0

kello = pygame.time.Clock()

while True:

    
    if jarrutan > 0 :
        jarrutan -= 1
        print(vauhti)
        print(vauhdinpudotus)
    if jarrutan == 20 :
        vauhdinpudotus = vauhti - 0.8
        vauhti -= vauhdinpudotus / 20
        print("10")
    elif jarrutan > 0 :
        vauhti -= vauhdinpudotus / 20
    elif jarrutan == 0:
        vauhti = 0.8
        jarrutan = -1
        oikealle = False 


    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()        

        elif tapahtuma.type == pygame.KEYDOWN:
            stopped = False
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = True
                vauhti += 0.2 

        elif tapahtuma.type == pygame.KEYUP:  
            jarrutan = 21   # 5 sykliä jarrutusta  
                
            
    keys=pygame.key.get_pressed()   # tämä ei saa olla for tapahtuma in pygame.event.get(): sisällä !!! 
    if keys[pygame.K_RIGHT]:
        vauhti += 0.06  
        
        
        
    if oikealle and x <= LEVEYS - robon_leveys - vauhti :    #  ei saa mennä reunojen yli !
        x += vauhti  
                
    naytto.fill((0, 0, 0))
    naytto.blit(robo, (x, y))
    pygame.display.flip()
    kello.tick(90)