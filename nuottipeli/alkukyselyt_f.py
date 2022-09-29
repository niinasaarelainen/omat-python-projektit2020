import pygame
from yhteiset import *



def nayta_alue(fontti_keski, fontti_pieni, fontti_pieni_b):
        
    naytto.fill(valkoinen)    
    nuottiviivasto(280)
    naytto.blit(f_avain, (11, 68))
    pygame.draw.line(naytto, musta, (200 ,YLIN_VIIVA + 5 * VIIVOJEN_VALI), (280 ,YLIN_VIIVA + 5 * VIIVOJEN_VALI), 4)    
    teksti = "Klikkaa haluamaasi alinta ja ylintä nuotin paikkaa " 
    teksti = fontti_keski.render(teksti, True, musta)
    naytto.blit(teksti, (106, 25))

    teksti = fontti_pieni_b.render("yläraja = a", True, turkoosi)
    naytto.blit(teksti, (280, YLIN_VIIVA - 16))
    teksti1 = fontti_pieni_b.render("alaraja =" , True, turkoosi)
    teksti2 = fontti_pieni_b.render("matala e" , True, turkoosi)
    naytto.blit(teksti1, (290, YLIN_VIIVA + 5 * VIIVOJEN_VALI-15))
    naytto.blit(teksti2, (290, YLIN_VIIVA + 5 * VIIVOJEN_VALI-15 + 20))   
        
    pygame.display.flip()
    return pelivalinnat_alue(fontti_keski, fontti_pieni, fontti_pieni_b)


def tarkista_nuotti(nuotti):
        if nuotti < 0:
            return 0
        elif nuotti > 10:
            return 10
        else:
            return nuotti


def pelivalinnat_alue(fontti_keski, fontti_pieni, fontti_pieni_b):

    alin_ja_ylin = []
        
    while True:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()
            else:
                if tapahtuma.type == pygame.MOUSEBUTTONDOWN:

                    nuotin_ind = int((tapahtuma.pos[1] + 10 - YLIN_VIIVA) / (VIIVOJEN_VALI/2))
                    nuotin_ind = tarkista_nuotti(nuotin_ind)
                    y = YLIN_VIIVA + nuotin_ind * int(VIIVOJEN_VALI/2)                    
                    print(nuotin_ind, y)
                    pygame.draw.circle(naytto, turkoosi, (240, y), PALLON_KOKO)                    
                    pygame.display.flip()
                    alin_ja_ylin.append(nuotin_ind)

        if len(alin_ja_ylin) == 1 :
            teksti1 = fontti_pieni.render("Klikkaa vielä nuottien kyselyalueen", True, musta)
            teksti2 = fontti_pieni.render("toinen raja", True, musta)
            naytto.blit(teksti1, (405, HEIGHT - 280))
            naytto.blit(teksti2, (530, HEIGHT - 250))
            pygame.display.flip()
        
        elif len(alin_ja_ylin) == 2:
            return alin_ja_ylin # ylin viiva = 0, alin = 8

    


def kysy_nappaimet(fontti_keski, fontti_pieni, fontti_pieni_b):
        
    naytto.fill((valkoinen))
    teksti = "Kumpaa tapaa haluat käyttää syötteen antamiseen?" 
    teksti = fontti_keski.render(teksti, True, musta)
    naytto.blit(teksti, (110, 30))
    teksti = "Paina näppäintä 1 tai 2" 
    teksti = fontti_keski.render(teksti, True, musta)
    naytto.blit(teksti, (110, 60))

    teksti1 = fontti_pieni_b.render("1 = Näppäimet c-h: ", True, turkoosi)
    teksti2 = fontti_pieni.render("näppäin c = nuotti c, näppäin d = nuotti d ...", True, turkoosi)
    naytto.blit(teksti1, (110, 145))
    naytto.blit(teksti2, (115, 175))

    teksti = fontti_pieni_b.render("2 = Pianistin tapa, vierekkäiset näppäimet: ", True, turkoosi)
    naytto.blit(teksti, (110, 235))
    piano = pygame.image.load('img\piano.png').convert_alpha()                    # pianon kuva
    piano = pygame.transform.scale(piano, (366, 135))             
    naytto.blit(piano, (116, 265))
    pygame.display.flip()
        
    while True:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()
            else:
                if tapahtuma.type == pygame.KEYDOWN:                    
                    if chr(tapahtuma.key) == "1":
                        return 1
                    elif chr(tapahtuma.key) == "2":
                        return 2    