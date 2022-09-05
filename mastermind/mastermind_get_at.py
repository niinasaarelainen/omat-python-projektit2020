import pygame, copy, random
from vakiot import *
from gameover import *


def alkunaytto():    
    naytto.fill((val))
    y = 130
    for rivi in alkuohjeet():
        teksti = fontti_iso.render(rivi, True, vih)
        naytto.blit(teksti, (150, y))
        y += 40
    pygame.display.flip()

    while True:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                 pygame.quit()
            elif tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_3:
                    return 3
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


def tyhjat_pallot(y):   
    x = X_ALOITUS   
    for i in range (palloja):      
        pygame.draw.circle(naytto, mus, (x, y), P_KOKO, 2)  
        x += P_KOKO * 2 + VALI


def piirra_valinta(x_valinta, y_valinta):
    pygame.draw.circle(naytto, (0, 0, 100), (x_valinta, y_valinta), P_KOKO) 


def varivalikoima():     # oikealla:
    x = WIDTH - 55
    y = Y_ALOITUS
    for vari in varit:
        if blokkaa_varit and vari not in voittorivi:  # jos on painettu V
            pass
        else:
            pygame.draw.circle(naytto, (vari), (x, y), P_KOKO) 
        y += P_KOKO * 2 + VALI


def  mika_vari(y):    
    # värivalikoima oikealla:
    y = (y - Y_ALOITUS + P_KOKO) // (P_KOKO * 2 + VALI) 
    if y >= 0 and y <= len(varit) -1:
        return y
    return None


def mika_paikka(x):   
    # "tyhjät" pallot:
    x = (x - X_ALOITUS + P_KOKO) // (P_KOKO * 2 + VALI) 
    if x >= 0 and x <= palloja -1:
        return x
    return None


def piirra_lukitut_pallot(nykyinen_arvaus, y_kohdennettu) :   
    for i in range(len(nykyinen_arvaus)):
        x_kohdennettu = X_ALOITUS + i * (P_KOKO * 2 + VALI)
        pygame.draw.circle(naytto, (nykyinen_arvaus[i]), (x_kohdennettu, y_kohdennettu), P_KOKO) 
    y = Y_ALOITUS
    for arvaus in arvaukset:
        for i in range(len(arvaus)):
            x_kohdennettu = X_ALOITUS + i * (P_KOKO * 2 + VALI)
            pygame.draw.circle(naytto, (arvaus[i]), (x_kohdennettu, y), P_KOKO) 
        y += P_KOKO * 2 + VALI


def rivi_ok():
    global nykyinen_arvaus, monesko_arvaus, arvaukset
    oikealla_paikalla = 0
    oikea_vari_vaaralla_paikalla = 0
    voittorivi_temp = copy.deepcopy(voittorivi)
    nykyinen_arvaus_temp = copy.deepcopy(nykyinen_arvaus)
    arvaukset.append(nykyinen_arvaus)
    for i in range(palloja):
        if nykyinen_arvaus_temp[i] == voittorivi_temp[i]:
            oikealla_paikalla += 1
            voittorivi_temp[i] = mus
            nykyinen_arvaus_temp[i] = val
    for i in range(palloja):
        if nykyinen_arvaus_temp[i] in voittorivi_temp:
            oikea_vari_vaaralla_paikalla += 1
            ind = voittorivi_temp.index(nykyinen_arvaus_temp[i])
            voittorivi_temp[ind] = mus
    nykyinen_arvaus = {0:val, 1:val, 2:val, 3:val, 4:val, 5:val}
    monesko_arvaus += 1
    return oikealla_paikalla, oikea_vari_vaaralla_paikalla


def piirra_tuomiot():
    x = 22
    y =  Y_ALOITUS
    for mustia, valkoisia in tuomiot:  # tuomio = tuple
        for i in range(mustia):
            pygame.draw.circle(naytto, (mus), (x, y), OIKEIN_KOKO) 
            x += 20
        for i in range(valkoisia):
            pygame.draw.circle(naytto, (mus), (x, y), OIKEIN_KOKO, 2)  # valkoinen jossa mustat reunat
            x += 20
        y += (P_KOKO * 2 + VALI)
        x = 20

def nayta_oikea_vastaus():
    x = 365
    y = HEIGHT - 40
    for pallo in voittorivi:  
        pygame.draw.circle(naytto, (pallo), (x, y), P_KOKO) 
        x +=  (P_KOKO * 2 + VALI - 2)

