import pygame, random, os, copy
from oikeellisuus import Oikeellisuus    # toimii vaikka alleviivaus !!!!!!!!

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
vuoro = 1
aakkoset = list("AAAAAAABDEEEFGHHHIIIIIIIIIJJJKKKKKLLLLLMMMMNNNOOOOOOPPRRRSSSSTTTTUUUUUUUUVVVVVYYYÄÄÄÄÖÖÖ")
#aakkoset = list("ABDEFGHHIIKLMOV")
kahden_pisteen_kirjaimet = ["B", "D", "F", "G"]
pel1_7 = []
pel2_7 = []
ruudukko = []
kerrokset = {}
edelliset_muuvit = []     # yhden siirron ajan
kirjaimet_yhdensiirronajalta = []
kaikki_muuvit_talteen = []   # koko pelin ajan --> UNDO
oikeellisuus = Oikeellisuus()


def jaa_napit_aloitus():
    for i in range(7):
        pel1_7.append(uusi_nappi())
        pel2_7.append(uusi_nappi())
    
def alusta_ruudukko():
    for rivi in range(kirjainten_lkm):
        ruudukko.append([])
        for sarake in range(kirjainten_lkm):
            ruudukko[rivi].append("") 
    kaikki_muuvit_talteen.append(copy.deepcopy(ruudukko))

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

