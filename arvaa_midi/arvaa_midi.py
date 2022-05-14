import pygame, glob, copy, random
from mixer import *


pygame.init()
LEVEYS =  1210
KORKEUS = 700
naytto = pygame.display.set_mode((LEVEYS, KORKEUS))
pygame.display.set_caption("Arvaa MIDI")

mids = []
mids_9kpl = []
for filename in glob.iglob("mids" + '**/*.mid', recursive=True):
    kansio, nimi = filename.split("\\")
    mids.append(nimi)
print(len(mids))
mids_9kpl, mids = valitse_biisi(mids, mids_9kpl)
print(len(mids))


def arvo_9(mids_copy):
    global mids_9kpl 
    for i in range(8):   # on jo oikea vastaus
        r = random.randint(0, len(mids_copy) - 1)
        mids_9kpl.append(mids_copy.pop(r))

def arvaus(time):
    global mids_9kpl 
    naytto.fill(BLACK)    

    mids_copy = copy.deepcopy(mids)    
    arvo_9(mids_copy)  
    print(len(mids_9kpl))  

    i  = 1
    for biisi in mids_9kpl:
        biisi = biisi.split(".")[0]
        textsurface = font_pieni.render(f" {i}) {biisi}", True, (100, 30, 30))           
        naytto.blit(textsurface, (130, i * 40))  
        i += 1  
    pygame.display.flip()  
    while True:
        for tapahtuma in pygame.event.get(): 
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()    
                mixer.music.stop()    

            elif tapahtuma.type == pygame.KEYDOWN:
                nro = tapahtuma.key - 48

        kello.tick(100)

def main():
    global r, g
    time = 0.0
    textsurface = myfont.render(f"{time}", True, (100, 30, 30))  
    mixer.music.play()
    stopped = False


    while True:
        naytto.fill(BLACK)            
       

        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()    
                mixer.music.stop()    

            elif tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_SPACE:
                    print(time)  
                    mixer.music.stop()   
                    stopped = True
          
                    
        textsurface = myfont.render(f" Paina SPACE kun tunnistat kappaleen  {time:.2f} ", True, (100, 30, 30))  
        naytto.blit(textsurface, (30, 20))  
        pygame.display.flip()  
        if not stopped:
            time += 0.01   
        else:
            arvaus(time)     
        kello.tick(100)


def lopetus(teksti):
    textsurface = myfont.render(teksti, True, (100, 30, 30))
    mixer.music.pause()  
    
    while True:
        naytto.fill((255, 255, 255))        
        naytto.blit(textsurface, (20, 100))  

        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()    
                
            elif tapahtuma.type == pygame.KEYDOWN:
                main()

        pygame.display.flip()
        kello.tick(70)



y = KORKEUS - 100
BLACK = (0, 0, 0)
r = 10
g = 200   # värien RGB .muuttujia palkissa

kello = pygame.time.Clock()
pygame.font.init()
font_pieni = pygame.font.SysFont('Comic Sans MS', 30)
myfont = pygame.font.SysFont('Comic Sans MS', 45)


main()