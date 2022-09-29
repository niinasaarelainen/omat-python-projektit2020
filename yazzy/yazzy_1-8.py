from yazzy_apufunktiot import *
from noppa import *
import pygame


def alkunaytto():
    naytto.fill((255, 255, 255))
    y = 40
    for rivi in alkuohjeet():
        teksti = fontti.render(rivi, True, (0, 20, 20))
        naytto.blit(teksti, (50, y))
        y += 35
    pygame.display.flip()

    while True:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                 pygame.quit()
            elif tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                 return

def mitä_puuttuu(kerätään):
    y = 130
    teksti = fontti_pieni.render("Vielä puuttuu:", True, (0, 20, 20))
    naytto.blit(teksti, (540, y))
    for item in kerätään:
        y += 20
        teksti = fontti_pieni.render(f" - {item}", True, (0, 20, 20))
        naytto.blit(teksti, (540, y))    


def tulos(heitto, kerätään):
    mika_tuli = "Et saanut mitään..."          
    lista = []
    for noppa in heitto:    
        lista.append(noppa.luku)
        noppa.valittu = False
    setti = set(lista)    

    parillinen = True
    for noppa in setti:
        if noppa % 2 != 0:
            parillinen = False
    if parillinen == True and  "parilliset" in kerätään:
        mika_tuli = "parilliset"

    parittomat = True
    for noppa in setti:
        if noppa % 2 != 1:
            parittomat = False
    if parittomat == True and  "parittomat" in kerätään:
        mika_tuli = "parittomat"

    useita = {}
    for i in range(1,MAX_SILMALUKU + 1):   # lukemat 1-6 merkitään näin !!!! (muista 7-1 = 6)
        if lista.count(i) >= 2:
            useita[i] = lista.count(i) 

    if len(useita) == 2:
        if 3 not in useita.values():
            if "kaksi paria" in kerätään:                
                mika_tuli = "kaksi paria"
    if 3 in useita.values():
        if 2 in useita.values():
            if "täyskäsi" in kerätään:                
                mika_tuli = "täyskäsi"
            elif "kolmoset" in kerätään:
                mika_tuli = "kolmoset"   
            elif "kaksi paria" in kerätään:
                mika_tuli = "kaksi paria"
        else:    
            if "kolmoset" in kerätään:
                mika_tuli = "kolmoset"
    if 4 in useita.values():
        if "neloset" in kerätään:            
            mika_tuli = "neloset"
        elif "kolmoset" in kerätään:
            mika_tuli = "kolmoset"     
    if 5 in useita.values():
        if "Y A Z Z Y ! ! !" in kerätään:            
            mika_tuli = "Y A Z Z Y ! ! !"
        elif "neloset" in kerätään:
            mika_tuli = "neloset"
        elif "kolmoset" in kerätään:
            mika_tuli = "kolmoset"         

    if {1,2,3,4,5}.issubset(setti):    
        if "suora 1-5" in kerätään:  
            mika_tuli = "suora 1-5"             

    if {2,3,4,5,6}.issubset(setti):   
        if "suora 2-6" in kerätään:  
            mika_tuli = "suora 2-6"  

    if {3,4,5,6,7}.issubset(setti):   
        if "suora 3-7" in kerätään:  
            mika_tuli = "suora 3-7"

    if {4,5,6,7,8}.issubset(setti):   
        if "suora 4-8" in kerätään:  
            mika_tuli = "suora 4-8"

    if mika_tuli in kerätään:       
        kerätään.remove(mika_tuli) 
        
    return mika_tuli
   

def piirra(heitto):
    x = EKA_NOPPA_X
    for noppa in heitto:
        naytto.blit(noppa.kuva(), (x, 160))
        x += NOPPIEN_VALI + KUVAN_KOKO


