import pygame

WIDTH = 810
HEIGHT = 410
NUOTTIAV_SIJAINTI = 122
VIIVOJEN_VALI = 50
YLIN_VIIVA = 100
PALLON_KOKO = 24

naytto = pygame.display.set_mode((WIDTH, HEIGHT))
kello = pygame.time.Clock()


g_avain = pygame.image.load('img\g_avain.png').convert_alpha()
g_avain= pygame.transform.scale(g_avain, (115, 355))            # resize = scale

valkoinen = (255, 255, 255)
musta = (0, 0, 0)
turkoosi = (0, 205, 205)
punainen = (255, 0, 0)


def nuottiviivasto(viivan_pit):
    for i in range(5):
        pygame.draw.line(naytto, (0, 0, 0), (NUOTTIAV_SIJAINTI, YLIN_VIIVA + i * VIIVOJEN_VALI), (viivan_pit - 15, YLIN_VIIVA + i * VIIVOJEN_VALI), 4)


