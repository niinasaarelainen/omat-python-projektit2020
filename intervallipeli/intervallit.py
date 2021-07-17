import random, pygame.midi, pygame

pygame.init()    
pygame.midi.init()
kello = pygame.time.Clock()
naytto = pygame.display.set_mode((900, 600))
fontti = pygame.font.SysFont("FreeMono", 42)
fontti_pieni = pygame.font.SysFont("FreeMono", 25)
fontti_medium = pygame.font.SysFont("FreeMono", 33)
port = pygame.midi.get_default_output_id()
midi_out = pygame.midi.Output(port, 0)
arrows = pygame.image.load('arrows.png')

ARROW_X = 630
ARROW_Y = 280
X_ALOITUS = 100
Y_ALOITUS = 100
WHITE = (250, 250, 250)
BLUE = (10, 97, 97)
RED = (220, 0, 0)
GREEN = (10, 220, 7)
BLOCKSIZE = 80

ruudukko = []
intervallit = ["s2", "p3", "s3", "pu4", "y4/vä5", "pu5", "p6", "s6", "p7", "s7"]
oikea_vastaus = 0
aani1 = 0
aani2 = 0
midi_numbers = {0:60, 1:61, 2:62, 3:63, 4:64, 5:65, 6:66, 7:67, 8:68, 9:69, 10:70, 11:71, 12:72 }    #keski-c - h   
oikein = -1  # aluksi ei kumpikaan, 0 = väärin, 1 = oikein
soundi = 105


def alusta_ruudukko():
    oikea_intervalli = 2  # pienin ero tässä pelissä s2 = 1 puolisävelaskel
    for rivi in range(5):
        ruudukko.append([])
        for sarake in range(2):
            ruudukko[rivi].append(oikea_intervalli) 
            oikea_intervalli += 1


def drawGrid():  
    for x in range(2):
        for y in range(5):                 
            rect = pygame.Rect(x*BLOCKSIZE*3 + X_ALOITUS, y*BLOCKSIZE + Y_ALOITUS, BLOCKSIZE*3, BLOCKSIZE)
            pygame.draw.rect(naytto, BLUE, rect, 1)   # 1 = vain reunat = mustaa keskellä
            ind = ruudukko[y][x]
            interv = intervallit[ind -2]
            text = fontti.render(interv, True, BLUE)  
            naytto.blit(text, (x * BLOCKSIZE * 3 + X_ALOITUS + 25, y * BLOCKSIZE + Y_ALOITUS + 18))  

def ruutu_oikein(x_ind, y_ind):
    rect = pygame.Rect(x_ind * BLOCKSIZE * 3 + X_ALOITUS +3, y_ind * BLOCKSIZE + Y_ALOITUS +3 , BLOCKSIZE * 3 - 6, BLOCKSIZE - 6)
    pygame.draw.rect(naytto, GREEN, rect, 6)   # 1 = vain reunat = mustaa keskellä

def ruutu_vaarin(x_ind, y_ind):
    rect = pygame.Rect(x_ind * BLOCKSIZE * 3 + X_ALOITUS +3, y_ind * BLOCKSIZE + Y_ALOITUS +3 , BLOCKSIZE * 3 - 6, BLOCKSIZE - 6)
    pygame.draw.rect(naytto, RED, rect, 6)   # 1 = vain reunat = mustaa keskellä

def mika_grid_indeksi_x(x):
    indeksi = -1
    for i in range(3):   # käytössä 0 ja 1, 2= yli alueen
        if x > X_ALOITUS + i * BLOCKSIZE * 3:
            indeksi = i
    return indeksi

def mika_grid_indeksi_y(y):
    indeksi = -1
    for i in range(6):   # käytössä 0-4, 5= yli alueen
        if y > Y_ALOITUS + i * BLOCKSIZE:
            indeksi = i
    return indeksi

