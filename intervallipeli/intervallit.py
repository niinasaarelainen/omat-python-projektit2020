import random, pygame.midi, pygame

pygame.init()    
pygame.midi.init()
kello = pygame.time.Clock()
naytto = pygame.display.set_mode((800, 600))
fontti = pygame.font.SysFont("FreeMono", 42)
fontti_pieni = pygame.font.SysFont("FreeMono", 25)
port = pygame.midi.get_default_output_id()
midi_out = pygame.midi.Output(port, 0)

WHITE = (200, 200, 200)
BLUE = (10, 97, 97)
RED = (220, 0, 0)
GREEN = (10, 220, 7)
blockSize = 80
x_aloitus = 100
y_aloitus = 130
ruudukko = []
intervallit = ["s2", "p3", "s3", "pu4", "y4/vä5", "pu5", "p6", "s6", "p7", "s7"]
oikea_vastaus = ""
aani1 = 0
aani2 = 0
midi_numbers = {0:60, 1:61, 2:62, 3:63, 4:64, 5:65, 6:66, 7:67, 8:68, 9:69, 10:70, 11:71 }    #keski-c - h   
oikein = -1  # aluksi ei kumpikaan, 0 = väärin, 1 = oikein


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
            rect = pygame.Rect(x*blockSize*3 + x_aloitus, y*blockSize + y_aloitus, blockSize*3, blockSize)
            pygame.draw.rect(naytto, WHITE, rect, 1)   # 1 = vain reunat = mustaa keskellä
            ind = ruudukko[y][x]
            interv = intervallit[ind -2]
            text = fontti.render(interv, True, BLUE)  
            naytto.blit(text, (x * blockSize * 3 + x_aloitus + 25, y * blockSize + y_aloitus + 18))  

def ruutu_oikein(x_ind, y_ind):
    rect = pygame.Rect(x_ind * blockSize * 3 + x_aloitus +3, y_ind * blockSize + y_aloitus +3 , blockSize * 3 - 6, blockSize - 6)
    pygame.draw.rect(naytto, GREEN, rect, 6)   # 1 = vain reunat = mustaa keskellä

def ruutu_vaarin(x_ind, y_ind):
    rect = pygame.Rect(x_ind * blockSize * 3 + x_aloitus +3, y_ind * blockSize + y_aloitus +3 , blockSize * 3 - 6, blockSize - 6)
    pygame.draw.rect(naytto, RED, rect, 6)   # 1 = vain reunat = mustaa keskellä

def mika_grid_indeksi_x(x):
    indeksi = -1
    for i in range(3):   # käytössä 0 ja 1, 2= yli alueen
        if x > x_aloitus + i * blockSize * 3:
            indeksi = i
    return indeksi

def mika_grid_indeksi_y(y):
    indeksi = -1
    for i in range(6):   # käytössä 0-4, 5= yli alueen
        if y > y_aloitus + i * blockSize:
            indeksi = i
    return indeksi

def midi_play(notes, instrument):
    midi_out.set_instrument(instrument)  
    for note in notes:
        midi_out.note_on(midi_numbers[note], 110)
    pygame.time.delay(700)
    for note in notes:
        midi_out.note_off(midi_numbers[note], 110)


def valitse_aanet():
    global oikea_vastaus, aani1, aani2
    aani1 = random.randint(0, 11)
    aani2 = random.randint(0, 11)
    while aani1 == aani2 or abs(aani2 - aani1) == 1:
        aani2 = random.randint(0, 11)
    erotus = abs(aani2 - aani1) - 2
    oikea_vastaus = erotus + 2


def soita_intervalli():  
    global oikein  
    # peräkkäin
    midi_play([aani1], 2)
    midi_play([aani2], 2) 
    midi_play([aani1, aani2], 2)
   

def ruudun_nollaus(pist, kysytty, x_ind, y_ind):
    naytto.fill((10, 10, 10))  
    teksti = fontti_pieni.render(f"Sama intervalli uudestaan = Space ", True, WHITE)
    naytto.blit(teksti, (100, 40))   
    drawGrid()   
    pisteet = fontti.render(f" {pist}/{kysytty}", True, BLUE)  
    naytto.blit(pisteet, (640, 25))  
    if oikein == 1:
        ruutu_oikein(x_ind, y_ind)
    elif oikein == 0:
        ruutu_vaarin(x_ind, y_ind)
    pygame.display.flip()     


def mainloop():
    global oikein
    kysytty = 0
    pist = 0  
    alusta_ruudukko()  
    drawGrid()     
    pygame.display.flip()      
    valitse_aanet()
    soita_intervalli()  
    x_ind = 0
    y_ind = 0    

    while True:
        ruudun_nollaus(pist, kysytty, x_ind, y_ind)              
        
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
                kysytty += 1   
                x = event.pos[0]
                x_ind = mika_grid_indeksi_x(x)
                y = event.pos[1]   
                y_ind = mika_grid_indeksi_y(y)
                if x_ind in [0,1] and y_ind >= 0 and y_ind <= 4:
                    print(oikea_vastaus, ruudukko[y_ind][x_ind])
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