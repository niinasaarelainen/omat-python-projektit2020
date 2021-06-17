import pygame, copy
from vakiot import *
from gameover import *


def alkunaytto():
    fontti = pygame.font.SysFont("Arial", 26)
    naytto.fill((val))
    y = 140
    for rivi in alkuohjeet():
        teksti = fontti.render(rivi, True, vih)
        naytto.blit(teksti, (150, y))
        y += 40
    pygame.display.flip()

    while True:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                 pygame.quit()
            elif tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_4:
                    return 4
                if tapahtuma.key == pygame.K_5:
                    return 5
                if tapahtuma.key == pygame.K_6:
                    return 6
                 

def valitusteksti(text):
    rivit = text.split(".")
    fontti = pygame.font.SysFont("Arial", 18)
    y = HEIGHT - 100
    for rivi in rivit:
        teksti = fontti.render(rivi, True, (200, 0, 0))
        naytto.blit(teksti, (10, y))
        y += 30


def pelaaja_tilanne(y):   
    x = X_ALOITUS
    y = Y_ALOITUS + y     
    for i in range (palloja):      
        pygame.draw.circle(naytto, mus, (x, y), P_KOKO, 2)  
        x += P_KOKO * 2 + VALI


def piirra_valinta(x_valinta, y_valinta):
    pygame.draw.circle(naytto, (0, 0, 100), (x_valinta, y_valinta), P_KOKO) 

def varivalikoima():
    x = WIDTH - 60
    y = 50
    for vari in varit:
        pygame.draw.circle(naytto, (vari), (x, y), P_KOKO) 
        y += P_KOKO * 2 + 4


def mika_paikka(x, y):
    x = x - X_ALOITUS // (P_KOKO + VALI)
    return x

def onko_voitto(mita_Verrataan, mihin_verrataan, kuulia):   
    sijainnit = []
    for x, y in mita_Verrataan:
        for  i in range(kuulia):
            if x > mihin_verrataan[i][0] - P_KOKO+2 and x < mihin_verrataan[i][0] + P_KOKO+2 and y > mihin_verrataan[i][1] - P_KOKO+2 and y < mihin_verrataan[i][1] + P_KOKO+2:
                sijainnit.append(i)
    print(sijainnit)
    if len(set(sijainnit)) == kuulia:
        return True
    return False



def silmukka():
    monesko_arvaus = 0
    teksti = ""
    x = -30
    y = -30
    
    while True:
        naytto.fill((val))
        varivalikoima()        
        for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    pygame.quit()                
                if tapahtuma.type == pygame.MOUSEBUTTONDOWN:    
                    x = tapahtuma.pos[0]
                    y = tapahtuma.pos[1]                  
                    monesko_pallo = mika_paikka(x, y)

        valitusteksti(teksti)
        #piirra_valinta(x_valinta, y_valinta)
        pelaaja_tilanne(monesko_arvaus)
        pygame.display.flip() 
        kello.tick(1000)   


pygame.init()
pygame.display.set_caption("MasterMind")
palloja = alkunaytto()
silmukka()