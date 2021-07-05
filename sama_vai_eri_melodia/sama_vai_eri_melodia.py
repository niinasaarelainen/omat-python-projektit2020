import random, pygame.midi, pygame

"""
pygame.init()    
pygame.midi.init()
kello = pygame.time.Clock()
naytto = pygame.display.set_mode((911, 220))
fontti = pygame.font.SysFont("FreeMono", 42)
fontti_pieni = pygame.font.SysFont("FreeMono", 25)
port = pygame.midi.get_default_output_id()
midi_out = pygame.midi.Output(port, 0) """

WHITE = (200, 200, 200)
BLUE = (10, 97, 97)
aania = 5       # ambitus kvintti 
soittoalue = "zxcvbnm,."
melodiat = {4:[], 5:[], 6:[]}
eka = ""
toka = ""



def alkuohjeet(naytto):
    global aania
    naytto.fill((10, 10, 10))  
    while True:    
        for event in pygame.event.get(): 
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()

        teksti = fontti_pieni.render(f" Kuulet kaksi melodiaa, joiden välissä on tauko", True, WHITE)
        naytto.blit(teksti, (30, 75))
        teksti = fontti_pieni.render(f" Klikkaa ovatko ne sama vai eri", True, WHITE)
        naytto.blit(teksti, (30, 100))   
        teksti = fontti_pieni.render(f" Paina nyt ENTER, kun haluat aloittaa", True, WHITE)
        naytto.blit(teksti, (30, 125))            

        pygame.display.flip()
        kello.tick(40)

def muodosta_melodiat():
    global melodiat
    melodiat[4].append(["zcvb", "zcbb", "zcvc", "zxvb", "zcxb", "zcbb", "zxbb", "zcbv", "zcvv"])
    # TODO 5, 6


def valitse_melodiat(montako_aanta):
    global eka, toka
    monesko_melodia = random.randint(0, len(melodiat[montako_aanta][0]) - 1) 
    print("monesko_melodia", monesko_melodia)
    eka = melodiat[montako_aanta][0][monesko_melodia]
    sama_vai_ei = random.randint(0,1) 
    if sama_vai_ei == 0:        
        toka = eka
    else:        
        monesko_melodia2 = random.randint(0, len(melodiat[montako_aanta]) - 1) 
        while monesko_melodia2 == monesko_melodia:
             monesko_melodia2 = random.randint(0, len(melodiat[montako_aanta][0]) - 1) 
        toka = melodiat[montako_aanta][0][monesko_melodia2]
        print("monesko_melodia2", monesko_melodia2)
    return eka, toka


def midi_play(n, instrument):
    midi_out.set_instrument(instrument)  
    midi_numbers = {"z":60, "x":62, "c":64, "v":65, "b":67, "n":69, "m":71 ,",":72, ".":74}    #60 = keski-c, 74 = d2
    midi_out.note_on(midi_numbers[n], 110)    
    pygame.time.delay(300)
    midi_out.note_off(midi_numbers[n], 110)


def soita_melodia(melodia, montako):
    for i in range(montako):
        midi_play(melodia[i], 2)        
   

def main():
    montako_aanta = 4
    virheet = 0     

    while True:
        naytto.fill((10, 10, 10))          
        pituus = fontti.render(f"melodian pituus: {montako_aanta}", True, BLUE)  
        naytto.blit(pituus, (190, 35))    
        virheita = fontti.render(f"virheitä: {virheet}", True, BLUE)  
        naytto.blit(virheita, (190, 95))  
        teksti = fontti_pieni.render(f" Sama pari uudestaan = Space ,  Esc = lopeta", True, WHITE)
        naytto.blit(teksti, (65, 180))   
        pygame.display.flip()

        pygame.time.delay(700)
        valitse_melodiat(montako_aanta)
        #soita_melodia(melodia, montako)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
                    
        
        kello.tick(40)



muodosta_melodiat()
print(valitse_melodiat(4))
#alkuohjeet(naytto)