import pygame, random

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 840
WINDOW_WIDTH = 700

SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CLOCK = pygame.time.Clock()
blockSize = 70 #Set the size of the grid block

#aakkoset = list("AAAAABDEEEFGHHHIIIIIIIIIJJJKKKKKLLLLLMMMMNNNOOOOOOPPRRRSSSSTTTTUUUUUUUUVVVVVYYYÄÄÄÄÄÄÖÖÖÖ")
aakkoset = list("AAABDEEEFGHHIIIKLM")
pel1_7 = []
pel2_7 = []



def jaa_napit_aloitus():
    for i in range(7):
        pel1_7.append(uusi_nappi())
    for i in range(7):
        pel2_7.append(uusi_nappi())


def uusi_nappi():    
    r = random.randint(0, len(aakkoset) - 1)    
    valittu = aakkoset[r]
    aakkoset.remove(valittu)
    return valittu


def drawGrid():    
    for x in range(10):
        for y in range(1,11):                 
            rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

def tekstit():
    fontti = pygame.font.SysFont("FreeMono", 32)
    pel1_str = "  "
    pel1_str = pel1_str.join(pel1_7) 
    teksti = fontti.render(f"Pelaaja 1:   {pel1_str}", True, WHITE)
    SCREEN.blit(teksti, (40, 20))

    pel2_str = "  "
    pel2_str = pel2_str.join(pel2_7) 
    teksti = fontti.render(f"Pelaaja 2:   {pel2_str}", True, WHITE)
    SCREEN.blit(teksti, (40, WINDOW_HEIGHT - 50))
    

def mika_kirjain(x):
    # 297, 353, 412, 466,  525, 580, 638    kirjainten keskipisteet
    kirjainvali = 57
    indeksi = 0
    for i in range(7):
        if x > 297 - (kirjainvali // 2) + i * kirjainvali:
            indeksi = i
    return indeksi
    

def tutki_mouse(x, y, vuoro):
    if vuoro % 4 == 1 and y < blockSize:
        kirjain = mika_kirjain(x)
        print(kirjain)
    elif vuoro % 4 == 2 and y >= blockSize and y <= WINDOW_HEIGHT - blockSize:
        print("1 pelitila")
    elif vuoro % 4 == 3 and y > WINDOW_HEIGHT - blockSize:
        kirjain = mika_kirjain(x)
        print(kirjain)
    elif vuoro % 4 == 0 and y >= blockSize and y <= WINDOW_HEIGHT - blockSize:
        print("2 pelitila")  


def main():
    pygame.init()    
    SCREEN.fill(BLACK)
    tekstit()
    vuoro = 1

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:   
                x = event.pos[0]
                y = event.pos[1]  
                tutki_mouse(x, y, vuoro)
                vuoro += 1
                """
                if vuoro % 2 == 1:   
                    vuoro = 2
                else:
                    vuoro = 1     
                """  
            CLOCK.tick(1000)   
            pygame.display.update()
            tekstit()
        
        """
        if len(aakkoset) > 0:
            if vuoro == 1:
                pel1_7.append(uusi_nappi())
                vuoro = 2
            elif vuoro == 2:
                pel2_7.append(uusi_nappi())
                vuoro = 1
        else:
            print("napit loppu")
        """

        
        

jaa_napit_aloitus()     
main()