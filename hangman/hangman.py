import pygame, copy
from vakiot import *
from ukko import *
from sana import *



def alustus():
    global onsanassa, eiolesanassa
    onsanassa = []
    eiolesanassa = []
    sana.valitsesana()
    

def viivat():
    x = SANA_X
    for i in range(8):   # kaikki sanat 8 kirjainta
        pygame.draw.line(naytto, ruskea, (x, SANA_Y), (x + 31, SANA_Y), 3)
        x += 44

def  eiole_naytolle():
    naytto.blit(fontti_pieni.render("Sanassa ei ole:", True, ruskea), (SANA_X, SANA_Y + 50))
    x = SANA_X
    y = SANA_Y + 100
    for kirjain in eiolesanassa:
        naytto.blit(fontti_pieni.render(kirjain, True, ruskea), (x, y))
        x += 29

def  on_sanassa():
    y = SANA_Y - 80
    for kirjain in onsanassa:
        for i in range(8):
            if sana.valittusana[i] == kirjain:
                naytto.blit(fontti.render(kirjain, True, ruskea), (SANA_X + i * 44, y))

def lopetus(teksti):
    global eiolesanassa
    while True:
        naytto.fill(vihrea)
        naytto.blit(fontti.render(teksti, True, ruskea), (30, 80))
        naytto.blit(fontti_pieni.render("Uusi peli = ", True, ruskea), (30, 220))
        naytto.blit(fontti_pieni.render("any key", True, ruskea), (30, 290))
        for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    pygame.quit()                
                if tapahtuma.type == pygame.KEYDOWN:
                    alustus()
                    main()

        pygame.display.flip() 
        kello.tick(10)   


def main():
    
    while len(eiolesanassa) < len(ukko.osat) :
        naytto.fill(vihrea)
        for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    pygame.quit()                
                if tapahtuma.type == pygame.KEYDOWN:
                    if chr(tapahtuma.key) in sana.valittusana or "ä" in sana.valittusana or "ö" in sana.valittusana:
                        if tapahtuma.key == 39:
                            onsanassa.append('ä')
                        elif tapahtuma.key == 59:
                            onsanassa.append('ö')
                        else:
                            onsanassa.append(chr(tapahtuma.key))
                    else:
                        if tapahtuma.key == 39:
                            eiolesanassa.append('ä')
                        elif tapahtuma.key == 59:
                            eiolesanassa.append('ö')
                        else:
                            eiolesanassa.append(chr(tapahtuma.key))
                        

        viivat()
        ukko.piirra(naytto, len(eiolesanassa))        
        on_sanassa()        
        eiole_naytolle()
        pygame.display.flip() 
        kello.tick(10)   
        if set(onsanassa) == set(sana.valittusana) and len(set(onsanassa)) != 0:
            lopetus("Voitit!!")
    
    lopetus("Hävisit!!")
    


pygame.init()
pygame.display.set_caption("Hangman")
fontti = pygame.font.SysFont("FreeMono", 72)
fontti_pieni = pygame.font.SysFont("FreeMono", 42)
ukko = Ukko()
ukko.osat_taulukkoon()
sana = Sana()
sana.sanalista()

onsanassa = []
eiolesanassa = []

main()