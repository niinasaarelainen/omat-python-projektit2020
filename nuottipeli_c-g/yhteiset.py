import pygame

WIDTH = 810
HEIGHT = 410
NUOTTIAV_SIJAINTI = 111
VIIVOJEN_VALI = 50
YLIN_VIIVA_Y = 100      # y-koordinaatti
ALIN_NUOTTI_Y = 350     # keski-c:n y-koordinaatti
PALLON_KOKO = int(VIIVOJEN_VALI / 2)

naytto = pygame.display.set_mode((WIDTH, HEIGHT))
kello = pygame.time.Clock()

g_avain = pygame.image.load('img\g_avain.png').convert_alpha()
g_avain= pygame.transform.scale(g_avain, (117, 355))            # resize = scale

valkoinen = (255, 255, 255)
musta = (0, 0, 0)
turkoosi = (0, 205, 205)
punainen = (255, 0, 0)





