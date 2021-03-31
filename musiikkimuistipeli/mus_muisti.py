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
BLUE = (10, 97, 97)
aania = 5       # ambitus kvintti jos käyttäjä ei muuta
nap = "zxcvb"
soittoalue = "zxcvbnm,."
valinta = 1


def nappaimet(intervalli):
    # virheellinen syöte TODO
    return "zxcvbnm,."[0 : intervalli]

def alkuohjeet1(naytto):
    global nap, aania
    teksti = fontti_pieni.render(f"Valitse intervalli, jonka alueella melodia liikkuu (2-9)", True, WHITE)
    naytto.blit(teksti, (30, 30))
    while True:    
        for event in pygame.event.get():                  
            if event.type == pygame.KEYDOWN:
                if event.key >= 50 and event.key <= 58:
                    print(event.key)
                    aania = int(chr(event.key))     
                    print("aania:", aania)               
                    nap = nappaimet(aania)
                    alkuohjeet2(naytto)
                else:
                    naytto.fill((10, 10, 10))  
                    teksti = fontti_pieni.render(f"Paina 2, 3, 4, 5, 6, 7, 8 tai 9", True, WHITE)
                    naytto.blit(teksti, (30, 30))

        pygame.display.flip()
        kello.tick(40)

def alkuohjeet2(naytto):
    global valinta
    naytto.fill((10, 10, 10))  
    teksti = fontti_pieni.render(f" Paina 1 tai 2", True, WHITE)
    naytto.blit(teksti, (30, 30))
    teksti = fontti_pieni.render(f" 1 = Sama melodia pitenee, 2 = Aina uusi melodia", True, WHITE)
    naytto.blit(teksti, (30, 100)) 
    while True:    
        for event in pygame.event.get():                  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    valinta = 1
                    alkuohjeet3(naytto)
                elif event.key == pygame.K_2:
                    valinta = 2
                    alkuohjeet3(naytto)
                else:
                    alkuohjeet2(naytto)
        pygame.display.flip()
        kello.tick(40)   

def alkuohjeet3(naytto):
    global nap, aania
    naytto.fill((10, 10, 10))  
    while True:    
        for event in pygame.event.get(): 
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()

        teksti = fontti_pieni.render(f" käytä näppäimiä {nap}  (z = keski-c)", True, WHITE)
        naytto.blit(teksti, (30, 75))
        teksti = fontti_pieni.render(f" Paina nyt ENTER, kun haluat aloittaa", True, WHITE)
        naytto.blit(teksti, (30, 105))            

        pygame.display.flip()
        kello.tick(40)


def generoi_melodia():
    aanet = "zxcvbnm,."  # näppäimistön alin rivi 
    return [aanet[random.randint(0,aania -1)]  for i in range(200)]


def midi_play(n, instrument):
    midi_out.set_instrument(instrument)  
    midi_numbers = {"z":60, "x":62, "c":64, "v":65, "b":67, "n":69, "m":71 ,",":72, ".":74}    #60 = keski-c, 74 = d2
    midi_out.note_on(midi_numbers[n], 110)    
    pygame.time.delay(300)
    midi_out.note_off(midi_numbers[n], 110)


def soita_melodia(melodia, montako):
    for i in range(montako):
        midi_play(melodia[i], 2)        
   

def uusi_melodia():                         # TODO
    print("def uusi_melodia")


def main():
    montako = 3
    koneen_vuoro = True
    monesko_kayttajan_aani = 0
    virheet = 0   
    melodia = generoi_melodia()    

    while True:
        naytto.fill((10, 10, 10))          
        pituus = fontti.render(f"melodian pituus: {montako}", True, BLUE)  
        naytto.blit(pituus, (190, 35))    
        virheita = fontti.render(f"virheitä: {virheet}", True, BLUE)  
        naytto.blit(virheita, (190, 95))  
        teksti = fontti_pieni.render(f" Sama melodia uudestaan = Space ,  Esc = lopeta", True, WHITE)
        naytto.blit(teksti, (65, 180))   
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
                    soita_melodia(melodia, montako) 
                    break
                if not melodia[monesko_kayttajan_aani] == chr(event.key) and chr(event.key) in soittoalue:
                    virheet += 1
                    print("virheitä:",  virheet)
                if chr(event.key) in soittoalue: 
                    midi_play(chr(event.key), 8)
                    monesko_kayttajan_aani += 1
                if monesko_kayttajan_aani == montako :
                    montako += 1
                    koneen_vuoro = True       
                    if valinta == 2:     # 1 = Sama melodia pitenee, 2 = Aina uusi melodia
                        melodia = generoi_melodia()   
        
        kello.tick(40)

alkuohjeet1(naytto)