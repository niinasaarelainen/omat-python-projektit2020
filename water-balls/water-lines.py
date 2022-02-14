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

def luo_obsticlet():
    
    obsticles.append(Obsticle(30, 30, 200, 10))
    obsticles.append(Obsticle(330, 40, 120, 80))
    obsticles.append(Obsticle(330, 130, -100, 110))
    obsticles.append(Obsticle(220, 300, 400, 80)) 
    obsticles.append(Obsticle(550, 130, -120, 120))  # PROBLEM, jos sama lopetus x/y kuin toisella esteellä
    obsticles.append(Obsticle(230, 230, -100, 110))  
    

def draw_obsticles():
    for obst in obsticles:
        pygame.draw.line(naytto, turkoosi, (obst.x_aloitus ,obst.y_aloitus ),(obst.x_lopetus,obst.y_lopetus ), 1)

def osuuko_esteeseen(nuotti):
    for obst in obsticles:
        if nuotti.y >= obst.y_aloitus and nuotti.x >= obst.x_aloitus and nuotti.x <= obst.x_lopetus and nuotti.y <= obst.y_lopetus:
            if nuotti.y == nuotti.x:
                return 1
    return 0

def osuuko_turkoosiin(nuotti):
    palautus_x = 0
    palautus_y = 1
    for obst in obsticles:
        if nuotti.x in [obst.x_aloitus, obst.x_lopetus] and nuotti.y in [obst.y_aloitus, obst.y_lopetus]:
            return palautus_x, palautus_y
    try:
        vari = naytto.get_at((nuotti.x, nuotti.y))[:3]
        if vari == turkoosi:      # huom! voi verrata turkoosiin jos pisarat piirtää kaikki vasta lopuksi
                                  # muutenhan ruudulla olisi myös sinistä
            for x in range(-1, 2):  
                for y in range(0, 2):  # oli (1, -1, -1) --> 0 1 0 1...            
                    if x != 0 :
                        if naytto.get_at((nuotti.x + x, nuotti.y + y))[:3] == turkoosi:
                            palautus_x = x
                            palautus_y = y
    except:
        print(nuotti.x, nuotti.y)
    
                    
    return palautus_x, palautus_y

def arvo_nuotti():
    nuotti = Nuotti()
    nuotti.arvo_nuotti()   
    midi_out.note_on(nuotti.arvottu_indeksi + 81, 50)        
    nuotit.append(nuotti)

def liikuta_nuotit():
    for nuotti in nuotit: 
        x, y = osuuko_turkoosiin(nuotti)   
        print(x, y)
        nuotti.x += x
        nuotti.y += y  
        
    for nuotti in nuotit:  
        if nuotti.y >= HEIGHT - 1 or nuotti.x >= WIDTH - 1:
            nuotit.remove(nuotti)
    
    
        


def main():
    vauhti = 69   # ticks  
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
            pygame.draw.ellipse(naytto, vari, [nuotti.x, nuotti.y , KOKO, KOKO*2], 6)

        pygame.display.flip()
        kello.tick(vauhti)
            

luo_obsticlet()
main()