import pygame, random, os

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREEN = (0, 200, 20)
YELLOW = (200, 200, 20)
WINDOW_HEIGHT = 910
WINDOW_WIDTH = 770

SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
os.environ['SDL_VIDEO_WINDOW_POS']='{},{}'.format(10,20)     # ????
CLOCK = pygame.time.Clock()
blockSize = 70 #Set the size of the grid block
kirjainten_lkm = 11  # per rivi
kirjainvali = 57

pisteet_pel1 = 0
pisteet_pel2 = 0
#aakkoset = list("AAAAAABDEEEFGHHHIIIIIIIIIJJJKKKKKLLLLLMMMMNNNOOOOOOPPRRRSSSSTTTTUUUUUUUUVVVVVYYYÄÄÄÄÄÖÖÖÖ")
aakkoset = list("AABDEEFGHHIIKLMUOV")
pel1_7 = []
pel2_7 = []
ruudukko = []
kerrokset = {}
edelliset_muuvit = []


def jaa_napit_aloitus():
    for i in range(7):
        pel1_7.append(uusi_nappi())
        pel2_7.append(uusi_nappi())
    
def alusta_ruudukko():
    for rivi in range(kirjainten_lkm):
        ruudukko.append([])
        for sarake in range(kirjainten_lkm):
            ruudukko[rivi].append("")     
    ruudukko[4][2] = "M"  
    ruudukko[4][3] = "U"  
    ruudukko[4][4] = "R"  
    ruudukko[4][5] = "M"  
    ruudukko[4][6] = "E"  
    ruudukko[4][7] = "L"
    ruudukko[4][8] = "I"  
    for x in range (2, 9):
        kerrokset[x, 4] = 1


def uusi_nappi():    
    r = random.randint(0, len(aakkoset) - 1)    
    valittu = aakkoset[r]
    aakkoset.remove(valittu)
    return valittu


def drawGrid():    
    for x in range(kirjainten_lkm):
        for y in range(1,kirjainten_lkm +1):                 
            rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)   # 1 = vain reunat = mustaa keskellä

