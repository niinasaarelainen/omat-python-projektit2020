import pygame

WIDTH = 660
HEIGHT = 700
VALI = 10
P_KOKO = 22
OIKEIN_KOKO = 9
VALI_PIENEMPI = 7
X_ALOITUS = 160
Y_ALOITUS = 100

ok = pygame.image.load('ok.png')
naytto = pygame.display.set_mode((WIDTH, HEIGHT))
kello = pygame.time.Clock()


val = (252, 252, 252)  # vain bg
mus = (1, 1, 1)        # pallon ääriviivat
pun = (255, 0, 0)      # 6 peliväriä
sin = (0, 0, 255) 
kel = (222, 170, 0) 
vio = (200, 0, 200) 
vih = (0, 170, 96) 
rus = (120, 80, 33)

varit = [pun, sin, kel, vio, vih, rus]



def alkuohjeet():
    ohjeet = []
    ohjeet.append("Paina näppäintä 4, 5 tai 6")
    ohjeet.append("")
    ohjeet.append("    4  =  4 palloa")
    ohjeet.append("    5  =  5 palloa")
    ohjeet.append("    6  =  6 palloa")

    return ohjeet

