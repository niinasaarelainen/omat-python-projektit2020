import pygame, copy, random
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
                 

def arvo_voittorivi(palloja):
    rivi = []    
    for i in range(palloja):
        monesko  = random.randint(0, len(varit) -1)
        rivi.append(varit[monesko])
    return rivi


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
        y += P_KOKO * 2 + VALI


def  mika_vari(y):
    # värivalikoima oikealla:
    y = (y - Y_ALOITUS + P_KOKO) // (P_KOKO * 2 + VALI) + 1
    if y >= 0 and y <= len(varit) -1:
        return y
    return None


def mika_paikka(x):   
    # "tyhjät" pallot:
    x = (x - X_ALOITUS + P_KOKO) // (P_KOKO * 2 + VALI) 
    if x >= 0 and x <= palloja -1:
        return x
    return None

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
    x_kohdennettu = -30
    y_kohdennettu = Y_ALOITUS + monesko_arvaus * (P_KOKO * 2 + VALI)
    vari = val
    
    while True:
        naytto.fill((val))
        varivalikoima()        
        for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    pygame.quit()                
                if tapahtuma.type == pygame.MOUSEBUTTONDOWN:    
                    x = tapahtuma.pos[0]
                    y = tapahtuma.pos[1]   
                    if x >= WIDTH - 60 - P_KOKO: 
                        if y != None:
                            vari = varit[mika_vari(y)]
                            print("vari", vari)
                    else:               
                        monesko_pallo = mika_paikka(x)  # voi olla None
                        print("monesko_pallo", monesko_pallo)
                        if monesko_pallo != None:
                            x_kohdennettu = X_ALOITUS + monesko_pallo * (P_KOKO * 2 + VALI)
                            print(x_kohdennettu)
                            
        pygame.draw.circle(naytto, (vari), (x_kohdennettu, y_kohdennettu), P_KOKO) 
        valitusteksti(teksti)
        #piirra_valinta(x_valinta, y_valinta)
        pelaaja_tilanne(monesko_arvaus)
        pygame.display.flip() 
        kello.tick(1000)   


pygame.init()
pygame.display.set_caption("MasterMind")
palloja = alkunaytto()
voittorivi = arvo_voittorivi(palloja)
print(voittorivi)
silmukka()