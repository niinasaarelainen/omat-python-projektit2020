import pygame, pygame.midi, random
from alkukyselyt import *
from yhteiset import *
from nuotti import Nuotti
from gameover import *

class Nuottipeli:

    def arvo_vari(self):
        r = random.randint(0, 200)   #ei yli 200, jottei tule valkoista/liian vaaleaa
        g = random.randint(0, 200)
        b = random.randint(0, 200)
        return r, g, b
        

    def midi_play(self, n, nykyinen_indeksi):
        #ei voi laskea systeemillä, esim. i+=2, koska välillä on puolisävelaskel välillä koko-
        midi_numbers = {0:77, 1:76, 2:74, 3:72, 4:71, 5:69, 6:67, 7:65, 8:64, 9:62, 10:60 }    #60 = keski-c, 77 = ylä-f
        midi_out.note_off(midi_numbers[nykyinen_indeksi], 110)
        midi_out.note_on(midi_numbers[n], 110)
        

    def lisataanko_vauhtia(self, pisteet):
        if pisteet % 15 == 0 and pisteet > 0:  #  0%11 == 0  
            return 20
        return 0

    def pelitilan_tekstit(self, vaarin, pisteet, pallo):
        teksti = fontti_iso.render(f"Pisteet: {pisteet}", True, turkoosi)
        naytto.blit(teksti, (600, 30))

        if vaarin:                          # chr(97) = 'a'
            teksti = fontti_keski.render(f"Väärin. Nuotti on: { str(chr(pallo.nykyinen_keycode())) }", True, punainen)        
            naytto.blit(teksti, (200, 40))    


    #############################################################################################################
            
    def main(self):
        pisteet = 0
        vaarin = False
        vauhti = 120   # ticks
        pallo = Nuotti(min(alin_ja_ylin), max(alin_ja_ylin))
        pallo.arvo_nuotti()    
        nykyinen_indeksi = pallo.arvottu_indeksi
        self.midi_play(pallo.arvottu_indeksi, nykyinen_indeksi) 
        vari = self.arvo_vari()                                                                                              
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
                            vauhti += self.lisataanko_vauhtia(pisteet)
                            vaarin = False
                            pallo.arvo_nuotti()                        
                            self.midi_play(pallo.arvottu_indeksi, nykyinen_indeksi)        # MIDI täällä
                            nykyinen_indeksi = pallo.arvottu_indeksi 
                            vari = self.arvo_vari()
                        else:
                            pisteet -= 1
                            vaarin = True         
                
            naytto.fill(valkoinen)
            naytto.blit(g_avain, (11, 28))
            
            # anaaliin fisti
            if not pallo.liiku():  
                gameover(pisteet, fontti_iso, fontti_pieni)

            pygame.draw.circle(naytto, vari, (pallo.x , pallo.y), PALLON_KOKO)
            nuottiviivasto(WIDTH)        
            if pallo.arvottu_indeksi == 10: # keski-c:lle apuviiva
                pygame.draw.line(naytto, (0, 0, 255), (pallo.x-50, pallo.y), (pallo.x+50, pallo.y), 2)
                
            self.pelitilan_tekstit(vaarin, pisteet, pallo)        
            
            pygame.display.flip()
            kello.tick(vauhti)            

pygame.init()
pygame.display.set_caption("Tunnista nuotin nimi")

pygame.midi.init()
port = pygame.midi.get_default_output_id()
midi_out = pygame.midi.Output(port, 0)
midi_out.set_instrument(10)   # GM 10 = Glockenspiel

fontti_iso = pygame.font.SysFont("Arial", 36)
fontti_keski = pygame.font.SysFont("Arial", 30)
fontti_pieni_b = pygame.font.SysFont("Arial", 24, bold = True)
fontti_pieni = pygame.font.SysFont("Arial", 24, bold = False)

alin_ja_ylin = nayta_alue(fontti_keski, fontti_pieni, fontti_pieni_b)
nappaimet_vai_koskettimisto = kysy_nappaimet(fontti_keski, fontti_pieni, fontti_pieni_b)
nuottipeli = Nuottipeli()
nuottipeli.main()
