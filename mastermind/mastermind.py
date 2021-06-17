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


def piirra_lukitut_pallot(nykyinen_arvaus, y_kohdennettu) :    
    y = Y_ALOITUS
    for arvaus in arvaukset:
        for i in range(len(arvaus)):
            x_kohdennettu = X_ALOITUS + i * (P_KOKO * 2 + VALI)
            pygame.draw.circle(naytto, (arvaus[i]), (x_kohdennettu, y), P_KOKO) 
        y += P_KOKO * 2 + VALI

    for i in range(len(nykyinen_arvaus)):
        x_kohdennettu = X_ALOITUS + i * (P_KOKO * 2 + VALI)
        pygame.draw.circle(naytto, (nykyinen_arvaus[i]), (x_kohdennettu, y_kohdennettu), P_KOKO) 

def rivi_ok():
    global nykyinen_arvaus, monesko_arvaus, arvaukset
    oikealla_paikalla = 0
    oikea_vari_vaaralla_paikalla = 0
    voittorivi_temp = copy.deepcopy(voittorivi)
    arvaukset.append(nykyinen_arvaus)
    for i in range(len(nykyinen_arvaus)):
        if nykyinen_arvaus[i] == voittorivi_temp[i]:
            oikealla_paikalla += 1
            voittorivi_temp[i] = val
        elif nykyinen_arvaus[i] in voittorivi_temp:
            oikea_vari_vaaralla_paikalla += 1
            ind = voittorivi_temp.index(nykyinen_arvaus[i])
            voittorivi_temp[ind] = val
    nykyinen_arvaus = {0:val, 1:val, 2:val, 3:val}
    monesko_arvaus += 1
    print(oikealla_paikalla, oikea_vari_vaaralla_paikalla)



def silmukka():    
    teksti = ""
    x_kohdennettu = -30
    y_kohdennettu = Y_ALOITUS + monesko_arvaus * (P_KOKO * 2 + VALI)   
    vari = val    
    
    while True:
        naytto.fill((val))
        naytto.blit(ok,  (400,40))
        y_kohdennettu = Y_ALOITUS + (monesko_arvaus * (P_KOKO * 2 + VALI)) 
        varivalikoima()        
        for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    pygame.quit()                
                if tapahtuma.type == pygame.MOUSEBUTTONDOWN:    
                    x = tapahtuma.pos[0]
                    y = tapahtuma.pos[1]  
                    if x >= 400 and x <= 500 and y >= 40 and y <= 140:
                        rivi_ok()
                    elif x >= WIDTH - 60 - P_KOKO: 
                        if y != None:
                            vari = varit[mika_vari(y)]
                    else:               
                        monesko_pallo = mika_paikka(x)  # voi olla None
                        if monesko_pallo != None:
                            nykyinen_arvaus[monesko_pallo] = vari
                            x_kohdennettu = X_ALOITUS + monesko_pallo * (P_KOKO * 2 + VALI)

        
        pygame.draw.circle(naytto, (vari), (x_kohdennettu, y_kohdennettu), P_KOKO) 
        piirra_lukitut_pallot(nykyinen_arvaus, y_kohdennettu)     
        valitusteksti(teksti)
        #piirra_valinta(x_valinta, y_valinta)
        pelaaja_tilanne(y_kohdennettu)
        pygame.display.flip() 
        kello.tick(1000)   


pygame.init()
pygame.display.set_caption("MasterMind")
palloja = alkunaytto()
voittorivi = arvo_voittorivi(palloja)
print(voittorivi)
monesko_arvaus = 0
nykyinen_arvaus = {0:val, 1:val, 2:val, 3:val}
arvaukset = []
silmukka()