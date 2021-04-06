import random, pygame.midi, pygame

pygame.init()    
pygame.midi.init()
kello = pygame.time.Clock()
WIDTH = 500
HEIGHT = 500
naytto = pygame.display.set_mode((WIDTH, HEIGHT))
fontti = pygame.font.SysFont("FreeMono", 42)
fontti_pieni = pygame.font.SysFont("FreeMono", 25)
port = pygame.midi.get_default_output_id()
midi_out = pygame.midi.Output(port, 0)

WHITE = (200, 200, 200)
BLUE = (10, 97, 97)
soittoalue = "zxcvbnm,.-"
raita_rec_enabled = [1, 3]
muted = []
raitoja = 4
vari = "valkoinen"

play = pygame.image.load('play.png')
play = pygame.transform.scale(play, (60, 60))
rec = pygame.image.load('rec.jpg')
rec = pygame.transform.scale(rec, (90, 90))
mute  = pygame.image.load('mute.png')
mute = pygame.transform.scale(mute, (40, 40))
unmute  = pygame.image.load('unmute.png')
unmute = pygame.transform.scale(unmute, (40, 40))


def kuvat_nakyviin():
    naytto.blit(play, (WIDTH - 90, HEIGHT - 90))
    for i in range(1, raitoja + 1):
        teksti = fontti_pieni.render(f"{i}", True, (10, 10, 10))
        naytto.blit(teksti, (40, i*70))
        naytto.blit(rec, (80, i*70 - 30))
        if i in muted:
            naytto.blit(mute, (190, i*70 ))
        else:
            naytto.blit(unmute, (190, i*70 ))
    
def aktiiviset_kuvat():
    global vari
    for raita in raita_rec_enabled:
        if vari == "valkoinen":
            print("valkoinen")
            pygame.draw.circle(naytto, (250, 250, 250), (107, raita*70 + 14), 11) #valk
            vari = "punainen"
        else:
            print("pun")
            pygame.draw.circle(naytto, (255, 0, 0), (107, raita*70 + 14), 11)  # pun
            vari = "valkoinen"


def midi_play(n, instrument):
    midi_out.set_instrument(instrument)  
    midi_numbers = {"z":60, "x":62, "c":64, "v":65, "b":67, "n":69, "m":71 ,",":72, ".":74}    #60 = keski-c, 74 = d2
    midi_out.note_on(midi_numbers[n], 110)    
    pygame.time.delay(300)
    midi_out.note_off(midi_numbers[n], 110)


"""
def soita_melodia(melodia):
    for i in range(len(melodia)):
        midi_play(melodia[i], 2)         """
   
def check_mouse_action(x, y):
    raita = y // 70
    if x > 194:
        if raita in muted:
            muted.remove(raita)
        else:
            muted.append(raita)
    print(muted)


def main():
    varinvaihto = 0
    while True:
        naytto.fill((250, 250, 250))          
        kuvat_nakyviin()
        teksti = fontti_pieni.render(f" käytä näppäimiä {soittoalue}  (z = keski-c)", True, WHITE)
        naytto.blit(teksti, (HEIGHT -80, 75))          
        pygame.display.flip()

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
                    midi_play(chr(event.key), 8)
            
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                check_mouse_action(x, y)
        
        
        varinvaihto += 1
        if varinvaihto % 15 == 0:
            aktiiviset_kuvat()
        kello.tick(50)
        




main()