def midi_play(notes, instrument, ms):
    midi_out.set_instrument(instrument)  
    for note in notes:
        midi_out.note_on(midi_numbers[note], 120)
    pygame.time.delay(ms)
    for note in notes:
        midi_out.note_off(midi_numbers[note], 110)


def valitse_aanet():
    global oikea_vastaus, aani1, aani2
    aani1_w = aani1
    aani2_w = aani2
    aani1 = random.randint(0, 1)  # jos molemmat voi olla mikä ääni vain, tulee liikaa pieniä intervalleja
    aani2 = random.randint(2, 12)
    while abs(aani2 - aani1) == 1 or abs(aani2 - aani1) == 12: # vaihtoehdoissa ei ole p2 eikä okt
        aani2 = random.randint(2, 12)
    if aani1_w == aani1 and aani2_w == aani2:
        print("UUSINTA")
        valitse_aanet()
    oikea_vastaus = abs(aani2 - aani1)


def soita_intervalli():  
    # peräkkäin
    midi_play([aani1], soundi, 500)  # notes, instrument, ms
    midi_play([aani2], soundi, 500) 
    # yhtaikaa
    midi_play([aani1, aani2], soundi, 1300)
   

def ruudun_nollaus(pist, kysytty, x_ind, y_ind):
    naytto.fill(WHITE)      
    naytto.blit(arrows, (ARROW_X , ARROW_Y))
    teksti = fontti_pieni.render(f"= Vaihda soundia ", True, BLUE)
    naytto.blit(teksti, (ARROW_X, 355))   
    teksti = fontti_medium.render(f"Space =  ", True, BLUE)
    naytto.blit(teksti, (ARROW_X -3 , 410))   
    teksti = fontti_pieni.render(f"= Sama uudestaan ", True, BLUE)
    naytto.blit(teksti, (ARROW_X, 450))  
    drawGrid()   
    pisteet = fontti.render(f" {pist}/{kysytty}", True, BLUE)  
    naytto.blit(pisteet, (680, 50))  
    if oikein == 1:
        ruutu_oikein(x_ind, y_ind)
    elif oikein == 0:
        ruutu_vaarin(x_ind, y_ind)
    pygame.display.flip()     


def vaihda_soundia(suunta):
    global soundi
    soundi = soundi + suunta
    if soundi == 128:
        soundi = 0
    if soundi == -1:
        soundi = 127    
    midi_play([0], soundi, 500) 


def mainloop():
    global oikein
    kysytty = 0
    pist = 0  
    naytto.fill(WHITE)  
    alusta_ruudukko()  
    drawGrid()     
    pygame.display.flip()      
    valitse_aanet()
    soita_intervalli()  
    x_ind = 0
    y_ind = 0  
    ruudun_nollaus(pist, kysytty, x_ind, y_ind)              

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    soita_intervalli()  
                    break

            if event.type == pygame.MOUSEBUTTONDOWN:                 
                x = event.pos[0]
                x_ind = mika_grid_indeksi_x(x)
                y = event.pos[1]   
                y_ind = mika_grid_indeksi_y(y)

                # nuolet:
                if x >= ARROW_X and x <= ARROW_X + 35 and y >= ARROW_Y and y <= ARROW_Y + 35:
                    vaihda_soundia(1)
                    break
                if x >= ARROW_X + 30 and x <= ARROW_X + 70 and y >= ARROW_Y + 25 and y <= ARROW_Y + 60:
                    vaihda_soundia(-1)
                    break

                #intervallit:
                if x_ind in [0,1] and y_ind >= 0 and y_ind <= 4:  
                    kysytty += 1                    
                    if oikea_vastaus == ruudukko[y_ind][x_ind]:
                        oikein = 1  
                        pist += 1                                       
                        valitse_aanet()                          
                    else:
                        oikein = 0                                   
                    ruudun_nollaus(pist, kysytty, x_ind, y_ind)  
                    soita_intervalli()    
                
        
        kello.tick(40)


mainloop()