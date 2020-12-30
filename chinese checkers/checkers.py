import pygame, copy
from vakiot import *
from gameover import *


def alkunaytto():
    fontti = pygame.font.SysFont("Arial", 26)
    naytto.fill((ruskea))
    y = 140
    for rivi in alkuohjeet():
        teksti = fontti.render(rivi, True, vihrea)
        naytto.blit(teksti, (150, y))
        y += 40
    pygame.display.flip()

    while True:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                 pygame.quit()
            elif tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_1:
                    return 1
                if tapahtuma.key == pygame.K_2:
                    return 2
                if tapahtuma.key == pygame.K_3:
                    return 3
                 

def valitusteksti(text):
    rivit = text.split(".")
    fontti = pygame.font.SysFont("Arial", 18)
    y = HEIGHT - 100
    for rivi in rivit:
        teksti = fontti.render(rivi, True, (200, 0, 0))
        naytto.blit(teksti, (10, y))
        y += 30


def pelaaja_tilanne(koordinaatit, vari, kuulia):         
    for i in range (kuulia):      
        pygame.draw.circle(naytto, vari, koordinaatit[i], P_KOKO)  


def piirra_valinta(x_valinta, y_valinta):
    pygame.draw.circle(naytto, (0, 0, 100), (x_valinta, y_valinta), P_KOKO +4) 


def mika_paikka(x, y, koordinaatit):
    i = 0
    for koordinaatti in koordinaatit:
        if x > koordinaatti[0] - P_KOKO+2 and x < koordinaatti[0] + P_KOKO+2 and y > koordinaatti[1] - P_KOKO+2 and y < koordinaatti[1] + P_KOKO+2:
            return i
        i += 1    

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

def onko_vapaa(x, y, koordinaatit1, koordinaatit2):
    for x_verrokki, y_verrokki in koordinaatit1:
        if x > x_verrokki - P_KOKO+2 and x < x_verrokki + P_KOKO+2 and y > y_verrokki - P_KOKO+2 and y < y_verrokki + P_KOKO+2:
            return False
    for x_verrokki, y_verrokki in koordinaatit2:
        if x > x_verrokki - P_KOKO+2 and x < x_verrokki + P_KOKO+2 and y > y_verrokki - P_KOKO+2 and y < y_verrokki + P_KOKO+2:
            return False
    return True   


def onko_laillinen(x_valinta, x):
    # suoraan ylös / alas laiton, pitää olla diagonaali
    if x > x_valinta - P_KOKO+2 and x < x_valinta + P_KOKO+2 :
        return False
    return True

def silmukka(kuulia):
    siirto = 0
    mika_pallo = 0,0   # pelipaikan keskelle keskitetyt x ja y
    koordinaatit1 = copy.deepcopy(koordinaatit1_orig)
    koordinaatit2 = copy.deepcopy(koordinaatit2_orig)
    teksti = ""
    x_valinta = -30
    y_valinta = -30
    
    while True:
        naytto.blit(lauta, (0,0))
        if siirto % 4 == 0 or siirto % 4 == 1: 
            pygame.draw.circle(naytto, vihrea, (430, 120), P_KOKO*2)
        elif siirto % 4 == 2 or siirto % 4 == 3: 
            pygame.draw.circle(naytto, ruskea, (430, HEIGHT - 130), P_KOKO*2)
        for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    pygame.quit()                
                if tapahtuma.type == pygame.MOUSEBUTTONDOWN:                    
                    siirto += 1
                    x = tapahtuma.pos[0]
                    y = tapahtuma.pos[1]  
                    if siirto % 4 == 1:                        
                        teksti = ""
                        mika_pallo = mika_paikka(x, y,koordinaatit1)      # pel1:n pallo...  
                        if mika_pallo == None:
                            teksti = "Klikkasit tyhjää tai väärää väriä. Valitse siirrettävä pallo uudestaan."
                            siirto -= 1
                            mika_pallo = mika_paikka(x, y,koordinaatit1)                            
                        else:
                            x_valinta, y_valinta = koordinaatit1[mika_pallo]              
                    elif siirto % 4 == 2:  
                        # ...siirretään tänne
                        if not onko_laillinen(x_valinta, x): # tsekataan vain x-sijaintai  TODO: muita tarkistuksia
                            teksti = "Laiton siirto. Siirrä diagonaaviivoja pitkin."
                            siirto -= 1
                        elif onko_vapaa(x, y, koordinaatit1, koordinaatit2):
                            koordinaatit1[mika_pallo] = x, y
                            teksti = ""
                            x_valinta = -30
                            y_valinta = -30                        
                        else:
                            teksti = "Kohteessa on jo pallo. Valitse kohde uudestaan."                            
                            siirto -= 1
                        if onko_voitto(koordinaatit1, koordinaatit2_orig, kuulia):
                            gameover(siirto // 4, naytto)
                            silmukka()
                    elif siirto % 4 == 3:
                        teksti = ""
                        mika_pallo = mika_paikka(x, y,koordinaatit2)      # pel2:n pallo...
                        if mika_pallo == None:                            
                            teksti = "Klikkasit tyhjää tai väärää väriä. Valitse uudestaan."
                            siirto -= 1
                            mika_pallo = mika_paikka(x, y,koordinaatit2)   
                        else:                            
                            x_valinta, y_valinta = koordinaatit2[mika_pallo]    
                    elif siirto % 4 == 0:  
                        # ...siirretään tänne
                        if not onko_laillinen(x_valinta, x): # tsekataan vain x-sijaintai  TODO: muita tarkistuksia
                            teksti = "Laiton siirto. Siirrä diagonaaviivoja pitkin."
                            siirto -= 1
                        elif onko_vapaa(x, y, koordinaatit1, koordinaatit2):
                            koordinaatit2[mika_pallo] = x, y
                            teksti = ""
                            x_valinta = -30
                            y_valinta = -30
                        else:
                            teksti = "Kohteessa on jo pallo. Valitse kohde uudestaan."                            
                            siirto -= 1
                        if onko_voitto(koordinaatit2, koordinaatit1_orig, kuulia):
                            gameover(siirto // 4, naytto)
                            silmukka()

        valitusteksti(teksti)
        piirra_valinta(x_valinta, y_valinta)
        pelaaja_tilanne(koordinaatit1, vihrea, kuulia) 
        pelaaja_tilanne(koordinaatit2, ruskea, kuulia)
        pygame.display.flip() 
        kello.tick(1000)   


pygame.init()
pygame.display.set_caption("Chinese Checkers")
kuulia = alkunaytto()
muunna = {1:6, 2:10, 3:15}   # käyttäjän valinta : kuulien määrä
kuulia_lisarivit(muunna[kuulia])
silmukka(muunna[kuulia])