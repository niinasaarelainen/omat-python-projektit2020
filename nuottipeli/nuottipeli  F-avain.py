import pygame, pygame.midi
from alkukyselyt_f import *
from yhteiset import *
from nuotti_f import Nuotti
from gameover import *

    

def midi_play(n, nykyinen_indeksi):
    #ei voi laskea systeemillä, esim. i+=2, koska välillä on puolisävelaskel välillä koko-
    midi_numbers = {0:57, 1:55, 2:53, 3:52, 4:50, 5:48, 6:47, 7:45, 8:43, 9:41, 10:40 }    #57 = a, 40 = ala-e
    midi_out.note_off(midi_numbers[nykyinen_indeksi], 110)
    midi_out.note_on(midi_numbers[n], 110)
    

def lisataanko_vauhtia(pisteet):
    if pisteet % 15 == 0 and pisteet > 0:  #  0%11 == 0  
        return 20
    return 0

def pelitilan_tekstit(vaarin, pisteet, pallo):
    teksti = fontti_iso.render(f"Pisteet: {pisteet}", True, turkoosi)
    naytto.blit(teksti, (600, 30))

    if vaarin:                          # chr(97) = 'a'
        teksti = fontti_keski.render(f"Väärin. Nuotti on: { str(chr(pallo.nykyinen_keycode())) }", True, punainen)        
        naytto.blit(teksti, (200, 40))    


#############################################################################################################
        
pygame.init()
pygame.display.set_caption("Tunnista nuotin nimi")

pygame.midi.init()
port = pygame.midi.get_default_output_id()
midi_out = pygame.midi.Output(port, 0)
midi_out.set_instrument(33)   # acoustic bass

fontti_iso = pygame.font.SysFont("Arial", 36)
fontti_keski = pygame.font.SysFont("Arial", 30)
fontti_pieni_b = pygame.font.SysFont("Arial", 24, bold = True)
fontti_pieni = pygame.font.SysFont("Arial", 24, bold = False)


def main():
    pisteet = 0
    vaarin = False
    vauhti = 120   # ticks
    pallo = Nuotti(min(alin_ja_ylin), max(alin_ja_ylin))  # koska f-avaimen f on g-avaimen d
    pallo.arvo_nuotti()    
    vari = pallo.arvo_vari()
    nykyinen_indeksi = pallo.arvottu_indeksi
    midi_play(pallo.arvottu_indeksi, nykyinen_indeksi)                                                           
    muunna_nappaimia = {pygame.K_z:"c", pygame.K_x: "d",  pygame.K_c: "e", pygame.K_v: "f", pygame.K_b: "g", 
    pygame.K_n: "a", pygame.K_m: "h", pygame.K_COMMA : "c", pygame.K_PERIOD: "d", 47: "e", pygame.K_RSHIFT: "f",}
                                                                                # TODO: miksei K_MINUS toimi? Keyb. Suomi-asetus ?!?!
         
    while True:
        for tapahtuma in pygame.event.get(): 
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()
            else:                
                if tapahtuma.type == pygame.KEYDOWN:

                    ok1, ok2 = False, False
                    if tapahtuma.key in muunna_nappaimia and nappaimet_vai_koskettimisto == 2:
                        if  muunna_nappaimia[tapahtuma.key] == chr(pallo.nykyinen_keycode()):
                            ok1 = True
                    if nappaimet_vai_koskettimisto == 1 and tapahtuma.key == pallo.nykyinen_keycode():
                        ok2 = True

                    if ok1 or ok2 :
                        pisteet += 1
                        vauhti += lisataanko_vauhtia(pisteet)
                        vaarin = False
                        pallo.arvo_nuotti()                        
                        midi_play(pallo.arvottu_indeksi, nykyinen_indeksi)        # MIDI täällä
                        nykyinen_indeksi = pallo.arvottu_indeksi   
                        vari = pallo.arvo_vari()                      
                    else:
                        pisteet -= 1
                        vaarin = True         
            
        naytto.fill(valkoinen)
        naytto.blit(f_avain, (11, 68))
        
        # anaaliin fisti
        if not pallo.liiku():  
            gameover(pisteet, fontti_iso, fontti_pieni, "hiscore_nuotti_f.txt")
            main()

        pygame.draw.circle(naytto, vari, (pallo.x , pallo.y), PALLON_KOKO)
        nuottiviivasto(WIDTH)        
        if pallo.arvottu_indeksi == 10: # keski-c:lle apuviiva
            pygame.draw.line(naytto, (0, 0, 255), (pallo.x-50, pallo.y), (pallo.x+50, pallo.y), 2)
            
        pelitilan_tekstit(vaarin, pisteet, pallo)        
           
        pygame.display.flip()
        kello.tick(vauhti)
            


alin_ja_ylin = nayta_alue(fontti_keski, fontti_pieni, fontti_pieni_b)
nappaimet_vai_koskettimisto = kysy_nappaimet(fontti_keski, fontti_pieni, fontti_pieni_b)
main()
