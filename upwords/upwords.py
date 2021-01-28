import pygame, random

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 840
WINDOW_WIDTH = 700

SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CLOCK = pygame.time.Clock()

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
    blockSize = 70 #Set the size of the grid block
    for x in range(10):
        for y in range(1,11):                 
            rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

def tekstit():
    fontti = pygame.font.SysFont("Arial", 26)
    pel1_str = "   "
    pel1_str = pel1_str.join(pel1_7) 
    teksti = fontti.render(f"Pelaaja 1:      {pel1_str}", True, WHITE)
    SCREEN.blit(teksti, (100, 20))

    pel2_str = "   "
    pel2_str = pel2_str.join(pel2_7) 
    teksti = fontti.render(f"Pelaaja 2:      {pel2_str}", True, WHITE)
    SCREEN.blit(teksti, (100, WINDOW_HEIGHT - 50))


def main():
    pygame.init()    
    SCREEN.fill(BLACK)
    vuoro = 1
    tekstit()

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            CLOCK.tick(1000)   
            pygame.display.update()
            print("moi")
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