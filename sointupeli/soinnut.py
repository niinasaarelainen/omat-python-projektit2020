import random, pygame.midi, pygame

pygame.init()    
pygame.midi.init()
kello = pygame.time.Clock()
naytto = pygame.display.set_mode((800, 560))
fontti = pygame.font.SysFont("FreeMono", 42)
fontti_pieni = pygame.font.SysFont("FreeMono", 25)
port = pygame.midi.get_default_output_id()
midi_out = pygame.midi.Output(port, 0)

WHITE = (200, 200, 200)
BLUE = (10, 97, 97)
RED = (220, 0, 0)
GREEN = (10, 220, 7)
blockSize = 90
x_aloitus = 100
y_aloitus = 130
ruudukko = []
soinnut = ["D7", "m7", "DMaj7", "mMaj7", "D7(b5)", "D7(#5)", "puolidimi", "dimi"]
sointuvaihtoehdot = [[0, 4, 7, 10], [0, 3, 7, 10], [0, 4, 7, 11], [0, 3, 7, 11], [0, 4, 6, 10], [0, 4, 8, 10], [0, 3, 6, 10],  [0, 3, 6, 9]]
oikea_vastaus = ""
oikea_sointu = []
midi_numbers = {0:60, 1:61, 2:62, 3:63, 4:64, 5:65, 6:66, 7:67, 8:68, 9:69, 10:70, 11:71, 12:72 }    #keski-c - h   
oikein = -1  # aluksi ei kumpikaan, 0 = väärin, 1 = oikein
riveja = 4
pno = 0


def alusta_ruudukko():
    oikea_sointu = 0  
    for rivi in range(riveja):
        ruudukko.append([])
        for sarake in range(2):
            ruudukko[rivi].append(oikea_sointu) 
            oikea_sointu += 1


def drawGrid():  
    for x in range(2):
        for y in range(riveja):                 
            rect = pygame.Rect(x*blockSize*3 + x_aloitus, y*blockSize + y_aloitus, blockSize*3, blockSize)
            pygame.draw.rect(naytto, WHITE, rect, 1)   # 1 = vain reunat = mustaa keskellä
            ind = ruudukko[y][x]
            sointu = soinnut[ind]
            text = fontti.render(sointu, True, BLUE)  
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

def midi_play(notes, instrument, ms):
    midi_out.set_instrument(instrument)  
    for note in notes:
        midi_out.note_on(midi_numbers[note], 120)
    pygame.time.delay(ms)
    for note in notes:
        midi_out.note_off(midi_numbers[note], 110)

def midi_arpeggio(notes, instrument, ms):
    midi_out.set_instrument(instrument)  
    for note in notes:
        midi_out.note_on(midi_numbers[note], 120)
        pygame.time.delay(ms)
    pygame.time.delay(ms*2)
    for note in notes:
        midi_out.note_off(midi_numbers[note], 110)


def valitse_aanet():
    global oikea_sointu, oikea_vastaus
    r = random.randint(0, len(sointuvaihtoehdot)-1)  # jos molemmat voi olla mikä ääni vain, tulee liikaa pieniä intervalleja
    oikea_sointu = sointuvaihtoehdot[r]
    oikea_vastaus = r


def soita_sointu(): 
    midi_play(oikea_sointu, pno, 1500)  # notes, instrument, ms

def soita_murrettuna(): 
    midi_arpeggio(oikea_sointu, pno, 500)  # notes, instrument, ms
   

def ruudun_nollaus(pist, kysytty, x_ind, y_ind):
    naytto.fill((10, 10, 10))  
    teksti = fontti_pieni.render(f"Sama sointu uudestaan = Space ", True, WHITE)
    naytto.blit(teksti, (100, 35))  
    teksti = fontti_pieni.render(f"Sama murrettuna = M ", True, WHITE)
    naytto.blit(teksti, (100, 58))    
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
    soita_sointu()  
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
                    soita_sointu()  
                    break
                if event.key == pygame.K_m:
                    soita_murrettuna()  
                    break

            if event.type == pygame.MOUSEBUTTONDOWN:                 
                x = event.pos[0]
                x_ind = mika_grid_indeksi_x(x)
                y = event.pos[1]   
                y_ind = mika_grid_indeksi_y(y)
                if x_ind in [0,1] and y_ind >= 0 and y_ind < riveja:
                    kysytty += 1   
                    if oikea_vastaus == ruudukko[y_ind][x_ind]:
                        oikein = 1  
                        pist += 1                                       
                        valitse_aanet()  
                    else:
                        oikein = 0
                                  
                ruudun_nollaus(pist, kysytty, x_ind, y_ind)  
                soita_sointu()  
        
        kello.tick(40)


mainloop()