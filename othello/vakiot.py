import pygame

WIDTH = 630
HEIGHT = 690
REUNAN_KOKO = 10
RUUDUN_KOKO = WIDTH // 8

lauta = pygame.image.load('lauta.png')
naytto = pygame.display.set_mode((WIDTH, HEIGHT))
kello = pygame.time.Clock()

punainen = (190, 7, 7) 
sininen = (7, 7, 190) 



def alkuohjeet():
    ohjeet = []
    ohjeet.append("Pelaat vuorotellen punaista ja sinistä.")
    ohjeet.append("Klikkaa hiirellä haluamaasi paikkaa")

    return ohjeet