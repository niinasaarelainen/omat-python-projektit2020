import pygame, random, time
from mixer import *


pygame.init()
LEVEYS =  400
KORKEUS = 360
naytto = pygame.display.set_mode((LEVEYS, KORKEUS))
pygame.display.set_caption("Squid Game #1")
kello = pygame.time.Clock()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 22)

sin = pygame.image.load("marble_blue.png")
vih = pygame.image.load("marble_green.png")
sin = pygame.transform.scale(sin, (30, 30))
vih = pygame.transform.scale(vih, (30, 30))

BLUE = (0, 0, 232)
GREEN = (0, 232, 0)


def kuvat_naytolle(sinisia, vihreita):
    x = 20
    # pelaaja 1
    for i in range(sinisia):
        naytto.blit(sin, (x, 50))
        x += 36
    x = 20
    for i in range(10 - vihreita):
        naytto.blit(vih, (x, 90))
        x += 36

    # pelaaja 2  = tietokone
    x = 20
    for i in range(vihreita):
        naytto.blit(vih, (x, 220))
        x += 36
    x = 20
    for i in range(10 - sinisia):
        naytto.blit(sin, (x, 260))
        x += 36


def main():

    vuoro = 0
    sinisia = 10   # omistajan määrät
    vihreita = 10
    tietokone_parillinenko = "pariton"
    pelaaja_parillinenko = "pariton"

    while True:
        naytto.fill((252, 252, 252)) 
        kuvat_naytolle(sinisia, vihreita)

        if vuoro % 6 == 0:
            kys = myfont.render("Montako kuulaa valitset?", True, BLUE)     
            naytto.blit(kys, (20, 130))  

        elif vuoro % 6 == 1:
            r = random.randint(0, 1)
            if r == 0:
                tietokone_parillinenko = "pariton"
            else:
                tietokone_parillinenko = "parillinen"
            r = random.randint(1, 4)            
            if pelaaja_parillinenko == tietokone_parillinenko:
               sinisia -= r   # TODO  vähennetään hankittuja vihreitä jos on . Jos ei kuolema 
            vuoro += 1

        elif vuoro % 6 == 2:
            naytto.fill((252, 252, 252)) 
            kys = myfont.render(f"Tietokone valitsi {tietokone_parillinenko}, panos: {r}", True, GREEN)     
            naytto.blit(kys, (20, 300)) 
            kuvat_naytolle(sinisia, vihreita)
            pygame.display.flip()     
            time.sleep(2) 
            vuoro += 1

        elif vuoro % 6 == 3:
            kys = myfont.render("Parillinen(2) vai pariton(1)?", True, BLUE)     
            naytto.blit(kys, (20, 130))  
            r = random.randint(0, 1)
            if r == 0:
                tietokone_parillinenko = "pariton"
            else:
                tietokone_parillinenko = "parillinen"

        elif vuoro % 6 == 4:
            kys = myfont.render("Paljonko panostat? (1-4)", True, BLUE)     
            naytto.blit(kys, (20, 130)) 

        elif vuoro % 6 == 5:            
            naytto.fill((252, 252, 252)) 
            kys = myfont.render(f"Tietokoneen valinta oli {tietokone_parillinenko}", True, BLUE)     
            naytto.blit(kys, (20, 130)) 
            if pelaaja_parillinenko == tietokone_parillinenko:
               vihreita -= lkm
            kuvat_naytolle(sinisia, vihreita)
            pygame.display.flip()       
            time.sleep(2) 
            vuoro += 1


        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()    

            elif tapahtuma.type == pygame.KEYDOWN:  
                lkm = tapahtuma.key - 48
                print(lkm)
                if lkm % 2 == 0:
                    pelaaja_parillinenko = "parillinen"
                else:
                    pelaaja_parillinenko = "pariton"
                vuoro += 1


        pygame.display.flip()          
        kello.tick(60)





main()