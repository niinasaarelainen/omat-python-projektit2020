import random, pygame.midi, pygame

pygame.init()    
pygame.midi.init()
kello = pygame.time.Clock()
naytto = pygame.display.set_mode((911, 220))
fontti = pygame.font.SysFont("FreeMono", 42)
fontti_pieni = pygame.font.SysFont("FreeMono", 25)
port = pygame.midi.get_default_output_id()
midi_out = pygame.midi.Output(port, 0)

WHITE = (200, 200, 200)
aania = 5       # ambitus kvintti jos käyttäjä ei muuta
nap = "zxcvb"


def nappaimet(intervalli):
    # virheellinen syöte TODO
    return "zxcvbnm,."[0 : intervalli]

def alkuohjeet(naytto):
    global nap, aania
    teksti = fontti_pieni.render(f"Valitse intervalli, jonka alueella melodia liikkuu (2-9)", True, WHITE)
    naytto.blit(teksti, (30, 30))
    while True:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()           
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mainloop()
                if event.key >= 50 and event.key <= 58:
                    print(event.key)
                    aania = int(chr(event.key))     
                    print("aania:", aania)               
                    nap = nappaimet(aania)
                teksti = fontti_pieni.render(f" käytä näppäimiä {nap}  (z = keski-c)", True, WHITE)
                naytto.blit(teksti, (30, 75))
                teksti = fontti_pieni.render(f" Sama melodia uudestaan = Space ,  Esc = lopeta", True, WHITE)
                naytto.blit(teksti, (30, 120))     
                teksti = fontti_pieni.render(f" Paina nyt ENTER, kun haluat aloittaa", True, WHITE)
                naytto.blit(teksti, (30, 165))            

        pygame.display.flip()
        kello.tick(40)

"""
def tilanne(naytto):
    fontti_pieni = pygame.font.SysFont("FreeMono", 27)
    pisteet = fontti_pieni.render(f"{pisteet_pel1}", True, GREEN)
    naytto.blit(pisteet, (WINDOW_WIDTH - 51, 31))   """


def generoi_melodia():
    print("aania:", aania)
    aanet = "zxcvbnm,."  # näppäimistön alin rivi 6 ekaa
    return [aanet[random.randint(0,aania -1)]  for i in range(200)]


def midi_play(n, edellinen, instrument):
    midi_out.set_instrument(instrument)  
    midi_numbers = {"z":60, "x":62, "c":64, "v":65, "b":67, "n":69, "m":71 ,",":72, ".":74}    #60 = keski-c, 74 = d2
    midi_out.note_off(midi_numbers[edellinen], 110)
    midi_out.note_on(midi_numbers[n], 110)


def soita_melodia(melodia, montako):
    edellinen = "z"
    for i in range(montako):
        midi_play(melodia[i], edellinen, 2)
        edellinen = melodia[i]
        pygame.time.delay(330)
        
   

def mainloop():
    montako = 3
    edellinen = "z"
    koneen_vuoro = True
    monesko_kayttajan_aani = 0
    virheet = 0   
    melodia = generoi_melodia()    

    while True:
        naytto.fill((10, 10, 10))          
        pituus = fontti.render(f"melodian pituus: {montako}", True, (10, 97, 97))  
        naytto.blit(pituus, (190, 35))    
        virheita = fontti.render(f"virheitä: {virheet}", True, (10, 97, 97))  
        naytto.blit(virheita, (190, 95))  
        pygame.display.flip()

        if koneen_vuoro:
            pygame.time.delay(700)
            soita_melodia(melodia, montako)
            koneen_vuoro = False
            monesko_kayttajan_aani = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    soita_melodia(melodia, montako ) 
                    break
                if not melodia[monesko_kayttajan_aani] == chr(event.key):
                    virheet += 1
                    print("virheitä:",  virheet)
                midi_play(chr(event.key), edellinen, 8)
                edellinen = chr(event.key)
                monesko_kayttajan_aani += 1
                if monesko_kayttajan_aani == montako :
                    montako += 1
                    koneen_vuoro = True       
        
        kello.tick(40)

alkuohjeet(naytto)