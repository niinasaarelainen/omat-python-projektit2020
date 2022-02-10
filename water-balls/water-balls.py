import pygame, pygame.midi, random
from nuotti import *
from yhteiset import *

        
pygame.init()
pygame.display.set_caption("Water")

pygame.midi.init()
port = pygame.midi.get_default_output_id()
midi_out = pygame.midi.Output(port, 0)
midi_out.set_instrument(10)   # GM 10 = Glockenspiel

fontti_iso = pygame.font.SysFont("Arial", 36)
fontti_keski = pygame.font.SysFont("Arial", 30)
fontti_pieni_bold = pygame.font.SysFont("Arial", 24, bold = True)

nuotti = Nuotti()
nuotit = []


def arvo_nuotti():
        nuotti.arvo_nuotti()   
        midi_out.note_on(nuotti.arvottu_indeksi + 81, 50)        
        nuotit.append(nuotti)
    
def liikuta_nuotit():
    for nuotti in nuotit:
        nuotti.y += 5
        vari = nuotti.arvo_vari()   
        pygame.draw.circle(naytto, vari, (nuotti.x , nuotti.y), PALLON_KOKO)


def main():
    vauhti = 5   # ticks  

    while True:
        naytto.fill(valkoinen)        

        for tapahtuma in pygame.event.get(): 
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()
    
        arvo_nuotti()  
        liikuta_nuotit()

        pygame.display.flip()
        kello.tick(vauhti)
            

main()