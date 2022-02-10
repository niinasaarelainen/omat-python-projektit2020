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
    obsticles.append(Obsticle(30, 30, 200,40))
    obsticles.append(Obsticle(220, 110, 100, 180))
    obsticles.append(Obsticle(320, 310, 100, 80))

def draw_obsticles():
    for obst in obsticles:
        pygame.draw.line(naytto, turkoosi, (obst.x_aloitus ,obst.y_aloitus ),(obst.x_lopetus,obst.y_lopetus ), 9)

def osuuko_esteeseen(nuotti):
    for obst in obsticles:
        if nuotti.y >= obst.y_aloitus and nuotti.x >= obst.x_aloitus and nuotti.x <= obst.x_lopetus and nuotti.y <= obst.y_lopetus:
            if nuotti.y == nuotti.x:
                return 1
    return 0

def osuuko_turkoosiin(nuotti):
    for obst in obsticles:
        if nuotti.y >= obst.y_aloitus and nuotti.x >= obst.x_aloitus and nuotti.x <= obst.x_lopetus and nuotti.y <= obst.y_lopetus:
            vari = naytto.get_at((nuotti.x, nuotti.y))[:3]
            if vari != valkoinen:
                for x in range(1, 2):
                    for y in range(0, 2):
                        if naytto.get_at((nuotti.x + x, nuotti.y + y))[:3] == turkoosi:
                            return x, y 
    return 0, 1 

def arvo_nuotti():
    nuotti = Nuotti()
    nuotti.arvo_nuotti()   
    midi_out.note_on(nuotti.arvottu_indeksi + 81, 50)        
    nuotit.append(nuotti)

def liikuta_nuotit():
    for nuotti in nuotit: 
        x, y = osuuko_turkoosiin(nuotti)         
        nuotti.x += x
        nuotti.y += y  
        #nuotti.x += osuuko_esteeseen(nuotti) 
        vari = nuotti.arvo_vari()   
        pygame.draw.ellipse(naytto, vari, [nuotti.x, nuotti.y , KOKO, KOKO*2], 6)
    for nuotti in nuotit:  
        if nuotti.y >= HEIGHT:
            nuotit.remove(nuotti)
        


def main():
    vauhti = 29   # ticks  
    i = 0
         

    while True:
        naytto.fill(valkoinen)        

        for tapahtuma in pygame.event.get(): 
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()
    
        draw_obsticles()
        pygame.display.flip()
        if i % 10 == 0:
            arvo_nuotti() 
        i += 1
        liikuta_nuotit()

        pygame.display.flip()
        kello.tick(vauhti)
            

luo_obsticlet()
main()