def tekstit(vuoro):
   
    if vuoro % 4 == 1 or vuoro % 4 == 2:        
        rect = pygame.Rect(15, 34, blockSize // 4, blockSize // 4)
    else:
        rect = pygame.Rect(15, WINDOW_HEIGHT - 40, blockSize // 4, blockSize // 4)
    pygame.draw.rect(SCREEN, YELLOW, rect, 0)    # 0 = kokovalkoinen

    #pisteet:
    fontti = pygame.font.SysFont("FreeMono", 32)
    fontti_pieni = pygame.font.SysFont("FreeMono", 26)
    pel1_str = "  "
    pel1_str = pel1_str.join(sorted(pel1_7)) 
    teksti = fontti.render(f"Pelaaja 1:   {pel1_str} ", True, WHITE)
    pisteet = fontti_pieni.render(f"{pisteet_pel1}", True, GREEN)
    SCREEN.blit(teksti, (40, 24))
    SCREEN.blit(pisteet, (WINDOW_WIDTH - 52, 27))
    pel2_str = "  "
    pel2_str = pel2_str.join(sorted(pel2_7)) 
    teksti = fontti.render(f"Pelaaja 2:   {pel2_str}", True, WHITE)
    pisteet = fontti_pieni.render(f"{pisteet_pel2}", True, GREEN)
    SCREEN.blit(teksti, (40, WINDOW_HEIGHT - 50))
    SCREEN.blit(pisteet, (WINDOW_WIDTH - 52, WINDOW_HEIGHT - 47))

    # näppäinkomennot:
    fontti_pieni = pygame.font.SysFont("FreeMono", 15)
    nappaink = fontti_pieni.render(f"ENTER = VUORONVAIHTO   V = VAIHDA KIRJAIN   L = LOPETA (KUMPIKAAN EI VOI SIIRTÄÄ)", True, YELLOW)
    SCREEN.blit(nappaink, (36, 4))

    fontti = pygame.font.SysFont("FreeMono", 50)
    fontti_pieni = pygame.font.SysFont("FreeMono", 24)
    for rivi in range(kirjainten_lkm):
        for sarake in range(kirjainten_lkm):            
            kirjain = ruudukko[rivi][sarake]
            if not kirjain == "":
                kirjain = fontti.render(kirjain, True, WHITE)
                SCREEN.blit(kirjain, ((sarake + 0.27) *blockSize , (rivi + 1.17) *blockSize))      
                kerros_lkm = kerrokset[sarake, rivi]    
                if kerros_lkm > 1:
                    kerros = fontti_pieni.render(str(kerros_lkm), True, WHITE)
                    SCREEN.blit(kerros, (sarake * blockSize , (rivi + 1) * blockSize))    

    

def mika_kirjain(x):
    # 297, 353, 412, 466, 525, 580, 638    kirjainten keskipisteet
    indeksi = 0
    for i in range(7):
        if x > 297 - (kirjainvali // 2) + i * kirjainvali:
            indeksi = i
    return indeksi


def minne_kirjain(x, y, kirjain, vuoro):

    #global pisteet_pel1
    #global pisteet_pel2
    x_indeksi = 0
    y_indeksi = 0 

    for i in range(kirjainten_lkm):
        if x > i * blockSize :
            x_indeksi = i
        if y > blockSize + i * blockSize :   # ylhäällä muuta tekstiä yhden blockSize:n verran
            y_indeksi = i
    if (x_indeksi, y_indeksi) not in kerrokset:
        kerrokset[x_indeksi, y_indeksi] = 1        
        ruudukko[y_indeksi][x_indeksi] = kirjain        
    elif kerrokset[x_indeksi, y_indeksi] == 5:
        return False
    else:
        kerrokset[x_indeksi, y_indeksi] += 1        
        ruudukko[y_indeksi][x_indeksi] = kirjain        

    edelliset_muuvit.append([x_indeksi, y_indeksi])
    return True
    

def tutki_mouse(x, y, vuoro, kirjain):
    global edelliset_muuvit
    kirjain_ind = -1

    if vuoro % 4 == 1 and y < blockSize:    # TODO sittenkin toinen kirjain ennen laittoa ?!?
        kirjain_ind = mika_kirjain(x)
        kirjain = sorted(pel1_7)[kirjain_ind]   
        vuoro += 1          
  
    elif vuoro % 4 == 2 and y >= blockSize and y <= WINDOW_HEIGHT - blockSize:    
        if minne_kirjain(x, y, kirjain, vuoro):
            pel1_7.remove(kirjain)    
            print(sorted(edelliset_muuvit))            
        
        vuoro -= 1   # oletus että lisätään useampi kuin 1 kirjain

    elif vuoro % 4 == 3 and y > WINDOW_HEIGHT - blockSize:        
        kirjain_ind = mika_kirjain(x)
        kirjain = sorted(pel2_7)[kirjain_ind]
        vuoro += 1 

    elif vuoro % 4 == 0 and y >= blockSize and y <= WINDOW_HEIGHT - blockSize:    
        if minne_kirjain(x, y, kirjain, vuoro):
            pel2_7.remove(kirjain)
            print(sorted(edelliset_muuvit))
        vuoro -= 1 

    return kirjain, kirjain_ind, vuoro


def tutki_edelliset_muuvit_vaaka(edelliset_muuvit):    
    tuplapisteet = True
    pisteet_tama_kierros = 0
    x_t = [x for x, y in edelliset_muuvit]
    y_t = [y for x, y in edelliset_muuvit]
    sanan_pituus = x_t[-1] - x_t[0] + 1    # itse laitetut napi !!!!
    
    # itse laitetut napit
    for x, y in edelliset_muuvit:
        pisteet_tama_kierros += kerrokset[x, y]
        if kerrokset[x, y] > 1:
           tuplapisteet = False 

    # sanan välissä oleva(t) valmis kirjain  
    muistiin = []  
    if len(x_t) > 1:        
        for x in range (x_t[0], x_t[-1]):
            if not x in x_t:
                muistiin.append(x)
    for x in muistiin:
        pisteet_tama_kierros += kerrokset[x, y_t[0]]   # kaikilla sama y


    # tutkitaan vaakasuorassa sanan reunat   
    x = x_t[0]
    while x > 0:
        if not ruudukko[y_t[0]][x - 1] == "":
            if kerrokset[x -1, y_t[0]] > 1 :   # 2 pistettä pohjakerroksesta, jos sana kokonaan 1-kerroksinen
                tuplapisteet = False
            pisteet_tama_kierros += kerrokset[x -1, y_t[0]]
            sanan_pituus += 1
            print(" vaaka vas")
            x -= 1 
        else:
            break

    x = x_t[-1] + 1
    while x < kirjainten_lkm :
        if not ruudukko[y_t[-1]][x] == "":
            if kerrokset[x, y_t[-1]] > 1 :   # 2 pistettä pohjakerroksesta
                tuplapisteet = False
            pisteet_tama_kierros += kerrokset[x, y_t[-1]]
            sanan_pituus += 1
            print(" vaaka oik")
            x += 1
        else:
            break 
        
    if tuplapisteet:
        pisteet_tama_kierros *= 2
    
    if sanan_pituus == 1:
        return 0
    
    return pisteet_tama_kierros


def tutki_edelliset_muuvit_pysty(edelliset_muuvit):
    tuplapisteet = True
    pisteet_tama_kierros = 0
    x_t = [x for x, y in edelliset_muuvit]
    y_t = [y for x, y in edelliset_muuvit]
    sanan_pituus =  y_t[-1] - y_t[0] + 1   # itse laitetut napi !!!!
    
    #itse laitetut napit
    for x, y in edelliset_muuvit:
        pisteet_tama_kierros += kerrokset[x, y]
        if kerrokset[x, y] > 1:
           tuplapisteet = False 

    # sanan välissä oleva(t) valmis kirjain  
    muistiin = []  
    if len(y_t) > 1:        
        for y in range (y_t[0], y_t[-1]):
            if not y in y_t:
                muistiin.append(y)
    for y in muistiin:
        pisteet_tama_kierros += kerrokset[x_t[0], y]   # kaikilla sama y
    
    # tutkitaan pystysuorassa sanan reunat
    y = y_t[0]
    while y > 0:
        if not ruudukko[y -1][x_t[0]] == "":
            if kerrokset[x_t[0], y -1] > 1 :   # 2 pistettä pohjakerroksesta, jos sana kokonaan 1-kerroksinen
                tuplapisteet = False
            pisteet_tama_kierros += kerrokset[x_t[0], y -1]
            sanan_pituus += 1
            print(" pysty ylä")
            y -= 1 
        else:
            break

    y = y_t[-1]
    while y < kirjainten_lkm -1:
        if not ruudukko[y +1][x_t[0]] == "":
            if kerrokset[x_t[0], y +1] > 1 :   # 2 pistettä pohjakerroksesta, jos sana kokonaan 1-kerroksinen
                tuplapisteet = False
            pisteet_tama_kierros += kerrokset[x_t[0], y +1]
            sanan_pituus += 1
            print(" pysty ala")
            y += 1 
        else:
            break
        
    if tuplapisteet:
        pisteet_tama_kierros *= 2

    if sanan_pituus == 1:
        return 0
    
    return pisteet_tama_kierros

def vaihda_nappi(vuoro, kirjain):             # TODO
    print(pel1_7)
    pyorii = True
    while pyorii:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN: 
                x = event.pos[0]
                y = event.pos[1]                  
                kirjain, kirjain_ind, vuoro_uusi = tutki_mouse(x, y, vuoro, kirjain)  
                if vuoro % 4 == 1 or vuoro % 4 == 2:
                    pel1_7.remove(kirjain)   
                    pel1_7.append(uusi_nappi())
                else:
                    pel2_7.remove(kirjain) 
                    pel2_7.append(uusi_nappi())
                vuoro = vuoro_uusi  
                pyorii = False
        CLOCK.tick(8000)    
           
    print(pel1_7)
    return vuoro + 1, kirjain    # vuoro hyppäää ruudukko"tilan" yli


def lopputeksti(vuoro):   # vuoro voi olla myös -1, jos ei painettiin "L"
    global pisteet_pel1, pisteet_pel2
    if vuoro > 0 and (vuoro % 4 == 1 or vuoro % 4 == 2):
        pisteet_pel1 += tutki_edelliset_muuvit_vaaka(sorted(edelliset_muuvit))
        pisteet_pel1 += tutki_edelliset_muuvit_pysty(sorted(edelliset_muuvit))  
    elif vuoro > 0 and (vuoro % 4 == 3 or vuoro % 4 == 4):
        pisteet_pel2 += tutki_edelliset_muuvit_vaaka(sorted(edelliset_muuvit))
        pisteet_pel2 += tutki_edelliset_muuvit_pysty(sorted(edelliset_muuvit))  

    SCREEN.fill(BLACK)
    while True:
        fontti_iso = pygame.font.SysFont("FreeMono", 62)
        if pisteet_pel1 == pisteet_pel2:
            teksti = fontti_iso.render(f"Tasapeli", True, WHITE)
            SCREEN.blit(teksti, (30, 90))
        elif pisteet_pel1 > pisteet_pel2:
            teksti = fontti_iso.render(f"Pelaaja 1 voitti !!", True, WHITE)
            SCREEN.blit(teksti, (30, 90))
        else:
            teksti = fontti_iso.render(f"Pelaaja 2 voitti !!", True, WHITE)
            SCREEN.blit(teksti, (30, 90))

        teksti = fontti_iso.render(f"{pisteet_pel1} - {pisteet_pel2}", True, WHITE)
        SCREEN.blit(teksti, (230, 290))    
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


def main():
    pygame.init()    
    
    vuoro = 1
    kirjain = ""
    fontti = pygame.font.SysFont("FreeMono", 30)
    valitus = fontti.render(f"", True, GREEN)
    kirjain_ind = -1    
    global edelliset_muuvit, pisteet_pel1, pisteet_pel2

    while len(pel1_7) > 0 and len(pel2_7) > 0:       
        SCREEN.fill(BLACK)
        tekstit(vuoro)
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN: 
                x = event.pos[0]
                y = event.pos[1]                  
                kirjain, kirjain_ind, vuoro_uusi = tutki_mouse(x, y, vuoro, kirjain)     
                vuoro = vuoro_uusi  
            if event.type == pygame.KEYDOWN:   
                #vuoronvaihto
                if event.key == pygame.K_RETURN:
                    if (vuoro % 4 == 1 or vuoro % 4 == 2) and len(edelliset_muuvit) > 0:
                        pisteet_pel1 += tutki_edelliset_muuvit_vaaka(sorted(edelliset_muuvit))
                        pisteet_pel1 += tutki_edelliset_muuvit_pysty(sorted(edelliset_muuvit))                    
                        for muuvi in edelliset_muuvit:
                            if len(aakkoset) > 0:
                                pel1_7.append(uusi_nappi())
                    elif len(edelliset_muuvit) > 0: 
                        pisteet_pel2 += tutki_edelliset_muuvit_vaaka(sorted(edelliset_muuvit))
                        pisteet_pel2 += tutki_edelliset_muuvit_pysty(sorted(edelliset_muuvit))
                        for muuvi in edelliset_muuvit:
                            if len(aakkoset) > 0:
                                pel2_7.append(uusi_nappi())                    
                    vuoro += 2
                    edelliset_muuvit = []
                #vaihda nappi
                if chr(event.key) == "v":
                    if len(aakkoset) > 0:
                        vuoro, kirjain = vaihda_nappi(vuoro, kirjain)   
                    else:
                        valitus = fontti.render(f"Ei enää uusia aakkosia, ei voi vaihtaa", True, YELLOW)

                # lopetus
                if chr(event.key) == "l":
                    lopputeksti(-1)

        # neliöidään valittu kirjain
        if kirjain_ind >= 0 and (vuoro % 4 == 1 or vuoro % 4 == 2):   #   -1 = ei tarvitse neliöidä
            rect = pygame.Rect(278 + kirjain_ind * kirjainvali , 23, blockSize // 2 + 2, blockSize // 2 + 2)
            pygame.draw.rect(SCREEN, WHITE, rect, 2)
            
        elif kirjain_ind >= 0 and (vuoro % 4 == 3 or vuoro % 4 == 0):
            rect = pygame.Rect(278 + kirjain_ind * kirjainvali , WINDOW_HEIGHT - 52, blockSize // 2 + 2, blockSize // 2 + 2)
            pygame.draw.rect(SCREEN, WHITE, rect, 2)

        #valitusteksti        
        SCREEN.blit(valitus, (61, 71))
        
        CLOCK.tick(8000)   
        pygame.display.flip()
            
    lopputeksti(vuoro)
    

        
        

jaa_napit_aloitus()    
alusta_ruudukko() 
main()