import pygame, random
from mixer import *


pygame.init()
LEVEYS =  1220
KORKEUS = 250
naytto = pygame.display.set_mode((LEVEYS, KORKEUS))
pygame.display.set_caption("Squid Game #1")

robo = pygame.image.load("robo.png")
robo_broken = pygame.image.load("robo_broken.png")
robo_broken = pygame.transform.scale(robo_broken, (150, 220))
robo_win = pygame.image.load("robo_win.png")
robo_win = pygame.transform.scale(robo_win, (210, 170))
robon_leveys = robo.get_width()
robon_korkeus = robo.get_height()



def main():
    global r, g
    x = 0
    time = 0
    sec = SEKUNTIMAARA
    textsurface = myfont.render(f"{sec}", True, (100, 30, 30))  
    vauhti = 0.5
    jarrutan = -1
    vauhdinpudotus = 0
    askeleita = 0
    musa_paused = False
    danger_time = DANGER_TIME
    mixer.music.play()
    liikkeella = False
    palkin_vari = (r, g, 10) 

    while True:
        naytto.fill(BLACK)
            
        if musa_paused and danger_time > 0:            
            danger_time -= 1
            pygame.draw.rect(naytto, palkin_vari, (LEVEYS // 2 - 30, 20, danger_time * 2, 30))
            r += 5
            g -= 5
            palkin_vari = (r, g, 10) 
        if danger_time == 0:
            danger_time = DANGER_TIME 
            musa_paused = False  
            pygame.time.delay(600)
            mixer.music.unpause()   
            r = 10
            g = 200   # värien RGB .muuttujia palkissa
            if jarrutan >= 0 or liikkeella:
                lopetus('H Ä V I S I T !!!', robo_broken)
                
        else:
            r = random.randint(0, 210)  # oli 210
            if r == 0:
                mixer.music.pause()    
                musa_paused = True 
                
        
        if jarrutan > 0  :
            if askeleita < 10:
                vauhti = 0.5
                jarrutan = -1
                askeleita = 0
                liikkeella = False
            else:
                jarrutan -= 1      
                if vauhti > 0.2:     
                    vauhti -= vauhdinpudotus / jarrutusmatka
        elif jarrutan == 0:
            vauhti = 0.5
            jarrutan = -1
            askeleita = 0
            liikkeella = False

        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()    
                mixer.music.stop()    

            elif tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_RIGHT:
                    vauhti += 0.2  
                    liikkeella = True

            elif tapahtuma.type == pygame.KEYUP:  
                jarrutan = int(vauhti * 10)   
                vauhdinpudotus = vauhti - 0.5       
                    
                
        keys=pygame.key.get_pressed()   # tämä ei saa olla for tapahtuma in pygame.event.get(): sisällä !!! 
        if keys[pygame.K_RIGHT]:
            if vauhti <= 5:
                vauhti += 0.05  
            askeleita += 1  
            
        if liikkeella and x < LEVEYS - robon_leveys - vauhti :    #  ei saa mennä reunojen yli !
            x += vauhti  

        if x >= LEVEYS - robon_leveys - vauhti:
            lopetus('V O I T I T !!!', robo_win)
                    
        
        naytto.blit(robo, (x, y))        
        time += 1
        if time % 60 == 0:
            sec -= 1    
            if sec == 0:
                lopetus('H Ä V I S I T !!!', robo_broken)
            textsurface = myfont.render(f"{sec}", True, (100, 30, 30)) 
        naytto.blit(textsurface, (320, 20))  
        pygame.display.flip()          
        kello.tick(60)


def lopetus(teksti, kuva):
    textsurface = myfont.render(teksti, True, (100, 30, 30))
    mixer.music.pause()  
    
    while True:
        naytto.fill((255, 255, 255))        
        naytto.blit(textsurface, (20, 100))    
        naytto.blit(kuva, (510, 10))

        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()    
                
            elif tapahtuma.type == pygame.KEYDOWN:
                main()

        pygame.display.flip()
        kello.tick(70)



y = KORKEUS - 100
jarrutusmatka = 35  # n. 20-60 sykliä, lasketaan KEYUP:ssa
DANGER_TIME = 40
BLACK = (0, 0, 0)
SEKUNTIMAARA = 30  # aikaa suorittaa peli

r = 10
g = 200   # värien RGB .muuttujia palkissa

kello = pygame.time.Clock()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 50)


main()
#lopetus('V O I T I T !!!', robo_win)
#lopetus('H Ä V I S I T !!!', robo_broken)