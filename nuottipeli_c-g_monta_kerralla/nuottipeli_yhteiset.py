import pygame

WIDTH = 790
HEIGHT = 410
VIIVASTON_ALKU_X = 50
VIIVOJEN_VALI = 50
YLIN_VIIVA_Y = 100      
ALIN_NUOTTI_Y = 350     
KUVAN_KOKO = 50
JESS_NO_AIKARAJA = 60   # 60 x mainin kesto    

naytto = pygame.display.set_mode((WIDTH, HEIGHT))
kello = pygame.time.Clock()

tumma = (25, 25, 25)
turkoosi = (0, 205, 205)
punainen = (255, 0, 0)
keltainen = (255, 255, 0)

K_c = pygame.K_c
K_d = pygame.K_d
K_e = pygame.K_e
K_f = pygame.K_f
K_g = pygame.K_g
nappaimet = [K_c, K_d, K_e, K_f, K_g]