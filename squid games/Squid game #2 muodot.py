import pygame, math
from datetime import datetime



pygame.init()
WIDTH = 400
HEIGHT = 400
naytto = pygame.display.set_mode((WIDTH, HEIGHT))
keskus = (int(WIDTH/2), int(HEIGHT/2))
sisainen_kello = pygame.time.Clock()

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 40)



def voittoko():
    for x in range(WIDTH):
        for y in range(HEIGHT):
            color = naytto.get_at((x, y))
            if color != (0, 0, 0, 255):
                return False
    return True
        

def main():
    klikkaukset = []
    while True:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()
            
            elif tapahtuma.type == pygame.MOUSEBUTTONDOWN :
                x, y = tapahtuma.pos
                klikkaukset.append((x, y))
                color = naytto.get_at(pygame.mouse.get_pos())
                if color != (255, 0, 0, 255):
                    lopetus("Et osaa leikata. Kuolit !!. Click = Uusi peli")

            
        naytto.fill((0, 0, 0)) 
        pygame.draw.circle(naytto, (255, 0, 0), keskus, 100)
        pygame.draw.circle(naytto, (0, 0, 0), keskus, 97)

        for klikkaus in klikkaukset:
            pygame.draw.circle(naytto, (0, 0, 0), klikkaus, 15)

        if voittoko():
            lopetus("Mahtavuutta. Voitit !!!! Click = Uusi peli")
                    
        pygame.display.flip()     
        sisainen_kello.tick(10)


def lopetus(teksti):
    splitted = teksti.split(".") 
    
    while True:
        naytto.fill((255, 255, 255))   

        y = 100
        for rivi in splitted:
            rivi = myfont.render(rivi, True, (100, 30, 30))     
            naytto.blit(rivi, (20, y))  
            y += 50

        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()    
                
            elif tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                main()

        pygame.display.flip()
        sisainen_kello.tick(70)

    
main()

