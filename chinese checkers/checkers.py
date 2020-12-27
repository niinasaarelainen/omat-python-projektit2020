import pygame, copy
from vakiot import *
from gameover import *

def pelaaja_tilanne(koordinaatit, vari):           
    pygame.draw.circle(naytto, vari, koordinaatit[0], P_KOKO)
    #2.rivi:
    pygame.draw.circle(naytto, vari, koordinaatit[1], P_KOKO)
    pygame.draw.circle(naytto, vari, koordinaatit[2], P_KOKO)
    #3.rivi:
    pygame.draw.circle(naytto, vari, koordinaatit[3], P_KOKO)
    pygame.draw.circle(naytto, vari, koordinaatit[4], P_KOKO)
    pygame.draw.circle(naytto, vari, koordinaatit[5], P_KOKO)
    # 4.rivi:


def mika_paikka(x, y, koordinaatit):
    i = 0
    for koordinaatti in koordinaatit:
        if x > koordinaatti[0] - P_KOKO+2 and x < koordinaatti[0] + P_KOKO+2 and y > koordinaatti[1] - P_KOKO+2 and y < koordinaatti[1] + P_KOKO+2:
            return i
        i += 1    

def onko_voitto(mita_Verrataan, mihin_verrataan):   
    sijainnit = []
    for x, y in mita_Verrataan:
        for  i in range(6):
            if x > mihin_verrataan[i][0] - P_KOKO+2 and x < mihin_verrataan[i][0] + P_KOKO+2 and y > mihin_verrataan[i][1] - P_KOKO+2 and y < mihin_verrataan[i][1] + P_KOKO+2:
                sijainnit.append(i)
    print(sijainnit)
    if len(set(sijainnit)) == 2:
        return True
    return False


def silmukka():
    siirto = 0
    mika_pallo = 0,0
    koordinaatit1 = copy.deepcopy(koordinaatit1_orig)
    koordinaatit2 = copy.deepcopy(koordinaatit2_orig)
    while True:
        naytto.blit(lauta, (0,0))
        if siirto % 4 == 0 or siirto % 4 == 1: 
            pygame.draw.circle(naytto, vihrea, (180, 50), P_KOKO*2)
        elif siirto % 4 == 2 or siirto % 4 == 3: 
            pygame.draw.circle(naytto, ruskea, (180, HEIGHT - 70), P_KOKO*2)
        for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    pygame.quit()                
                if tapahtuma.type == pygame.MOUSEBUTTONDOWN:                    
                    siirto += 1
                    x = tapahtuma.pos[0]
                    y = tapahtuma.pos[1]  
                    if siirto % 4 == 1:
                        mika_pallo = mika_paikka(x, y,koordinaatit1)      # pel1:n pallo...     
                        if mika_pallo == None:
                            print("None")
                            siirto -= 1
                            mika_pallo = mika_paikka(x, y,koordinaatit1)                  
                    elif siirto % 4 == 2:  
                        koordinaatit1[mika_pallo] = x, y    # ...siirretään tänne
                        if onko_voitto(koordinaatit1, koordinaatit2_orig):
                            gameover(siirto // 4, naytto)
                            silmukka()
                    elif siirto % 4 == 3:
                        mika_pallo = mika_paikka(x, y,koordinaatit2)      # pel2:n pallo...
                        if mika_pallo == None:
                            print("None")
                            siirto -= 1
                            mika_pallo = mika_paikka(x, y,koordinaatit2)       
                    elif siirto % 4 == 0:  
                        koordinaatit2[mika_pallo] = x, y    # ...siirretään tänne
                        if onko_voitto(koordinaatit2, koordinaatit1_orig):
                            gameover(siirto // 4, naytto)
                            silmukka()

        
        pelaaja_tilanne(koordinaatit1, vihrea)
        pelaaja_tilanne(koordinaatit2, ruskea)
        pygame.display.flip() 
        kello.tick(100)   


pygame.init()
pygame.display.set_caption("Chinese Checkers")
silmukka()