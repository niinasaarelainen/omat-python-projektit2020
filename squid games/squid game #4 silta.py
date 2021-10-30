import pygame, random
from mixer import *


class Robo:

    def __init__(self, offset, monesko):
        self.x = 20 + offset
        self.y = 80
        self.voitto = False
        self.pic = pygame.image.load("robo.png")
        self.monesko  = monesko
        

    def liiku(self, x, y):
        self.x = x
        self.y = y


pygame.init()
LEVEYS =  1111
KORKEUS = 250
naytto = pygame.display.set_mode((LEVEYS, KORKEUS))
pygame.display.set_caption("Squid Game #4  Bridge")

silta = []  # 15 kpl True/False
robot = []



def rakenna_robot():
    offset = 0
    for i in range(9):
        robot.append(Robo(offset, abs(i - 9)))
        offset += 12


def rakenna_silta():
    for i in range(15):
        r = random.randint(0, 1)  
        if r == 0:
            silta.append(False)
        else:
            silta.append(True)


def piirra_silta():
    rect_leveys = 35
    rect_pituus = 45
    x = 170
    y = 70
    for i in range(15):
        pygame.draw.rect(naytto, BLUE, pygame.Rect(x, y, rect_pituus, rect_leveys))
        x += 55
    x = 170
    y = 170
    for i in range(15):
        pygame.draw.rect(naytto, BLUE, pygame.Rect(x, y, rect_pituus, rect_leveys))
        x += 55  

def main():
    # textsurface = myfont.render(f"{sec}", True, (100, 30, 30))  
    #mixer.music.play()
    x = 110
    y = 80
    robo_nro = 0

    while True:
        naytto.fill(BLACK)
        
        piirra_silta()
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()    
                mixer.music.stop()    

            elif tapahtuma.type == pygame.MOUSEBUTTONDOWN :
                x, y = tapahtuma.pos   
                for robo in robot:
                    if robo.monesko = robo_nro:
                        robo.liiku(x, y)

            elif tapahtuma.type == pygame.KEYDOWN:
                robo_nro = tapahtuma.key - 48
  
        
                    
        for robo in robot:
            naytto.blit(robo.pic, (robo.x, robo.y))  
            textsurface = myfont.render(f"{robo.monesko}", True, (0, 30, 30))  
            naytto.blit(textsurface, (robo.x + 20, robo.y + 35))               
        #        lopetus('H Ä V I S I T !!!', robo_broken)
        # textsurface = myfont.render(f"{sec}", True, (100, 30, 30)) 
        #naytto.blit(textsurface, (320, 20))  
        pygame.display.flip()          
        kello.tick(60)


def lopetus(teksti, kuva):
    textsurface = myfont.render(teksti, True, (100, 30, 30))
    mixer.music.pause()  
    
    while True:
        naytto.fill((255, 255, 255))        
        naytto.blit(textsurface, (20, 100))    
        naytto.blit(kuva, (510, 10))        
        

        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()    
                
            elif tapahtuma.type == pygame.MOUSEBUTTONDOWN :
                x, y = tapahtuma.pos

        pygame.display.flip()
        kello.tick(70)



y = KORKEUS - 100
BLACK = (0, 0, 0)
BLUE = (0, 0, 210)

kello = pygame.time.Clock()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 20)

rakenna_silta()
rakenna_robot()
main()
#lopetus('V O I T I T !!!', robo_win)
#lopetus('H Ä V I S I T !!!', robo_broken)