def tekstit():   
    if vuoro % 4 == 1 or vuoro % 4 == 2:        
        rect = pygame.Rect(15, 34, blockSize // 4, blockSize // 4)
    else:
        rect = pygame.Rect(15, WINDOW_HEIGHT - 40, blockSize // 4, blockSize // 4)
    pygame.draw.rect(SCREEN, YELLOW, rect, 0)    # 0 = kokovalkoinen

    #napit ja pisteet:
    fontti = pygame.font.SysFont("FreeMono", 32)
    fontti_pieni = pygame.font.SysFont("FreeMono", 27)
    pel1_str = "  "
    pel1_str = pel1_str.join(sorted(pel1_7)) 
    teksti = fontti.render(f"Pelaaja 1:   {pel1_str} ", True, WHITE)
    pisteet = fontti_pieni.render(f"{pisteet_pel1}", True, GREEN)
    SCREEN.blit(teksti, (40, 26))
    SCREEN.blit(pisteet, (WINDOW_WIDTH - 51, 31))
    pel2_str = "  "
    pel2_str = pel2_str.join(sorted(pel2_7)) 
    teksti = fontti.render(f"Pelaaja 2:   {pel2_str}", True, WHITE)
    pisteet = fontti_pieni.render(f"{pisteet_pel2}", True, GREEN)
    SCREEN.blit(teksti, (40, WINDOW_HEIGHT - 50))
    SCREEN.blit(pisteet, (WINDOW_WIDTH - 51, WINDOW_HEIGHT - 46))

    # näppäinkomennot:
    fontti_pieni = pygame.font.SysFont("FreeMono", 17, bold=True)
    nappaink = fontti_pieni.render(f"F2 = UNDO   ENTER = VUORONVAIHTO   V = KIRJAIMENVAIHTO   L = LOPETUS", True, YELLOW)
    SCREEN.blit(nappaink, (40, 2))

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

def minne_kirjain(x, y, kirjain):  
    global vuoro
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
        # ei saa laittaa kahta samaa omaa kirjainta päällekkäin
        if ruudukko[y_indeksi][x_indeksi] == kirjain :
            print(" if ruudukko[y_indeksi][x_indeksi] == kirjain")
            vuoro -= 2
            # TODO nappi pois laudalta pelaajalle takaisin
            return False   
        else:
            kerrokset[x_indeksi, y_indeksi] += 1   
            ruudukko[y_indeksi][x_indeksi] = kirjain        

    edelliset_muuvit.append([x_indeksi, y_indeksi])
    kaikki_muuvit_talteen.append(copy.deepcopy(ruudukko))
    return True
    
def tutki_mouse(x, y, kirjain):
    global edelliset_muuvit, ruudukko, vuoro
    kirjain_ind = -1

    # pelaaja 1
    if vuoro % 4 == 1 or vuoro % 4 == 2:
        if y < blockSize:    
            kirjain_ind = mika_kirjain(x)
            kirjain = sorted(pel1_7)[kirjain_ind]  
    
        elif y >= blockSize and y <= WINDOW_HEIGHT - blockSize:                
            if minne_kirjain(x, y, kirjain):   # False jos kerroksia jo 5  / 2 samaa omaa pääl. 
 # TODO jos oli kaksi J:tä ja yritti vaihtaa paikkaa, poistui molemmat J:t
                if kirjain in pel1_7:            
                    kirjaimet_yhdensiirronajalta.append(kirjain)
                    pel1_7.remove(kirjain)                   
                    print(sorted(edelliset_muuvit))         
                elif len(edelliset_muuvit) > 1:      
                    ruudukko = undo()  
                    ruudukko = undo()  
                    minne_kirjain(x, y, kirjain)
            # laiton siirto:
            else:
                for k in kirjaimet_yhdensiirronajalta:
                    pel1_7.append(k)
                    if len(edelliset_muuvit) > 0:  
                        ruudukko = undo() 
                vuoro -= 2
    
    # pelaaja 2
    elif vuoro % 4 == 3 or vuoro % 4 == 0:
        if y > WINDOW_HEIGHT - blockSize:        
            kirjain_ind = mika_kirjain(x)
            kirjain = sorted(pel2_7)[kirjain_ind]

        elif y >= blockSize and y <= WINDOW_HEIGHT - blockSize:    
            if minne_kirjain(x, y, kirjain):
                if kirjain in pel2_7:        
                    kirjaimet_yhdensiirronajalta.append(kirjain)
                    pel2_7.remove(kirjain)
                    print(sorted(edelliset_muuvit))    
                elif len(edelliset_muuvit) > 1:  
                    ruudukko = undo()  
                    ruudukko = undo()  
                    minne_kirjain(x, y, kirjain)   
            # laiton siirto:
            else:
                for k in kirjaimet_yhdensiirronajalta:
                    pel2_7.append(k)
                    if len(edelliset_muuvit) > 0:  
                        ruudukko = undo() 
                vuoro -= 2      

    return kirjain, kirjain_ind
    

def tutki_edelliset_muuvit_vaaka(edelliset_muuvit):    
    tuplapisteet = True
    pisteet_tama_kierros = 0
    x_t = [x for x, y in edelliset_muuvit]
    y_t = [y for x, y in edelliset_muuvit]
    sanan_pituus = x_t[-1] - x_t[0] + 1    # itse laitetut napit !!!!
    
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
        if kerrokset[x, y_t[0]] > 1:
           tuplapisteet = False 

    # tutkitaan vaakasuorassa sanan reunat      
    # ei voi laittaa:  if not x_t[0] == x_t[-1]: sanan vikaksi T --> sanan_pituus jää 1:ksi
    x = x_t[0]
    while x > 0:
        if not ruudukko[y_t[0]][x - 1] == "":
            if kerrokset[x -1, y_t[0]] > 1 :   # 2 pistettä pohjakerroksesta, jos sana kokonaan 1-kerroksinen
                tuplapisteet = False
            pisteet_tama_kierros += kerrokset[x -1, y_t[0]]
            sanan_pituus += 1
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
            x += 1
        else:
            break 

    if sanan_pituus == 1:
        return 0      
    if tuplapisteet:
        pisteet_tama_kierros *= 2    
     
    return pisteet_tama_kierros

def tutki_vaaka_additional(x_orig, y):  
    tuplapisteet = True
    pisteet_tama_kierros = 0
    x = x_orig
    while x > 0:
        if not ruudukko[y][x - 1] == "":
            pisteet_tama_kierros += kerrokset[x - 1, y]
            if kerrokset[x - 1, y] > 1 :   # 2 pistettä pohjakerroksesta
                tuplapisteet = False
            x -= 1 
        else:
            break
    x = x_orig
    while x < kirjainten_lkm - 1 :
        if not ruudukko[y][x + 1] == "":
            pisteet_tama_kierros += kerrokset[x + 1, y]
            if kerrokset[x + 1, y] > 1 :   # 2 pistettä pohjakerroksesta
                tuplapisteet = False
            x += 1    
        else:
            if pisteet_tama_kierros > 0:
                pisteet_tama_kierros += kerrokset[x_orig, y]
                if kerrokset[x_orig, y] > 1 :   # 2 pistettä pohjakerroksesta
                    tuplapisteet = False
            break

    if tuplapisteet:
        pisteet_tama_kierros *= 2    
    return pisteet_tama_kierros

def tutki_pysty_additional(x, y_orig):     
    tuplapisteet = True
    pisteet_tama_kierros = 0
    y = y_orig
    while y > 0:
        if not ruudukko[y - 1][x] == "":
            pisteet_tama_kierros += kerrokset[x, y - 1]
            if kerrokset[x, y - 1] > 1 :   # 2 pistettä pohjakerroksesta
                tuplapisteet = False
            y -= 1 
        else:
            break
    y = y_orig
    while y < kirjainten_lkm - 1:
        if not ruudukko[y + 1][x] == "":
            pisteet_tama_kierros += kerrokset[x, y + 1]
            if kerrokset[x, y + 1] > 1 :   # 2 pistettä pohjakerroksesta
                tuplapisteet = False
            y += 1    
        else:
            if pisteet_tama_kierros > 0:
                pisteet_tama_kierros += kerrokset[x, y_orig]
                if kerrokset[x, y_orig] > 1 :   # 2 pistettä pohjakerroksesta
                    tuplapisteet = False
            break

    if tuplapisteet:
        pisteet_tama_kierros *= 2    
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
        pisteet_tama_kierros += kerrokset[x_t[0], y]   # kaikilla sama x
        if kerrokset[x_t[0], y] > 1:
           tuplapisteet = False 
    
    # tutkitaan pystysuorassa sanan reunat
    y = y_t[0]
    while y > 0:
        if not ruudukko[y -1][x_t[0]] == "":
            if kerrokset[x_t[0], y -1] > 1 :   # 2 pistettä pohjakerroksesta, jos sana kokonaan 1-kerroksinen
                tuplapisteet = False
            pisteet_tama_kierros += kerrokset[x_t[0], y -1]
            sanan_pituus += 1
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
            y += 1 
        else:
            break
        
    if sanan_pituus == 1:   
        return 0
    if tuplapisteet:
        pisteet_tama_kierros *= 2        
    return pisteet_tama_kierros

def vaihda_nappi(kirjain):    
    global vuoro        
    pyorii = True
    valitus = ""
    while pyorii:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN: 
                x = event.pos[0]
                y = event.pos[1]                  
                kirjain, kirjain_ind = tutki_mouse(x, y, kirjain)  
                if vuoro % 4 == 1 or vuoro % 4 == 2:
                    if y > WINDOW_HEIGHT - blockSize:
                        valitus = "Voit vaihtaa vain yhden napin, nyt on Pelaaja1:n vuoro"
                    else:                            
                        pel1_7.remove(kirjain)   
                        pel1_7.append(uusi_nappi())
                        vuoro += 2  # vuoro hyppäää ruudukko"tilan" yli
                else:
                    if y < blockSize:
                        valitus = "Voit vaihtaa vain yhden napin, nyt on Pelaaja2:n vuoro"
                    else:    
                        pel2_7.remove(kirjain) 
                        pel2_7.append(uusi_nappi())
                        vuoro += 2  # vuoro hyppäää ruudukko"tilan" yli
                pyorii = False
        CLOCK.tick(8000)    
           
    return kirjain, valitus   

def laitetut_laittomat_napit_pois():
    global kaikki_muuvit_talteen
    kaikki_muuvit_talteen = copy.deepcopy(kaikki_muuvit_talteen[:-(len(edelliset_muuvit))])
    uusi_ruudukko = copy.deepcopy(kaikki_muuvit_talteen[-1]) 
    for x, y in edelliset_muuvit:
        kerrokset[x, y] -= 1
    return uusi_ruudukko

def lopputeksti(vuoro):   # vuoro voi olla myös -1, jos painettiin "L"
    global pisteet_pel1, pisteet_pel2

    # käyttämättöät napit
    pisteet_pel1 -= len(pel1_7) * 5
    pisteet_pel2 -= len(pel1_7) * 5            

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

def pelaaja_1(fontti):
    global ruudukko, pisteet_pel1, kirjaimet_yhdensiirronajalta, vuoro
    valitus = fontti.render(f"", True, YELLOW)
    #oikeellisuus:
    if oikeellisuus.tarkista(ruudukko, sorted(edelliset_muuvit)):   # laittomasta siirrosta ei pisteitä
        y_t = [y for x, y in edelliset_muuvit]
        x_t = [x for x, y in edelliset_muuvit]
        # pelaaja1, vaaka pitkä, pysty vain additional : 
        if y_t[0] == y_t[-1]:
            pisteet_pel1 += tutki_edelliset_muuvit_vaaka(sorted(edelliset_muuvit))
            print("tutki_edelliset_muuvit_vaaka", pisteet_pel1 )
            if len(y_t) == 1:
                pisteet_pel1 += tutki_edelliset_muuvit_pysty(sorted(edelliset_muuvit))
                print("tutki_edelliset_muuvit_pysty", pisteet_pel1 )
            else:
                for muuvi in edelliset_muuvit:   
                    pisteet_pel1 += tutki_pysty_additional(muuvi[0], muuvi[1])   # x, y     
                print("tutki_pysty_additional", pisteet_pel1)                         
        
        # pelaaja1, pysty pitkä, vaaka vain additional
        else:
            pisteet_pel1 += tutki_edelliset_muuvit_pysty(sorted(edelliset_muuvit))
            print("tutki_edelliset_muuvit_pysty", pisteet_pel1 )
            if len(x_t) == 1:
                pisteet_pel1 += tutki_edelliset_muuvit_vaaka(sorted(edelliset_muuvit))
                print("tutki_edelliset_muuvit_vaaka", pisteet_pel1 )
            else:
                for muuvi in edelliset_muuvit:   
                    pisteet_pel1 += tutki_vaaka_additional(muuvi[0], muuvi[1])   # x, y     
                    print("tutki_vaaka_additional", pisteet_pel1) 

        # erikoisnapit, pelaaja 1
        for kirjain in kirjaimet_yhdensiirronajalta:
            if kirjain in kahden_pisteen_kirjaimet: 
                pisteet_pel1 += 2 

        # uudet napit
        print("edelliset_muuvit", edelliset_muuvit)
        for muuvi in edelliset_muuvit:                                                   
            if len(aakkoset) > 0:
                pel1_7.append(uusi_nappi())

    else: # laiton siirto 
        for kirjain in kirjaimet_yhdensiirronajalta:   
            pel1_7.append(kirjain)
        valitus = fontti.render(oikeellisuus.syy, True, YELLOW)
        ruudukko = laitetut_laittomat_napit_pois()
        vuoro -= 2

    return valitus

def pelaaja_2(fontti):
    global ruudukko, pisteet_pel2, vuoro, kirjaimet_yhdensiirronajalta
    valitus = fontti.render(f"", True, YELLOW)
    #oikeellisuus:
    if oikeellisuus.tarkista(ruudukko, sorted(edelliset_muuvit)):   # laittomasta siirrosta ei pisteitä
        y_t = [y for x, y in edelliset_muuvit]
        x_t = [x for x, y in edelliset_muuvit]
        # pelaaja1, vaaka pitkä, pysty vain additional : 
        if y_t[0] == y_t[-1]:
            pisteet_pel2 += tutki_edelliset_muuvit_vaaka(sorted(edelliset_muuvit))
            print("tutki_edelliset_muuvit_vaaka", pisteet_pel2 )
            if len(y_t) == 1:
                pisteet_pel2 += tutki_edelliset_muuvit_pysty(sorted(edelliset_muuvit))
                print("tutki_edelliset_muuvit_pysty", pisteet_pel2 )
            else:
                for muuvi in edelliset_muuvit:   
                    pisteet_pel2 += tutki_pysty_additional(muuvi[0], muuvi[1])   # x, y     
                print("tutki_pysty_additional", pisteet_pel2)                         
        
        # pelaaja1, pysty pitkä, vaaka vain additional
        else:
            pisteet_pel2 += tutki_edelliset_muuvit_pysty(sorted(edelliset_muuvit))
            print("tutki_edelliset_muuvit_pysty", pisteet_pel2 )
            if len(x_t) == 1:
                pisteet_pel2 += tutki_edelliset_muuvit_vaaka(sorted(edelliset_muuvit))
                print("tutki_edelliset_muuvit_vaaka", pisteet_pel2 )
            else:
                for muuvi in edelliset_muuvit:   
                    pisteet_pel2 += tutki_vaaka_additional(muuvi[0], muuvi[1])   # x, y     
                    print("tutki_vaaka_additional", pisteet_pel2)  

        # erikoisnapit, pelaaja 2
        for kirjain in kirjaimet_yhdensiirronajalta:
            if kirjain in kahden_pisteen_kirjaimet: 
                pisteet_pel2 += 2  

        # uudet napit
        for muuvi in edelliset_muuvit:
            if len(aakkoset) > 0:
                pel2_7.append(uusi_nappi())    
            
    else: # laiton siirto
        for kirjain in kirjaimet_yhdensiirronajalta:   
            pel2_7.append(kirjain)
        valitus = fontti.render(oikeellisuus.syy, True, YELLOW)
        ruudukko = laitetut_laittomat_napit_pois()
        vuoro -= 2   # oma vuoro pysyy, RETURN = +2, evens out

    return valitus

def undo():
    global kaikki_muuvit_talteen, edelliset_muuvit, kirjaimet_yhdensiirronajalta
    kaikki_muuvit_talteen = copy.deepcopy(kaikki_muuvit_talteen[:-1])
    tokavika = copy.deepcopy(kaikki_muuvit_talteen[-1]) 
    kirjaimet_yhdensiirronajalta = copy.deepcopy(kirjaimet_yhdensiirronajalta[:-1])
    x, y = edelliset_muuvit[-1]
    kerrokset[x, y] -= 1
    edelliset_muuvit = copy.deepcopy(edelliset_muuvit[:-1])
    return tokavika


def main():
    pygame.init()    
    
    kirjain = ""
    fontti = pygame.font.SysFont("Arial", 26)
    valitus = fontti.render(f"", True, GREEN)
    kirjain_ind = -1    
    global edelliset_muuvit, pisteet_pel1, pisteet_pel2, ruudukko, vuoro, kirjaimet_yhdensiirronajalta

    

    while (len(pel1_7) > 0 or len(pel2_7) > 0) or len(aakkoset) > 0:   
        SCREEN.fill(BLACK)
        drawGrid()
        tekstit()          
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN: 
                x = event.pos[0]
                y = event.pos[1]                  
                kirjain, kirjain_ind = tutki_mouse(x, y, kirjain)  
            
            if event.type == pygame.KEYDOWN:
                #undo  
                if event.key == pygame.K_F2:    
                    if len(edelliset_muuvit) > 0:                   
                        x, y = edelliset_muuvit[-1]                    
                        if (vuoro % 4 == 1 or vuoro % 4 == 2): 
                            pel1_7.append(ruudukko[y][x])
                        else:
                            pel2_7.append(ruudukko[y][x])
                        ruudukko = undo()  

                # ENTER = vuoronvaihto
                if event.key == pygame.K_RETURN:
                    if (vuoro % 4 == 1 or vuoro % 4 == 2) and len(edelliset_muuvit) > 0:  
                        if len(edelliset_muuvit) == 7:   # laitettiin kaikki napit     
                            pisteet_pel1  += 15              
                        valitus = pelaaja_1(fontti)   
                    elif len(edelliset_muuvit) > 0:  
                        if len(edelliset_muuvit) == 7:   # laitettiin kaikki napit     
                            pisteet_pel2  += 15      
                        valitus = pelaaja_2(fontti)  
                    vuoro += 2
                    edelliset_muuvit = []
                    kirjaimet_yhdensiirronajalta = []

                #vaihda nappi
                if chr(event.key) == "v":
                    if len(aakkoset) > 0:                        
                        kirjain, valivali = vaihda_nappi(kirjain)   
                        while not valivali == "":                            
                            valitus = fontti.render(valivali, True, YELLOW)
                            SCREEN.blit(valitus, (30, 71))     
                            pygame.display.flip()
                            kirjain, valivali = vaihda_nappi(kirjain) 
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
        SCREEN.blit(valitus, (30, 71))      

        CLOCK.tick(8000)   
        pygame.display.flip()
            
    # peli loppuu siihen että pelaajan napit loppu ennenkuin ehtii painaa ENTER
    if (vuoro % 4 == 1 or vuoro % 4 == 2) and len(edelliset_muuvit) > 0:                        
        pelaaja_1(fontti)   
    elif len(edelliset_muuvit) > 0:    
        pelaaja_2(fontti)  
    lopputeksti(vuoro)
        

jaa_napit_aloitus()    
alusta_ruudukko() 
main()