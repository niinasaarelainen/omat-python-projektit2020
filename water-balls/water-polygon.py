import pygame, pygame.midi, random
from nuotti_obs import *
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

nuotit = []
obsticles = []


def draw_obsticles():
    points = [(100, 150), (200, 110), (260, 140), (210, 250)]
    pygame.draw.polygon(naytto, turkoosi, points, 1)
    points = [(270, 250), (300, 120), (390, 340), (310, 350)]
    pygame.draw.polygon(naytto, turkoosi, points, 1)
    points = [(400, 150), (480, 130), (560, 12), (510, 250)]   
    pygame.draw.polygon(naytto, turkoosi, points, 1)



def osuuko_turkoosiin(nuotti):
    turkoosit = []
    try:
        vari = naytto.get_at((nuotti.x, nuotti.y))[:3]
        if vari == turkoosi:      # huom! voi verrata turkoosiin jos pisarat piirtää kaikki vasta lopuksi
                                  # muutenhan ruudulla olisi myös sinistä
            for x in range(-1, 2):  
                for y in range(0,2):  # oli  --> 0 1 0 1...  
                    if naytto.get_at((nuotti.x + x, nuotti.y + y))[:3] == turkoosi:
                        turkoosit.append([x, y])
    except:
        print(nuotti.x, nuotti.y)
    
    if len(turkoosit) > 1:
        s = sorted(turkoosit, key=lambda x: (x[1], abs(x[0])), reverse=True)  
        if nuotti.x + s[0][0] == nuotti.x_w and nuotti.y + s[0][1] == nuotti.y_w:
            print(s[1])
            if s[1] != [0,0]:
                return s[1][0], s[1][1]
            return 0,1
        return s[0][0], s[0][1]
    else:
        return 0,1

def arvo_nuotti():
    nuotti = Nuotti()
    nuotti.arvo_nuotti()   
    midi_out.note_on(nuotti.arvottu_indeksi + 81, 50)        
    nuotit.append(nuotti)

def liikuta_nuotit():
    for nuotti in nuotit: 
        x, y = osuuko_turkoosiin(nuotti) 
        # älä jankkaa 2 paikkaa edestakaisin vaan mene alas
        if nuotti.x + x == nuotti.x_w  and nuotti.y + y == nuotti.y_w :
            nuotti.y += 1  
        else:
            nuotti.x_w = nuotti.x
            nuotti.x += x
            nuotti.y_w = nuotti.y
            nuotti.y += y  
        
    for nuotti in nuotit:  
        if nuotti.y >= HEIGHT - 1 or nuotti.x >= WIDTH - 1:
            nuotit.remove(nuotti)
    
    
        


def main():
    vauhti = 89   # ticks  
    i = 0

    while True:
        naytto.fill(valkoinen)        

        for tapahtuma in pygame.event.get(): 
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()
    
        draw_obsticles()
        if i % 7 == 0:
            arvo_nuotti() 
        i += 1
        liikuta_nuotit()
        for nuotti in nuotit:
            vari = nuotti.arvo_vari()   
            pygame.draw.ellipse(naytto, vari, [nuotti.x, nuotti.y , KOKO, KOKO*2], 4)

        pygame.display.flip()
        kello.tick(vauhti)
            

main()