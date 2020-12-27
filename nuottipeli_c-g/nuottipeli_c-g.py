
import pygame, pygame.midi, random
from yhteiset import *
from nuotti import Nuotti
from gameover import *


def alkuteksti():
    naytto.fill(valkoinen)
    tekstit = []
    tekstit.append("Laita kätesi valmiiksi näppäimille c, d, e, f, g.")
    tekstit.append("Ohjelma kyselee näitä viittä G-avaimen nuottia.")
    tekstit.append("Mietintäaikaa on kunnes nuotti osuu avaimeen.")
    tekstit.append("Paina nyt mitä tahansa, niin peli käynnistyy.")
    y = 90
    for teksti in tekstit:
        t = fontti_keski.render(teksti, True, turkoosi)
        naytto.blit(t, (50, y))
        y += 50
    pygame.display.flip()

    while True:
        for tapahtuma in pygame.event.get(): 
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()
            else:                
                if tapahtuma.type == pygame.KEYDOWN:     
                    return       


def midi_play(n, nykyinen_indeksi):
    #ei voi laskea systeemillä, esim. i+=2, koska välillä on puolisävelaskel välillä koko-
    midi_numbers = {0:60, 1:62, 2:64, 3:65, 4:67}    #60 = keski-c, 67 = g
    midi_out.note_off(midi_numbers[nykyinen_indeksi], 110)
    midi_out.note_on(midi_numbers[n], 110)
    

def lisataanko_vauhtia(pisteet):
    if pisteet % 12 == 0 and pisteet > 0:  #  0%12 == 0  
        return 25
    return 0

def pelitilan_tekstit(vaarin, pisteet):
    teksti = fontti_iso.render(f"Pisteet: {pisteet}", True, turkoosi)
    naytto.blit(teksti, (600, 30))    
    if vaarin:                         
        teksti = fontti_keski.render(f"Väärin. Nuotti on: {nuotti.nykyinen_nimi() }", True, punainen)  
    else:
        teksti = fontti_keski.render("Nuotin nimi?", True, turkoosi)        
    naytto.blit(teksti, (200, 40))    

def nuottiviivasto(viivan_pit):
    for i in range(5):
        pygame.draw.line(naytto, (0, 0, 0), (NUOTTIAV_SIJAINTI, YLIN_VIIVA_Y + i * VIIVOJEN_VALI), (viivan_pit - 15, YLIN_VIIVA_Y + i * VIIVOJEN_VALI), 4)


#############################################################################################################
        
pygame.init()
pygame.display.set_caption("Tunnista nuotin nimi")

pygame.midi.init()
port = pygame.midi.get_default_output_id()
midi_out = pygame.midi.Output(port, 0)
midi_out.set_instrument(10)   # GM 10 = Glockenspiel

fontti_iso = pygame.font.SysFont("Arial", 36)
fontti_keski = pygame.font.SysFont("Arial", 30)
fontti_pieni_bold = pygame.font.SysFont("Arial", 24, bold = True)

nuotti = Nuotti()


def main():
    pisteet = 0
    vaarin = False
    vauhti = 150   # ticks
    nuotti.arvo_nuotti()        
    vari = nuotti.arvo_vari()
    nykyinen_indeksi = nuotti.arvottu_indeksi
    midi_play(nuotti.arvottu_indeksi, nykyinen_indeksi)     

    while True:
        for tapahtuma in pygame.event.get(): 
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()
            else:                
                if tapahtuma.type == pygame.KEYDOWN:                   
                    if chr(tapahtuma.key) == nuotti.nykyinen_nimi():
                        pisteet += 1
                        vauhti += lisataanko_vauhtia(pisteet)
                        vaarin = False
                        nuotti.arvo_nuotti()                        
                        midi_play(nuotti.arvottu_indeksi, nykyinen_indeksi)        # MIDI täällä
                        nykyinen_indeksi = nuotti.arvottu_indeksi   
                        vari = nuotti.arvo_vari()                      
                    else:
                        pisteet -= 1
                        vaarin = True         
            
        naytto.fill(valkoinen)
        naytto.blit(g_avain, (11, 28))
        
        # anaaliin fisti
        if not nuotti.liiku():  
            gameover(pisteet, fontti_iso, fontti_pieni_bold)
            main()

        pygame.draw.circle(naytto, vari, (nuotti.x , nuotti.y), PALLON_KOKO)
        nuottiviivasto(WIDTH)        
        if nuotti.arvottu_indeksi == 0: # keski-c:lle apuviiva
            pygame.draw.line(naytto, (0, 0, 255), (nuotti.x-50, nuotti.y), (nuotti.x+50, nuotti.y), 2)
            
        pelitilan_tekstit(vaarin, pisteet)              
        pygame.display.flip()
        kello.tick(vauhti)
            

alkuteksti()
main()
