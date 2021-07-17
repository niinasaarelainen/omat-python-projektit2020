import random, pygame.midi, pygame

pygame.init()    
pygame.midi.init()
kello = pygame.time.Clock()

raitoja = 8
assert raitoja > 0, "Vähintään yksi raita"
assert raitoja <= 10, "Ruudulle ei mahdu kuin kymmenen raitaa"
WIDTH = 1170
HEIGHT = raitoja * 81 + 100
naytto = pygame.display.set_mode((WIDTH, HEIGHT))
fontti = pygame.font.SysFont("FreeMono", 42)
fontti_pieni = pygame.font.SysFont("FreeMono", 24)

port = pygame.midi.get_default_output_id()
midi_out = pygame.midi.Output(port, 0)
midi_numbers = {"z":60, "x":62, "c":64, "v":65, "b":67, "n":69, "m":71 ,",":72, ".":74, "/":76}    #60 = keski-c, 76 = e2
midi_instruments = {1:2, 2:22, 3:33, 4:74, 5:88, 6:44, 7:99, 8:127, 9:101, 10:66}

WHITE = (200, 200, 200)
BLUE = (10, 97, 97)
BLACK = (10, 10, 10)
WHITE = (250, 250, 250)
RED = (251, 0, 0)

soittoalue = "zxcvbnm,.-"
rec_enabled = [1]
muted = []
raidat = []
play_or_pause = True
rec_or_pause = True
aanitys = []
kursori = 0
START_SEQ = 250 
END_SEQ = 1100
RAIDAN_KORKEUS = 70
EKA_RAITA_Y = 40

play = pygame.image.load('play.png')
play = pygame.transform.scale(play, (68, 68))

pause = pygame.image.load('pause.jpg')
pause = pygame.transform.scale(pause, (67, 67))

pause_red = pygame.image.load('pause_red.jpg')
pause_red = pygame.transform.scale(pause_red, (67, 67))

rec = pygame.image.load('rec.jpg')
rec = pygame.transform.scale(rec, (90, 90))

mute  = pygame.image.load('mute.png')
mute = pygame.transform.scale(mute, (40, 40))

unmute  = pygame.image.load('unmute.png')
unmute = pygame.transform.scale(unmute, (40, 40))


def alusta_raidat():
    for raita in range(raitoja):
        raidat.append([])


def kuvat_nakyviin(vari):    
    for i in range(1, raitoja + 1):
        teksti = fontti_pieni.render(f"{i}", True, BLACK)
        naytto.blit(teksti, (EKA_RAITA_Y, i * RAIDAN_KORKEUS))
        naytto.blit(rec, (80, i*70 - 30))
        if i in muted:
            naytto.blit(mute, (190, i * RAIDAN_KORKEUS ))
        else:
            naytto.blit(unmute, (190, i * RAIDAN_KORKEUS ))  

    for raita in rec_enabled:
        pygame.draw.circle(naytto, vari, (107, raita*70 + 14), 11)     # parametri vari tänne

    # PLAY / PAUSE:
    if play_or_pause:
        naytto.blit(play, (WIDTH - 188, HEIGHT - 78))
    else:
        naytto.blit(pause, (WIDTH - 188, HEIGHT - 78))
    # REC / PAUSE:
    if rec_or_pause:
        pygame.draw.circle(naytto, RED, (WIDTH - 66, HEIGHT - 44), 33)  
    else:
        naytto.blit(pause_red, (WIDTH - 100, HEIGHT - 78))   
    


def soita_raita(aanitys): 
    global kursori, play_or_pause 
    laskuri = 0   
    for i in range(len(aanitys)):
        while play_or_pause:
            pygame.time.delay(500) 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    check_mouse_action(x, y, RED) 
         
        kirjain, down, ms, raita = aanitys[i]
        while laskuri != ms:   
            laskuri += 1
            kursori += 1
            kello.tick(100) 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    check_mouse_action(x, y, RED) 
                        
        if down:
            #print(ms)
            midi_out.set_instrument(midi_instruments[raita])
            midi_out.note_on(midi_numbers[kirjain], 110) 
        else:
            midi_out.note_off(midi_numbers[kirjain], 110)
    kursori = 0
    play_or_pause = not play_or_pause
        

def soita_kaikki_raidat():
    soivat_raidat = [raidat[i] for i in range(len(raidat)) if (i + 1) not in muted ]
    flat_list = [item for sublist in soivat_raidat for item in sublist]
    s = sorted(flat_list, key = lambda x: x[2])   # kolmas parametri = ms
    soita_raita(s)


def aanita(kirjain, down, ms):    # down = True, up = False
    global aanitys
    print("aanita:", kirjain)
    aanitys.append((kirjain, down, ms))
       