def valintatekstit():
    teksti = fontti.render("Klikkaa mitkä nopat haluat säilyttää ja lopuksi  OK ", True, (0, 20, 20))    
    naytto.blit(teksti, (50, 50))
    teksti = fontti.render(" VALITSE KAIKKI ", True, (0, 220, 220))
    naytto.blit(teksti, (80, HEIGHT // 2 + 50))
    teksti = fontti.render(" OK ", True, (0, 220, 0))
    naytto.blit(teksti, (WIDTH // 2 -80, HEIGHT // 2 + 50))
    

def toggle_valittu(klikkaus, heitto):
    hiiri_x, hiiri_y = klikkaus
    if hiiri_x < EKA_NOPPA_X:
        hiiri_x = EKA_NOPPA_X 
    if hiiri_x > EKA_NOPPA_X + ((KUVAN_KOKO + NOPPIEN_VALI) * 5):    # 5 = noppien väli
        hiiri_x = EKA_NOPPA_X + ((KUVAN_KOKO + NOPPIEN_VALI)* 5) - NOPPIEN_VALI // 2 

    nopan_nro = (hiiri_x - EKA_NOPPA_X) // (KUVAN_KOKO + NOPPIEN_VALI)
    heitto[nopan_nro].toggle_valittu()
    return heitto

def nollaa_valintakuvat(heitto):
    for noppa in heitto:
        noppa.valittu = False
    return heitto       


def silmukka():                                                        
    kerätään = mitä_kerätään()    
    klikattu_ok = False
    win = False
    heitto_123 = 1  # max 3
    kierros = 1   # max 12
    heitto = valitse_5_randomia(nopat)

    while kierros <= KIERROKSIA and len(kerätään) > 0:       
        naytto.fill((255, 255, 255))             
        valintatekstit()    
        teksti = fontti.render(f" kierros {kierros}/{KIERROKSIA} ,  heitto {heitto_123} ", True, (200, 0, 20))
        naytto.blit(teksti, (100, HEIGHT - 60))
        piirra(heitto)
        mitä_puuttuu(kerätään)
        pygame.display.flip()           

        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()                
            if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                x = tapahtuma.pos[0]
                y = tapahtuma.pos[1]
                # nopat:
                if y < HEIGHT // 2 + 40 and y > HEIGHT // 2 - 50:   # ei laiteta ok:lle reunoja !!!
                    heitto = toggle_valittu(tapahtuma.pos, heitto)
                # valitse kaikki:
                if x >= 80 and  x <= WIDTH // 2 -100 and y >= HEIGHT // 2 + 50 and y <= HEIGHT // 2 + 75:
                    if len([noppa for noppa in heitto if noppa.valittu == True]) == 5:                        
                        for noppa in heitto:
                            noppa.toggle_valittu()
                    else:
                        for noppa in heitto:
                            noppa.valittu = True
                # ok:
                elif x > 312 and  x < 360 and y > 253 and y < 282:   # ok                       
                    klikattu_ok = True   
                
                if klikattu_ok:
                    klikattu_ok = False
                    heitto_123 += 1                    
                    heitto = valitse_lukitsemattomat(heitto)    # oli heitto
                   
                    if heitto_123 == 3:                         
                        naytto.fill((255, 255, 255))
                        mika_tuli = tulos(heitto, kerätään)                        
                        piirra(heitto)
                        teksti = fontti.render(mika_tuli, True, (40, 40, 220))
                        naytto.blit(teksti, (220, 300))
                        if not "Et " in mika_tuli:
                            naytto.blit(clap, (320, 300))
                        pygame.display.flip()   
                        pygame.time.delay(2500)  # 2,5 sekunnin viive
                        heitto_123 = 1
                        kierros += 1
                        heitto = valitse_5_randomia(nopat)
                    else:                        
                        valintatekstit()   
                    
        if len(kerätään)== 0:
            win = True
        pygame.display.flip() 
        kello.tick(100)   
        # END WHILE

            
    naytto.fill((255, 255, 255))
    if win:
        teksti = fontti.render(" Voitit !!! ", True, (200, 0, 20))
    else:
        montako_oikein = max_mita_kerataan - len(kerätään)
        teksti = fontti.render(f" Hävisit. Sait kerättyä {montako_oikein}/{max_mita_kerataan}", True, (200, 0, 20))
    naytto.blit(teksti, (66, HEIGHT - 60))
    pygame.display.flip()
    pygame.time.delay(2500)  
    silmukka()
                        

 # # # # # #     MAIN     # # # # # # # # # #

pygame.init()
WIDTH = 780
HEIGHT = 410
EKA_NOPPA_X = 80
KIERROKSIA = 22

naytto = pygame.display.set_mode((WIDTH, HEIGHT))
kello = pygame.time.Clock()

fontti = pygame.font.SysFont("Arial", 26)
fontti_pieni = pygame.font.SysFont("Arial", 18)

clap = pygame.image.load('img\clap_hands_animation.gif').convert_alpha()
clap = pygame.transform.scale(clap, (100, 100) )

alkunaytto()
ei_valitut, valitut = nopat_listaan()
nopat = muodosta_nopat(ei_valitut, valitut)   # 5 kpl Noppa-oliota
max_mita_kerataan = len(mitä_kerätään())
      
silmukka()