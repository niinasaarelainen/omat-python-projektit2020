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
blockSize = 80
x_aloitus = 170
y_aloitus = 120
ruudukko = []
intervallit = ["s2", "p3", "s3", "pu4", "y4/vä5", "pu5", "p6", "s6", "p7", "s7"]


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
            naytto.blit(text, (x*blockSize*3 + x_aloitus + 25, y*blockSize + y_aloitus + 18))  

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
    midi_numbers = {0:60, 1:61, 2:62, 3:63, 4:64, 5:65, 6:66, 7:67, 8:68, 9:69, 10:70, 11:71 }    #keski-c - h   
    for note in notes:
        midi_out.note_on(midi_numbers[note], 110)
    pygame.time.delay(900)
    for note in notes:
        midi_out.note_off(midi_numbers[note], 110)


def soita_intervalli():
    aani1 = random.randint(0, 11)
    aani2 = random.randint(0, 11)
    while aani1 == aani2:
        aani2 = random.randint(0, 11)
    # peräkkäin
    midi_play([aani1], 2)
    midi_play([aani2], 2)    
    # yhtaikaa
    midi_play([aani1, aani2], 2)
    
   

def mainloop():
    kysytty = 0
    virheet = 0  
    alusta_ruudukko()
    print(ruudukko) 

    while True:
        naytto.fill((10, 10, 10))  
        drawGrid() 
        oikein = kysytty - virheet      
        pisteet = fontti.render(f" {oikein}/{kysytty}", True, BLUE)  
        naytto.blit(pisteet, (640, 25))  
        pygame.display.flip()

        pygame.time.delay(700)
        soita_intervalli()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN: 
                x = event.pos[0]
                x_ind = mika_grid_indeksi_x(x)
                y = event.pos[1]   
                y_ind = mika_grid_indeksi_y(y)
                print(x_ind, y_ind)
                """
                if not melodia[monesko_kayttajan_aani] == chr(event.key):
                    virheet += 1
                    print("virheitä:",  virheet)
                """
                kysytty += 1   
        
        kello.tick(40)

mainloop()