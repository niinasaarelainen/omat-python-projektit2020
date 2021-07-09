import random, pygame.midi, pygame


pygame.init()    
pygame.midi.init()
kello = pygame.time.Clock()
naytto = pygame.display.set_mode((911, 320))
fontti = pygame.font.SysFont("FreeMono", 42)
fontti_pieni = pygame.font.SysFont("FreeMono", 25)
port = pygame.midi.get_default_output_id()
midi_out = pygame.midi.Output(port, 0) 

WHITE = (200, 200, 200)
BLUE = (10, 97, 97)
GREEN = (7, 210, 7)
blockSize = 60
x_aloitus = 100
y_aloitus = 60
aania = 5       # ambitus kvintti 
soittoalue = "zxcvbnm,."
melodiat = {3:[], 4:[], 5:[], 6:[]}
eka = ""
toka = ""
sama = False   
montako_aanta = 4
AANTEN_MAX = 6
AANTEN_MIN = 3



def alkuohjeet(naytto):
    global aania
    naytto.fill((10, 10, 10))  
    while True:    
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        main()

        teksti = fontti_pieni.render(f" Kuulet kaksi melodiaa, joiden välissä on tauko", True, WHITE)
        naytto.blit(teksti, (30, 70))
        teksti = fontti_pieni.render(f" Klikkaa ovatko ne sama vai eri", True, WHITE)
        naytto.blit(teksti, (30, 100))   
        teksti = fontti_pieni.render(f" Paina nyt ENTER, kun haluat aloittaa", True, WHITE)
        naytto.blit(teksti, (30, 175))            

        pygame.display.flip()
        kello.tick(40)

def muodosta_melodiat():
    global melodiat
    melodiat[3] = ["123", "357", "865"]
    melodiat[4] = ["1235", "3576", "8657"] 
    melodiat[5] = ["123", "357", "865"]  #TODO
    melodiat[6] = ["123", "357", "865"]
    

def valitse_melodiat(montako_aanta):
    global eka, toka, sama
    monesko_melodia = random.randint(0, len(melodiat[montako_aanta]) - 1) 
    print("monesko_melodia", monesko_melodia)
    eka = melodiat[montako_aanta][monesko_melodia]
    sama_vai_ei = random.randint(0,1) 
    toka = eka
    if sama_vai_ei == 0:  
        sama = True
    else:        
        monesko_aani_muuttuu = random.randint(0, montako_aanta-1) 
        alas_vai_ylos = random.randint(0, 1) 
        if alas_vai_ylos == 0:        
            uusi_aani = min(8, int(eka[monesko_aani_muuttuu]) + 1)            
        else:  
            uusi_aani = max(0, int(eka[monesko_aani_muuttuu]) - 1)  
        toka = toka.replace(str(eka[monesko_aani_muuttuu]), str(uusi_aani))
        sama = False
    print("eka:", eka, "toka",  toka)
    return eka, toka


def midi_play(n, instrument):
    midi_out.set_instrument(instrument)  
    midi_numbers = {"1":60, "2":62, "3":64, "4":65, "5":67, "6":69, "7":71 ,"8":72}    
    midi_out.note_on(midi_numbers[n], 110)    
    pygame.time.delay(300)
    midi_out.note_off(midi_numbers[n], 110)


def soita_melodiat(montako):
    for i in range(montako):
        midi_play(eka[i], 2)  
    pygame.time.delay(700) 
    for i in range(montako):
        midi_play(toka[i], 2)       


def draw_tekstit(pisteet, kysytty):
    rect = pygame.Rect( x_aloitus, y_aloitus, blockSize*3, blockSize)
    pygame.draw.rect(naytto, WHITE, rect, 1)   # 1 = vain reunat = mustaa keskellä
    text = fontti.render(f" SAMA ", True, BLUE)  
    naytto.blit(text, (x_aloitus + 10, y_aloitus + 5))
    rect = pygame.Rect (x_aloitus + blockSize*3,  y_aloitus, blockSize*3, blockSize)
    pygame.draw.rect(naytto, WHITE, rect, 1)   # 1 = vain reunat = mustaa keskellä
    text = fontti.render(f" ERI ", True, BLUE)  
    naytto.blit(text, (300, y_aloitus + 5))
    
    virheita = fontti_pieni.render(f"oikein: {pisteet}/{kysytty}", True, GREEN)  
    naytto.blit(virheita, (660, y_aloitus + 5)) 
    teksti = fontti_pieni.render(f" Soita sama pari uudestaan = Space ,  Esc = lopeta", True, WHITE)
    naytto.blit(teksti, (65, 183))     

    text = fontti_pieni.render(f" Melodian pituus: nuolet ylös ja alas (nykyinen {montako_aanta})", True, WHITE)  
    naytto.blit(text, (65, 250))

def main():    
    global montako_aanta
    pisteet = 0   
    kysytty = 0
    naytto.fill((10, 10, 10))     
    draw_tekstit(pisteet, kysytty)      
    pygame.display.flip()
    valitse_melodiat(montako_aanta)
    soita_melodiat(montako_aanta)   

    while True:
        naytto.fill((10, 10, 10))     
        draw_tekstit(pisteet, kysytty)                   
        #pygame.time.delay(700)             

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    soita_melodiat(montako_aanta) 
                if event.key == pygame.K_UP:
                    if montako_aanta < AANTEN_MAX:
                        montako_aanta += 1
                        valitse_melodiat(montako_aanta)
                if event.key == pygame.K_DOWN:
                    if montako_aanta > AANTEN_MIN:
                        montako_aanta -= 1
                        valitse_melodiat(montako_aanta)
            if event.type == pygame.MOUSEBUTTONDOWN:  
                x = event.pos[0]
                y = event.pos[1]                 
                if x > x_aloitus + blockSize*3 :
                    if sama == False:
                        pisteet += 1
                else:
                     if sama == True:
                         pisteet += 1
                kysytty += 1
                     
                naytto.fill((10, 10, 10))     
                draw_tekstit(pisteet, kysytty)                        
                pygame.display.flip()

                valitse_melodiat(montako_aanta)
                soita_melodiat(montako_aanta)
                
                    
        pygame.display.flip()
        kello.tick(50)



muodosta_melodiat()
alkuohjeet(naytto)