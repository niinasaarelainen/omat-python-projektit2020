import pygame, random

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 840
WINDOW_WIDTH = 700

SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CLOCK = pygame.time.Clock()
blockSize = 70 #Set the size of the grid block
kirjainten_lkm = 10
kirjainvali = 57

#aakkoset = list("AAAAABDEEEFGHHHIIIIIIIIIJJJKKKKKLLLLLMMMMNNNOOOOOOPPRRRSSSSTTTTUUUUUUUUVVVVVYYYÄÄÄÄÄÄÖÖÖÖ")
aakkoset = list("AAABDEEEFGHHIIIKLM")
pel1_7 = []
pel2_7 = []
ruudukko = []
kerrokset = {}


def jaa_napit_aloitus():
    for i in range(7):
        pel1_7.append(uusi_nappi())
        pel2_7.append(uusi_nappi())
    
def alusta_ruudukko():
    for rivi in range(kirjainten_lkm):
        ruudukko.append([])
        for sarake in range(kirjainten_lkm):
            ruudukko[rivi].append("")       


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
        rect = pygame.Rect(15, 30, blockSize // 4, blockSize // 4)
    else:
        rect = pygame.Rect(15, WINDOW_HEIGHT - 40, blockSize // 4, blockSize // 4)
    pygame.draw.rect(SCREEN, WHITE, rect, 0)    # 0 = kokovalkoinen

    fontti = pygame.font.SysFont("FreeMono", 32)
    pel1_str = "  "
    pel1_str = pel1_str.join(sorted(pel1_7)) 
    teksti = fontti.render(f"Pelaaja 1:   {pel1_str}", True, WHITE)
    SCREEN.blit(teksti, (40, 20))

    pel2_str = "  "
    pel2_str = pel2_str.join(sorted(pel2_7)) 
    teksti = fontti.render(f"Pelaaja 2:   {pel2_str}", True, WHITE)
    SCREEN.blit(teksti, (40, WINDOW_HEIGHT - 50))

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
    return True
    

def tutki_mouse(x, y, vuoro, kirjain):
    kirjain_ind = -1
    if vuoro % 4 == 1 and y < blockSize:
        kirjain_ind = mika_kirjain(x)
        kirjain = sorted(pel1_7)[kirjain_ind]             
  
    elif vuoro % 4 == 2 and y >= blockSize and y <= WINDOW_HEIGHT - blockSize:
        if minne_kirjain(x, y, kirjain):
            pel1_7.remove(kirjain)
        if len(aakkoset) > 0:
            pel1_7.append(uusi_nappi())

    elif vuoro % 4 == 3 and y > WINDOW_HEIGHT - blockSize:
        kirjain_ind = mika_kirjain(x)
        kirjain = sorted(pel2_7)[kirjain_ind]

    elif vuoro % 4 == 0 and y >= blockSize and y <= WINDOW_HEIGHT - blockSize:
        if minne_kirjain(x, y, kirjain):
            pel2_7.remove(kirjain)
        if len(aakkoset) > 0:
            pel2_7.append(uusi_nappi())
    return kirjain, kirjain_ind


def main():
    pygame.init()    
    
    vuoro = 1
    kirjain = ""
    kirjain_ind = -1

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
                kirjain, kirjain_ind = tutki_mouse(x, y, vuoro, kirjain)               
                vuoro += 1
        
        if kirjain_ind > 0 and (vuoro % 4 == 1 or vuoro % 4 == 2):   #   -1 = ei tarvitse neliöidä
            rect = pygame.Rect(278 + kirjain_ind * kirjainvali , 19, blockSize // 2, blockSize // 2)
            pygame.draw.rect(SCREEN, WHITE, rect, 2)
        elif kirjain_ind > 0 and (vuoro % 4 == 3 or vuoro % 4 == 0):
            rect = pygame.Rect(278 + kirjain_ind * kirjainvali , WINDOW_HEIGHT - 50, blockSize // 2, blockSize // 2)
            pygame.draw.rect(SCREEN, WHITE, rect, 2)
        CLOCK.tick(1000)   
        pygame.display.flip()
            
        
    print("napit lopussa")

        
        

jaa_napit_aloitus()    
alusta_ruudukko() 
main()