def lopputeksti():
    global palloja
    pygame.draw.rect(naytto, val, pygame.Rect(0, HEIGHT - 70, WIDTH, HEIGHT))
    teksti = fontti_iso.render("Et ehtinyt ratkaista.", True, vih)
    naytto.blit(teksti, (50, HEIGHT- 80))
    teksti = fontti_iso.render("ENTER = Uusi peli", True, vih)
    naytto.blit(teksti, (50, HEIGHT- 40))
    nayta_oikea_vastaus()
    pygame.display.flip()
    uusi_peli()

def uusi_peli():
    global palloja, voittorivi, monesko_arvaus, nykyinen_arvaus, arvaukset, tuomiot
    while True:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                 pygame.quit()
            elif tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_RETURN:
                    palloja = alkunaytto()
                    voittorivi = arvo_voittorivi(palloja)
                    monesko_arvaus = 0
                    nykyinen_arvaus = {0:val, 1:val, 2:val, 3:val, 4:val, 5:val}
                    arvaukset = []
                    tuomiot = []      
                    silmukka()
  


def silmukka(): 
    global vari, blokkaa_varit
    y_kohdennettu = Y_ALOITUS + monesko_arvaus * (P_KOKO * 2 + VALI)  
    alateksti = True 
    kaikki_oikein = False
    blokkaa_varit = False
    
    while monesko_arvaus <= 10:
        naytto.fill((val))
        naytto.blit(ok,  (480, y_kohdennettu - 10))
        y_kohdennettu = Y_ALOITUS + (monesko_arvaus * (P_KOKO * 2 + VALI)) 
        varivalikoima() 
        piirra_lukitut_pallot(nykyinen_arvaus, y_kohdennettu)          
        for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    pygame.quit()  
                elif tapahtuma.type == pygame.KEYDOWN:
                    if tapahtuma.key == pygame.K_SPACE:                         
                        alateksti = False    
                    if tapahtuma.key == pygame.K_v:
                        blokkaa_varit = True       
                elif tapahtuma.type == pygame.MOUSEBUTTONDOWN:    
                    x = tapahtuma.pos[0]
                    y = tapahtuma.pos[1]  

                    #ok-nappi
                    if x >= 480 and x <= 580 and y >= y_kohdennettu -40 and y <= y_kohdennettu + 70:
                        tuomio = rivi_ok()
                        tuomiot.append(tuomio)
                        if tuomio[0] == palloja:
                            kaikki_oikein = True
                            alateksti = False                           
                    
                    # uusin rivi
                    elif y >= y_kohdennettu -22 and y <= y_kohdennettu + 22 and x < 480 :  
                        monesko_pallo = mika_paikka(x)  # voi olla None
                        if monesko_pallo != None:
                            nykyinen_arvaus[monesko_pallo] = vari

                    # ota väri
                    else:
                        vari = naytto.get_at((x, y))[:3]
                            
        piirra_lukitut_pallot(nykyinen_arvaus, y_kohdennettu)   
                
        if kaikki_oikein:
            teksti = fontti_iso.render("JESS!! Kaikki oikein", True, vih)
            naytto.blit(teksti, (X_ALOITUS -30, y_kohdennettu + 35))
            teksti = fontti_iso.render("ENTER = Uusi peli", True, vih)
            naytto.blit(teksti, (X_ALOITUS -30, y_kohdennettu + 66))
            pygame.display.flip()
            uusi_peli()
        else:
            tyhjat_pallot(y_kohdennettu)
        if alateksti:
            teksti = fontti_pieni.render("V = Näytä oikeat värit", True, vih)
            naytto.blit(teksti, (325, HEIGHT - 40))
            teksti = fontti_pieni.render("Space = Näytä oikea vastaus", True, vih)
            naytto.blit(teksti, (325, HEIGHT - 80))
        elif not kaikki_oikein:
            nayta_oikea_vastaus()  
        y_kohdennettu =  y_kohdennettu - (P_KOKO * 2 + VALI)
        piirra_tuomiot()  
        pygame.display.flip() 
        kello.tick(4000)   

    lopputeksti()


pygame.init()
fontti_iso = pygame.font.SysFont("Arial", 32)      
fontti_pieni = pygame.font.SysFont("Arial", 25)
pygame.display.set_caption("MasterMind")
palloja = alkunaytto()
voittorivi = arvo_voittorivi(palloja)
monesko_arvaus = 0
nykyinen_arvaus = {0:val, 1:val, 2:val, 3:val, 4:val, 5:val}
arvaukset = []
tuomiot = []    
vari = val  
blokkaa_varit = False
#blokattavat_varit = []
silmukka()