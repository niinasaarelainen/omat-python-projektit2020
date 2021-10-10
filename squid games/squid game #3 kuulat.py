import pygame, random, time
from mixer import *


pygame.init()
LEVEYS =  440
KORKEUS = 360
naytto = pygame.display.set_mode((LEVEYS, KORKEUS))
pygame.display.set_caption("Squid Game #1")
kello = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 22)
font_iso = pygame.font.SysFont('Comic Sans MS', 30)

sin = pygame.image.load("marble_blue.png")
vih = pygame.image.load("marble_green.png")
sin = pygame.transform.scale(sin, (32, 32))
vih = pygame.transform.scale(vih, (32, 32))

BLUE = (0, 0, 232)
GREEN = (0, 232, 0)


def kuvat_naytolle(sinisia, vihreita):
    if sinisia > 10:
        sinisia = 10
    if vihreita > 10:
        vihreita = 10
    if sinisia < 0:
        sinisia = 0
    if vihreita < 0:
        vihreita = 0
    x = 25
    # pelaaja 1
    for i in range(sinisia):
        naytto.blit(sin, (x, 50))
        x += 38
    x = 25
    for i in range(10 - vihreita):
        naytto.blit(vih, (x, 90))
        x += 38

    # pelaaja 2  = tietokone
    x = 25
    for i in range(vihreita):
        naytto.blit(vih, (x, 220))
        x += 38
    x = 25
    for i in range(10 - sinisia):
        naytto.blit(sin, (x, 260))
        x += 38

    return sinisia, vihreita


def main():

    vuoro = 0
    sinisia = 10   # omistajan määrät
    vihreita = 10
    tietokone_parillinenko = "pariton"
    pelaaja_parillinenko = "pariton"

    while True:
        naytto.fill((252, 252, 252)) 
        sinisia, vihreita = kuvat_naytolle(sinisia, vihreita)

        if vuoro % 6 == 0:
            kys = font.render("Montako kuulaa valitset?", True, BLUE)     
            naytto.blit(kys, (35, 130))  

        elif vuoro % 6 == 1:
            r = random.randint(0, 1)
            if r == 0:
                tietokone_parillinenko = "pariton"
            else:
                tietokone_parillinenko = "parillinen"
            r = random.randint(1, 4)  
            # tietokone arvasi oikein:          
            if pelaaja_parillinenko == tietokone_parillinenko:
               sinisia -= r   
               if sinisia <= 0:
                   vihreita -= sinisia   
                   if vihreita >= 10:
                       lopetus("Lose !!  Any key = New Game")
            # tietokone arvasi väärin:      
            else:
                vihreita -= r
                if vihreita <= 0:
                   sinisia -= vihreita
                   if sinisia >= 10:
                       lopetus("Win !!   Any key = New Game")                 
            vuoro += 1

        elif vuoro % 6 == 2:
            naytto.fill((252, 252, 252)) 
            kys = font.render(f"Tietokone valitsi {tietokone_parillinenko}, panos: {r}", True, GREEN)     
            naytto.blit(kys, (25, 300)) 
            sinisia, vihreita = kuvat_naytolle(sinisia, vihreita)
            pygame.display.flip()     
            time.sleep(2) 
            vuoro += 1

        elif vuoro % 6 == 3:
            kys = font.render("Parillinen(2) vai pariton(1)?", True, BLUE)     
            naytto.blit(kys, (25, 130))  
            r = random.randint(0, 1)
            if r == 0:
                tietokone_parillinenko = "pariton"
            else:
                tietokone_parillinenko = "parillinen"

        elif vuoro % 6 == 4:
            kys = font.render("Paljonko panostat? (1-4)", True, BLUE)     
            naytto.blit(kys, (25, 130)) 

        elif vuoro % 6 == 5:            
            naytto.fill((252, 252, 252)) 
            kys = font.render(f"Tietokoneen valinta oli {tietokone_parillinenko}", True, GREEN)     
            naytto.blit(kys, (25, 300)) 
            # tietokone arvasi oikein:          
            if pelaaja_parillinenko == tietokone_parillinenko:
               vihreita -= lkm
               if vihreita <= 0:
                   sinisia -= vihreita                   
                   print("tietokone arvasi oikein...lkm:", lkm, "  vihreita:", vihreita, "  sinisia:", sinisia)
                   if sinisia >= 10:
                       lopetus("Win !!   Any key = New Game")
            # tietokone arvasi väärin:          
            else:
               sinisia -= lkm   
               if sinisia <= 0: 
                   vihreita -= sinisia
                   print("lkm:", lkm, "  vihreita:", vihreita, "  sinisia:", sinisia)
                   if vihreita >= 10:
                       lopetus("Lose !!  Any key = New Game")
            sinisia, vihreita = kuvat_naytolle(sinisia, vihreita)
            pygame.display.flip()       
            time.sleep(2) 
            vuoro += 1


        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()    

            elif tapahtuma.type == pygame.KEYDOWN:  
                lkm = tapahtuma.key - 48
                if lkm % 2 == 0 and (vuoro % 6 == 3 or vuoro % 6 == 0):
                    pelaaja_parillinenko = "parillinen"
                    print(pelaaja_parillinenko)
                elif vuoro % 6 == 3 or vuoro % 6 == 0:
                    pelaaja_parillinenko = "pariton"
                    print(pelaaja_parillinenko)
                vuoro += 1


        pygame.display.flip()          
        kello.tick(60)


def lopetus(teksti):
    textsurface = font_iso.render(teksti, True, (100, 30, 30))
    
    while True:
        naytto.fill((255, 255, 255))        
        naytto.blit(textsurface, (20, 100)) 

        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()    
                
            elif tapahtuma.type == pygame.KEYDOWN:
                main()

        pygame.display.flip()
        kello.tick(70)



main()