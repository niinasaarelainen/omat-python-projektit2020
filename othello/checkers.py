import pygame, copy
from vakiot import *


def alkunaytto():
    fontti = pygame.font.SysFont("Arial", 26)
    naytto.fill((sininen))
    y = 140
    for rivi in alkuohjeet():
        teksti = fontti.render(rivi, True, punainen)
        naytto.blit(teksti, (150, y))
        y += 40
    pygame.display.flip()
                 

def valitusteksti(text):
    rivit = text.split(".")
    fontti = pygame.font.SysFont("Arial", 18)
    y = HEIGHT - 100
    for rivi in rivit:
        teksti = fontti.render(rivi, True, (200, 0, 0))
        naytto.blit(teksti, (10, y))
        y += 30


def pelaaja_tilanne(vari, kuulia, x, y):         
    for i in range (kuulia):      
        pygame.draw.circle(naytto, vari, (x, y), P_KOKO)  


def piirra_valinta(x_valinta, y_valinta):
    pygame.draw.circle(naytto, (0, 0, 100), (x_valinta, y_valinta), P_KOKO +4) 


def mika_paikka(x, y):
    i = 0
    # mieti tämä
    
    return i

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

def onko_vapaa(x, y):
    
    return True   


def onko_laillinen(x_valinta, x, y_valinta, y):
    # suoraan ylös / alas laiton, paitsi pidemmät hypyt y-suunnassa (tyhjän kautta)
    print(abs(y_valinta - y) , VALI * 2  - 10 )
    if x > x_valinta - P_KOKO+2 and x < x_valinta + P_KOKO+2 and abs(y_valinta - y) < VALI * 2 + 15 :    # TODO
        return False
    return True

def silmukka(kuulia):
    siirto = 0
    mika_pallo = 0,0   # pelipaikan keskelle keskitetyt x ja y
    teksti = ""
    x_valinta = -30
    y_valinta = -30
    
    while True:
        naytto.blit(lauta, (0,0))
        if siirto % 4 == 0 or siirto % 4 == 1: 
            pygame.draw.circle(naytto, punainen, (430, 120), P_KOKO*2)
        elif siirto % 4 == 2 or siirto % 4 == 3: 
            pygame.draw.circle(naytto, sininen, (430, HEIGHT - 130), P_KOKO*2)
        for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    pygame.quit()                
                if tapahtuma.type == pygame.MOUSEBUTTONDOWN:                    
                    siirto += 1
                    x = tapahtuma.pos[0]
                    y = tapahtuma.pos[1]  
                    if siirto % 4 == 1:                        
                        teksti = ""
                        mika_pallo = mika_paikka(x, y)      # pel1:n pallo...  
                        if mika_pallo == None:
                            teksti = "Klikkasit tyhjää tai väärää väriä. Valitse siirrettävä pallo uudestaan."
                            siirto -= 1
                            mika_pallo = mika_paikka(x, y)                            
                        else:
                            #x_valinta, y_valinta = koordinaatit1[mika_pallo]     
                            pass         
                    elif siirto % 4 == 2:  
                        # ...siirretään tänne
                        if not onko_laillinen(x_valinta, x, y_valinta, y): 
                            teksti = "Laiton siirto. Siirrä diagonaaviivoja pitkin."
                            siirto -= 1
                        elif onko_vapaa(x, y):
                            teksti = ""
                            x_valinta = -30   # "nollaus"
                            y_valinta = -30                        
                        else:
                            teksti = "Kohteessa on jo pallo. Valitse kohde uudestaan."                            
                            siirto -= 1
                        if onko_voitto(kuulia):
                            silmukka()
                    elif siirto % 4 == 3:
                        teksti = ""
                        mika_pallo = mika_paikka(x, y)      # pel2:n pallo...
                        if mika_pallo == None:                            
                            teksti = "Klikkasit tyhjää tai väärää väriä. Valitse uudestaan."
                            siirto -= 1
                            mika_pallo = mika_paikka(x, y)   
                        else:                            
                            #x_valinta, y_valinta = koordinaatit2[mika_pallo]    
                            pass
                    elif siirto % 4 == 0:  
                        # ...siirretään tänne
                        if not onko_laillinen(x_valinta, x, y_valinta, y): 
                            teksti = "Laiton siirto. Siirrä diagonaaviivoja pitkin."
                            siirto -= 1
                        elif onko_vapaa(x, y):
                            #koordinaatit2[mika_pallo] = x, y
                            teksti = ""
                            x_valinta = -30
                            y_valinta = -30
                        else:
                            teksti = "Kohteessa on jo pallo. Valitse kohde uudestaan."                            
                            siirto -= 1
                        if onko_voitto(kuulia):
                            silmukka()

        valitusteksti(teksti)
        piirra_valinta(x_valinta, y_valinta)
        pelaaja_tilanne(punainen, kuulia, x_valinta, y_valinta)   # x_valinta, y_valinta muutettu onko järkeä
        pelaaja_tilanne(sininen, kuulia)
        pygame.display.flip() 
        kello.tick(1000)   


pygame.init()
pygame.display.set_caption("Chinese Checkers")
kuulia = alkunaytto()
muunna = {1:6, 2:10, 3:15}   # käyttäjän valinta : kuulien määrä
silmukka(muunna[kuulia])