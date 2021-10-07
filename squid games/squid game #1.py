# TEE RATKAISUSI TÄHÄN:
import pygame, random
from mixer import *


pygame.init()
LEVEYS =  1200
KORKEUS = 200
naytto = pygame.display.set_mode((LEVEYS, KORKEUS))
pygame.display.set_caption("Squid Game #1")

robo = pygame.image.load("robo.png")
robon_leveys = robo.get_width()
robon_korkeus = robo.get_height()



def main():
    global musa_paused, jarrutan, oikealle, x, vauhti, askeleita, danger_time, vauhdinpudotus
    while True:

        naytto.fill((0, 0, 0))
            
        if musa_paused and danger_time > 0:
            danger_time -= 1
            pygame.draw.rect(naytto, RED, (LEVEYS // 2 - 30, 20, danger_time * 2, 30))
            if danger_time == 0:
                if jarrutan == -1:
                    lopetus()
                print("0")
                mixer.music.unpause()   
                musa_paused = False  
                danger_time = DANGER_TIME 
        else:
            r = random.randint(0, 210)
            if r == 0:
                mixer.music.pause()    
                musa_paused = True 

        
        if jarrutan > 0 :
            if askeleita < 10:
                print(askeleita)
                vauhti = 0.8
                jarrutan = -1
                oikealle = False 
                askeleita = 0
            jarrutan -= 1
        if jarrutan == jarrutusmatka - 1  :
            vauhdinpudotus = vauhti - 0.8
            vauhti -= vauhdinpudotus / jarrutusmatka
        elif jarrutan > 0 :
            vauhti -= vauhdinpudotus / jarrutusmatka
        elif jarrutan == 0:
            vauhti = 0.8
            jarrutan = -1
            askeleita = 0
            oikealle = False 


        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()    
                mixer.music.stop()    

            elif tapahtuma.type == pygame.KEYDOWN:
                stopped = False
                if tapahtuma.key == pygame.K_RIGHT:
                    oikealle = True
                    vauhti += 0.2  

            elif tapahtuma.type == pygame.KEYUP:  
                jarrutan = int(vauhti * 10)
                print(jarrutan)
                
                    
                
        keys=pygame.key.get_pressed()   # tämä ei saa olla for tapahtuma in pygame.event.get(): sisällä !!! 
        if keys[pygame.K_RIGHT]:
            vauhti += 0.06  
            askeleita += 1  
            
        if oikealle and x <= LEVEYS - robon_leveys - vauhti :    #  ei saa mennä reunojen yli !
            x += vauhti  
                    
        
        naytto.blit(robo, (x, y))
        kello.tick(60)


def lopetus():
    print("lopetus")
    while True:
        naytto.fill((0, 0, 0))
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 50)
        textsurface = myfont.render('HÄVISIT !!!', False, (0, 0, 0))
        naytto.blit(textsurface, (20, 100))
        
        pygame.display.flip()

        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()    
                mixer.music.stop()    

            elif tapahtuma.type == pygame.KEYDOWN:
                main()



x = 0
y = KORKEUS - 100

oikealle = False
vasemmalle = False
vauhti = 0.8
jarrutan = -2
vauhdinpudotus = 0
askeleita = 0
musa_paused = False

jarrutusmatka = 30  # n. 20-60 sykliä, lasketaan KEYUP:ssa
DANGER_TIME = 50
danger_time = DANGER_TIME
RED = (200, 0, 0)

kello = pygame.time.Clock()

main()