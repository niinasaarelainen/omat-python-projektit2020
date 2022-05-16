from calendar import timegm
import pygame, glob, copy, random
from mixer import *


pygame.init()
LEVEYS =  1010
KORKEUS = 600
naytto = pygame.display.set_mode((LEVEYS, KORKEUS))
pygame.display.set_caption("Arvaa MIDI")

mids = []
mids_9kpl = []
times = []
kierros = 0
oikein  = 0
vaarin = 0

for filename in glob.iglob("mids" + '**/*.mid', recursive=True):
    kansio, nimi = filename.split("\\")
    mids.append(nimi)


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


def arvaus(time):     
    global kierros
    global mids_9kpl 
    naytto.fill(BLACK)    
    kierros += 1
    print(len(mids_9kpl))  

    i  = 1
    random.shuffle(mids_9kpl)
    for biisi in mids_9kpl:
        biisi = biisi.split(".")[0]
        textsurface = font_pieni.render(f" {i}) {biisi}", True, (100, 130, 130))           
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
                if 0 <= nro <= 8:
                    lopetus(mids_9kpl[nro] == oikea_vastaus, time)

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
                    mixer.music.stop()   
                    stopped = True
                elif tapahtuma.key == pygame.K_RETURN:
                    mixer.music.stop()   
                    stopped = True
                    lopetus(None, time)   # oikeinko, time
          
                    
        textsurface = myfont.render(f" Paina SPACE kun tunnistat kappaleen ", True, (100, 230, 230))  
        naytto.blit(textsurface, (30, 20))  
        textsurface = myfont.render(f"   {time:.1f} ", True, (100, 130, 130))  
        naytto.blit(textsurface, (LEVEYS - 130, 20)) 
        textsurface = font_pieni.render(f" RETURN = lopetan", True, (100, 30, 30))           
        naytto.blit(textsurface, (130, 340)) 

        pygame.display.flip()  
        if not stopped:
            time += 0.01   
        else:
            arvaus(time)     
        kello.tick(100)


def lopetus(oikeinko, time):
    global oikein, vaarin

    if oikeinko :
        textsurface = myfont.render("Oikein !!", True, (20, 230, 30))
        oikein += 1
        times.append(time)
    elif oikeinko == False:
        textsurface = myfont.render("Väärin !!", True, (200, 30, 30))
        vaarin += 1
    
    while True:
        naytto.fill((255, 255, 255))       
        if oikeinko != None: 
            naytto.blit(textsurface, (120, 100)) 
            uusi = myfont.render("Any key = seuraava biisi", True, (120, 130, 130))
            naytto.blit(uusi, (120, 300)) 

        if len(mids) == 8 or oikeinko == None:
            if len(times) > 0:
                keski = sum(times) / len(times)
                
            naytto.fill((255, 255, 255))      
            lop = myfont.render("Kyselty tarpeeksi ! Lopetetaan.", True, (200, 30, 30))
            naytto.blit(lop, (20, 120)) 
            if oikein > 0:
                lop2 = myfont.render(f"Oikein {oikein} kpl  keskimäärin ajassa {keski:.2f}", True, (20, 230, 30))
                naytto.blit(lop2, (60, 240)) 
            lop2 = myfont.render(f"Väärin {vaarin} kpl", True, (220, 30, 30))
            naytto.blit(lop2, (60, 310)) 
            uusi = myfont.render("Any key = uusi peli", True, (120, 230, 130))
            naytto.blit(uusi, (120, 440)) 

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