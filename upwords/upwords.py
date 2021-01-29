import pygame, random

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 840
WINDOW_WIDTH = 700

SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CLOCK = pygame.time.Clock()
blockSize = 70 #Set the size of the grid block
kirjainten_lkm = 10

#aakkoset = list("AAAAABDEEEFGHHHIIIIIIIIIJJJKKKKKLLLLLMMMMNNNOOOOOOPPRRRSSSSTTTTUUUUUUUUVVVVVYYYÄÄÄÄÄÄÖÖÖÖ")
aakkoset = list("AAABDEEEFGHHIIIKLM")
pel1_7 = []
pel2_7 = []
ruudukko = []


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
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

def tekstit():
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
    for rivi in range(kirjainten_lkm):
        for sarake in range(kirjainten_lkm):
            kirjain = ruudukko[rivi][sarake]
            if not kirjain == "":
                kirjain = fontti.render(kirjain, True, WHITE)
                SCREEN.blit(kirjain, ((sarake + 0.27) *blockSize , (rivi + 1.17) *blockSize))   
    

def mika_kirjain(x):
    # 297, 353, 412, 466, 525, 580, 638    kirjainten keskipisteet
    kirjainvali = 57
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
    ruudukko[y_indeksi][x_indeksi] = kirjain
    print(y_indeksi, x_indeksi, kirjain)
    print(ruudukko)
    

def tutki_mouse(x, y, vuoro, kirjain):
    kirjain_ind = ""
    if vuoro % 4 == 1 and y < blockSize:
        kirjain_ind = mika_kirjain(x)
        kirjain = sorted(pel1_7)[kirjain_ind]       
    elif vuoro % 4 == 2 and y >= blockSize and y <= WINDOW_HEIGHT - blockSize:
        minne_kirjain(x, y, kirjain)
        pel1_7.remove(kirjain)
        if len(aakkoset) > 0:
            pel1_7.append(uusi_nappi())

    elif vuoro % 4 == 3 and y > WINDOW_HEIGHT - blockSize:
        kirjain_ind = mika_kirjain(x)
        kirjain = sorted(pel2_7)[kirjain_ind]
    elif vuoro % 4 == 0 and y >= blockSize and y <= WINDOW_HEIGHT - blockSize:
        minne_kirjain(x, y, kirjain)
        pel2_7.remove(kirjain)
        if len(aakkoset) > 0:
            pel2_7.append(uusi_nappi())
    return kirjain


def main():
    pygame.init()    
    tekstit()
    vuoro = 1
    kirjain = ""

    while len(pel1_7) > 0 and len(pel2_7) > 0:        
        SCREEN.fill(BLACK)
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:   
                x = event.pos[0]
                y = event.pos[1]  
                kirjain = tutki_mouse(x, y, vuoro, kirjain)
                vuoro += 1
            CLOCK.tick(1000)   
            tekstit()
            pygame.display.flip()
            
        
    print("napit lopussa")

        
        

jaa_napit_aloitus()    
alusta_ruudukko() 
main()