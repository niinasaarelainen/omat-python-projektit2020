import random, pygame.midi, pygame

pygame.init()    
pygame.midi.init()
kello = pygame.time.Clock()
WIDTH = 505
HEIGHT = 500
naytto = pygame.display.set_mode((WIDTH, HEIGHT))
fontti = pygame.font.SysFont("FreeMono", 42)
fontti_pieni = pygame.font.SysFont("FreeMono", 24)
port = pygame.midi.get_default_output_id()
midi_out = pygame.midi.Output(port, 0)
midi_out.set_instrument(2)
midi_numbers = {"z":60, "x":62, "c":64, "v":65, "b":67, "n":69, "m":71 ,",":72, ".":74}    #60 = keski-c, 74 = d2

WHITE = (200, 200, 200)
BLUE = (10, 97, 97)
BLACK = (10, 10, 10)
valkoinen = (250, 250, 250)
punainen = (251, 0, 0)
soittoalue = "zxcvbnm,.-"
rec_enabled = [1]
muted = []
raitoja = 4
raidat = []
play_or_pause = True
rec_or_pause = True
kursori = 0     # missä kohtaa äänitystä ollaan menossa, eli monesko melodian ääni
aanitys = []

play = pygame.image.load('play.png')
play = pygame.transform.scale(play, (65, 65))

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
        teksti = fontti_pieni.render(f"{i}", True, (10, 10, 10))
        naytto.blit(teksti, (40, i*70))
        naytto.blit(rec, (80, i*70 - 30))
        if i in muted:
            naytto.blit(mute, (190, i*70 ))
        else:
            naytto.blit(unmute, (190, i*70 ))  

    for raita in rec_enabled:
        pygame.draw.circle(naytto, vari, (107, raita*70 + 14), 11)     # parametri vari tänne

    # PLAY / PAUSE:
    if play_or_pause:
        naytto.blit(play, (WIDTH - 188, HEIGHT - 138))
    else:
        naytto.blit(pause, (WIDTH - 188, HEIGHT - 138))
    # REC / PAUSE:
    if rec_or_pause:
        pygame.draw.circle(naytto, punainen, (WIDTH - 66, HEIGHT - 104), 33)  
    else:
        naytto.blit(pause_red, (WIDTH - 100, HEIGHT - 138)) 




  
    
    


def soita_raita(aanitys):   
    laskuri = 0   
    for i in range(len(aanitys)):
        kirjain, down, ms = aanitys[i]
        print(laskuri, ms)
        while laskuri != ms:
            laskuri += 1
            kello.tick(100)
           
        if down:
            midi_out.note_on(midi_numbers[kirjain], 120) 
        else:
            midi_out.note_off(midi_numbers[kirjain], 120)
        

def soita_kaikki_raidat():
    flat_list = [item for sublist in raidat for item in sublist]
    s = sorted(flat_list, key = lambda x: x[1])
    soita_raita(s)


def aanita(kirjain, down, ms):    # down = True, up = False
    global aanitys
    aanitys.append((kirjain, down, ms))
       

def tallenna():
    global aanitys
    ms_offset = aanitys[0][2]
    aanitys = [(aani[0], aani[1], aani[2] - ms_offset) for aani in aanitys]
    for raita_nro in rec_enabled:
        print("aanitys@tallenna", aanitys)
        raidat[raita_nro - 1] = aanitys


   
def check_mouse_action(x, y, vari):
    global play_or_pause, rec_or_pause, aanitys
    raita = y // 70
    if x > 194 and raita <= raitoja:         # MUTE
        if raita in muted:
            muted.remove(raita)
        else:
            muted.append(raita)
    elif x > 78 and x < 190:                 # REC ENABLE
        if raita in rec_enabled:
            rec_enabled.remove(raita)
        else:
            rec_enabled.append(raita)
    elif x > WIDTH - 85 and raita > raitoja:    # REC/PAUSE
        rec_or_pause = not rec_or_pause
        if not rec_or_pause:
            aanitys = []
        if rec_or_pause:
            print(aanitys)
            tallenna()        
    elif x > WIDTH - 185 and x < WIDTH - 85 and raita > raitoja:   # PLAY/ PAUSE   # TODO PAUSE
        play_or_pause = not play_or_pause
        kuvat_nakyviin(vari)
        pygame.display.flip()           # muista flip !!!!!!!!!!!!!!!!!
        if not play_or_pause and aanitys != []:
            soita_kaikki_raidat()
            play_or_pause = not play_or_pause
        




def main():
    ms = 0
    vari = valkoinen
    alusta_raidat()
    print(raidat)
    while True:
        naytto.fill((250, 250, 250)) 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_SPACE:  # play / pause
                    #soita_melodia(melodia) 
                    break
                if chr(event.key) in soittoalue: 
                    if rec_enabled != []:
                        aanita(chr(event.key), True, ms)
            if event.type == pygame.KEYUP:
                if chr(event.key) in soittoalue: 
                    if rec_enabled != []:
                        aanita(chr(event.key), False, ms)
            
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                check_mouse_action(x, y, vari)        
     
        teksti = fontti_pieni.render(f"ÄÄNITYS: käytä näppäimiä {soittoalue}", True, punainen)
        naytto.blit(teksti, (10, HEIGHT -50))  
        ms += 1
        if ms % 50 == 0 and vari == valkoinen:
            vari = punainen
        elif ms % 50 == 0 and vari == punainen:
            vari = valkoinen                 
        kuvat_nakyviin(vari)
        pygame.display.flip()
        kello.tick(100)


main()