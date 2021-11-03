import pygame, random
from mixer import *


class Robo:

    def __init__(self, offset, monesko):

        self.x = 20 + offset
        self.y = 80
        self.voitto = True
        self.pic = pygame.image.load("robo.png")
        self.monesko  = monesko
        

    def liiku(self, x, y):
        self.x = x - 20    # jotta saadaan robotti keskemmäs hiiren sijaintia
        self.y = y - 80   
        self.ruutu = ((x - 170) // 55 ) * 2
        if y > 165 :  # alarivi
            self.ruutu += 1
        print(self.ruutu)


pygame.init()
LEVEYS =  1111
KORKEUS = 250
naytto = pygame.display.set_mode((LEVEYS, KORKEUS))
pygame.display.set_caption("Squid Game #4  Bridge")

robo_broken = pygame.image.load("robo_broken.png")
robo_broken = pygame.transform.scale(robo_broken, (150, 220))
robo_win = pygame.image.load("robo_win.png")
robo_win = pygame.transform.scale(robo_win, (180, 170))

RUUTUJA = 15
silta = []  # 15 kpl True/False
silta_rikki = []
robot = []
etummaisen_sijainti = 0    # maali = 15




def rakenna_robot():
    offset = 0
    for i in range(9):
        robot.append(Robo(offset, abs(i - 9)))
        offset += 12


def rakenna_silta():
    for i in range(RUUTUJA):
        r = random.randint(0, 1)  
        if r == 0:
            silta.append(False)                        
        else:
            silta.append(True)
        silta.append(not silta[-1])


def piirra_silta():
    rect_leveys = 35
    rect_pituus = 45
    x = 170
    y = 90
    for i in range(RUUTUJA):
        if i * 2 not in silta_rikki:
            pygame.draw.rect(naytto, BLUE, pygame.Rect(x, y, rect_pituus, rect_leveys))
        x += 55
    x = 170
    y = 170
    for i in range(RUUTUJA):
        if i * 2 + 1 not in silta_rikki:
            pygame.draw.rect(naytto, BLUE, pygame.Rect(x, y, rect_pituus, rect_leveys))
        x += 55  


def onko_laillinen(robo_nro, x):
    global etummaisen_sijainti
    yritetty_sijainti = ((x - 170) // 55 )   
    x = x - 20    # jotta saadaan robotti keskemmäs hiiren sijaintia
    if yritetty_sijainti > etummaisen_sijainti :    # TODO
        return False
    else:
        etummaisen_sijainti += 1
        return True



def main():
    global silta, robot, silta_rikki, etummaisen_sijainti
    x = 110
    y = 80
    robo_nro = 0
    silta = []  # 15 kpl True/False
    silta_rikki = []
    robot = []
    rakenna_silta()
    rakenna_robot()
    etummaisen_sijainti = 0 
    valitus = myfont.render(f" ", True, (0, 30, 30)) 

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
                    if robo.monesko == robo_nro and onko_laillinen(robo_nro, x):    
                        valitus = myfont.render(f" ", True, BLACK)                      
                        robo.liiku(x, y)
                        if robo.ruutu < 30:
                            if silta[robo.ruutu] == False:
                                robo.voitto = False
                                robot.remove(robo)
                                silta_rikki.append(robo.ruutu)
                        else:
                            lopetus('V O I T I T !!!', robo_win)
                    #laiton
                    else:
                        valitus = myfont.render(f"Saat siirtyä vain yhden ruudun eteenpäin", True, (220, 30, 30))  
                        

            elif tapahtuma.type == pygame.KEYDOWN:
                robo_nro = tapahtuma.key - 48
  
        
        if len(robot) == 0:
            lopetus('H Ä V I S I T !!!', robo_broken)          
        for robo in robot:
            naytto.blit(robo.pic, (robo.x, robo.y))  
            textsurface = myfont.render(f"{robo.monesko}", True, (0, 30, 30))  
            naytto.blit(textsurface, (robo.x + 20, robo.y + 35))  

        naytto.blit(valitus, (x + 50, 35))  
        pygame.display.flip()          
        kello.tick(60)


def lopetus(teksti, kuva):
    textsurface = myfont.render(teksti, True, (100, 30, 30))
    mixer.music.pause()  
    
    while True:
        naytto.fill((255, 255, 255))        
        naytto.blit(textsurface, (20, 100))   
        x = 0
        if len(robot) == 0:
            naytto.blit(kuva, (510, 10))    
        else:
            for robo in robot: 
                naytto.blit(kuva, (300 + x, 10))      
                x += 180  
        

        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                pygame.quit()    
                
            elif tapahtuma.type == pygame.MOUSEBUTTONDOWN :
                main()

        pygame.display.flip()
        kello.tick(70)


BLACK = (0, 0, 0)
BLUE = (0, 0, 210)

kello = pygame.time.Clock()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 20)


main()