def tallenna():
    global aanitys    
    ms_offset = aanitys[0][2]
    aanitys = [(aani[0], aani[1], aani[2] - ms_offset) for aani in aanitys]
    for raita_nro in rec_enabled:
        aanitys = [(aani[0], aani[1], aani[2], raita_nro) for aani in aanitys] # lisätään raita
        raidat[raita_nro - 1] = aanitys        
        piirra_sekvenssi(aanitys)
        

def piirra_sekvenssi(aanitys): #kirjain, down, ms, raita_nro
    soittoalue = "zxcvbnm,./"   # - vaihdettu /
    key_down = [aani for aani in aanitys if aani[1] == True]
    key_up = [aani for aani in aanitys if aani[1] == False]
    #print(key_down, key_up)
    for aani_down in key_down:
        kirjain_down, down, ms_down, raita_nro = aani_down
        monesko = soittoalue.index(kirjain_down)  
        y = raita_nro * RAIDAN_KORKEUS + EKA_RAITA_Y - monesko * 5
        for aani_up in key_up:
            kirjain_up, down, ms_up, raita_nro = aani_up
            if kirjain_down == kirjain_up:
                #print("kirjain_up", kirjain_up, "ms", ms_up)
                pygame.draw.line(naytto, BLACK, (ms_down // 7 + START_SEQ, y), (ms_up // 7 + START_SEQ, y), 2)  
                key_up.remove(aani_up)
                break
   
def check_mouse_action(x, y, vari):
    global play_or_pause, rec_or_pause, aanitys
    raita = y // 70
    if x > 194 and x< 245 and raita <= raitoja:         # MUTE
        if raita in muted:
            muted.remove(raita)
        else:
            muted.append(raita)
    elif x > 78 and x < 190:                 # REC ENABLE
        if raita in rec_enabled:
            rec_enabled.remove(raita)
        else:
            rec_enabled.append(raita)
    elif x > WIDTH - 85 :    # REC/PAUSE
        rec_or_pause = not rec_or_pause
        if not rec_or_pause:
            aanitys = []
        if rec_or_pause:
            if aanitys != []:
                tallenna()        
    elif x > WIDTH - 185 and x < WIDTH - 85 :   # PLAY/ PAUSE   # TODO PAUSE
        play_or_pause = not play_or_pause
        kuvat_nakyviin(vari)
        pygame.display.flip()           # muista flip !!!!!!!!!!!!!!!!!
        if not play_or_pause and raidat != []:
            if kursori == 0:
                soita_kaikki_raidat()
            #play_or_pause = not play_or_pause

def tekstit_ruudulle():
    teksti = fontti_pieni.render(f"0:00", True, BLACK)
    naytto.blit(teksti, (START_SEQ, 20)) 
    teksti = fontti_pieni.render(f"0:30", True, BLACK)
    naytto.blit(teksti, ((END_SEQ - START_SEQ) // 2 + START_SEQ, 20)) 
    teksti = fontti_pieni.render(f"1:00", True, BLACK)
    naytto.blit(teksti, (END_SEQ, 20)) 
    teksti = fontti_pieni.render(f"ÄÄNITYS: käytä näppäimiä {soittoalue}", True, RED)
    naytto.blit(teksti, (190, HEIGHT -50))


def main():
    ms = 0
    vari = WHITE
    alusta_raidat()
    while True:
        naytto.fill((250, 250, 250)) 
        tekstit_ruudulle()
        for raita_nro in range(len(raidat)):
            if raidat[raita_nro] != []:
                piirra_sekvenssi(raidat[raita_nro])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_SPACE:  # play / pause
                    #soita_melodia(melodia) 
                    break
                if chr(event.key) in soittoalue or chr(event.key) == '/':      # ??? näyttää - mutta tulee / : 
                    if rec_enabled != []:
                        aanita(chr(event.key), True, ms)
                        midi_out.note_on(midi_numbers[chr(event.key)], 110) 

            if event.type == pygame.KEYUP:
                if chr(event.key) in soittoalue or chr(event.key) == '/':      # ??? näyttää - mutta tulee /                
                    if rec_enabled != []:
                        aanita(chr(event.key), False, ms)
                        midi_out.note_off(midi_numbers[chr(event.key)], 110) 
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                check_mouse_action(x, y, vari)        
     
         
        ms += 1
        if ms % 50 == 0 and vari == WHITE:
            vari = RED
        elif ms % 50 == 0 and vari == RED:
            vari = WHITE                 
        kuvat_nakyviin(vari)
        pygame.display.flip()
        kello.tick(100)


main()