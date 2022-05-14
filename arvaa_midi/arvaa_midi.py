import pygame, glob, copy, random
from mixer import *


pygame.init()
LEVEYS =  1010
KORKEUS = 600
naytto = pygame.display.set_mode((LEVEYS, KORKEUS))
pygame.display.set_caption("Arvaa MIDI")

mids = []
mids_9kpl = []
kierros = 0

for filename in glob.iglob("mids" + '**/*.mid', recursive=True):
    kansio, nimi = filename.split("\\")
    mids.append(nimi)
    kierroksia_max = len(mids) - 9


def arvo_9():
    global oikea_vastaus, mids_9kpl, mids  

    print(len(mids))
    oikea_vastaus, mids_9kpl, mids = valitse_biisi(mids, mids_9kpl)
    mids_copy = copy.deepcopy(mids)      
    print(len(mids), len(mids_9kpl))
    print(oikea_vastaus)

    for i in range(8):   # on jo oikea vastaus
        r = random.randint(0, len(mids_copy) - 1)
        mids_9kpl.append(mids_copy.pop(r))


def arvaus(time):     # TODO  ajat muistiin ?
    global kierros
    global mids_9kpl 
    naytto.fill(BLACK)    
    kierros += 1
    print(len(mids_9kpl))  

    i  = 1
    random.shuffle(mids_9kpl)
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
                nro = tapahtuma.key - 49
                lopetus(mids_9kpl[nro] == oikea_vastaus)

        kello.tick(100)


def main():
    global mids_9kpl, mids
    global r, g
    time = 0.0
    textsurface = myfont.render(f"{time}", True, (100, 30, 30))      
    stopped = False
    mids_9kpl = []       
    arvo_9() 
    
    mixer.music.play()


    while True :
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
          
                    
        textsurface = myfont.render(f" Paina SPACE kun tunnistat kappaleen   {time:.2f} ", True, (100, 30, 30))  
        naytto.blit(textsurface, (30, 20))  
        pygame.display.flip()  
        if not stopped:
            time += 0.01   
        else:
            arvaus(time)     
        kello.tick(100)


def lopetus(oikeinko):

    if oikeinko:
        textsurface = myfont.render("Oikein !!", True, (200, 30, 30))
    else:
        textsurface = myfont.render("Väärin !!", True, (200, 30, 30))
    
    while True:
        naytto.fill((255, 255, 255))        
        naytto.blit(textsurface, (20, 100)) 
        uusi = myfont.render("Any key = uusi peli", True, (200, 30, 30))
        naytto.blit(uusi, (20, 300)) 

        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()    
                
            elif tapahtuma.type == pygame.KEYDOWN:
                if kierros < kierroksia_max:
                    main()
                else:
                    naytto.fill((255, 255, 255))      
                    lop = myfont.render("Kyselty tarpeeksi ! Lopetetaan.", True, (200, 30, 30))
                    naytto.blit(lop, (20, 300)) 


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