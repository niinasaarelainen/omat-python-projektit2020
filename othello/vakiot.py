import pygame

WIDTH = 630
HEIGHT = 690
REUNAN_KOKO = 12
RUUDUN_KOKO = WIDTH // 8
P_KOKO = 23

lauta = pygame.image.load('lauta.png')
kello = pygame.time.Clock()

PUNAINEN = [(190, 7, 7), "punainen"]
SININEN = [(7, 7, 190), "sininen"]



def alkuohjeet():
    ohjeet = []
    ohjeet.append("Pelaat vuorotellen punaista ja sinistä.")
    ohjeet.append("Klikkaa hiirellä haluamaasi paikkaa")

    return ohjeet