import pygame

WIDTH = 630
HEIGHT = 630
YLIN_KUULA_X = WIDTH // 2 -1
YLIN_KUULA_Y = 48
ALIN_KUULA_X = WIDTH // 2 -1
ALIN_KUULA_Y = HEIGHT - 63
VALI = 32
P_KOKO = 13
#KUULIA = 6

lauta = pygame.image.load('chinese_lauta.png')
naytto = pygame.display.set_mode((WIDTH, HEIGHT))
kello = pygame.time.Clock()

vihrea = (0, 170, 96) 
ruskea = (120, 80, 33) 


koordinaatit1_orig =  [(YLIN_KUULA_X, YLIN_KUULA_Y), 
 (YLIN_KUULA_X - 19, YLIN_KUULA_Y + VALI), (YLIN_KUULA_X + 19, YLIN_KUULA_Y + VALI),  
 (YLIN_KUULA_X - 38, YLIN_KUULA_Y + 2*VALI), (YLIN_KUULA_X, YLIN_KUULA_Y + 2*VALI), (YLIN_KUULA_X + 38, YLIN_KUULA_Y + 2*VALI),
 ]  

koordinaatit2_orig =  [(ALIN_KUULA_X, ALIN_KUULA_Y),
(ALIN_KUULA_X - 19, ALIN_KUULA_Y - VALI), (ALIN_KUULA_X + 19, ALIN_KUULA_Y - VALI),
(ALIN_KUULA_X - 38, ALIN_KUULA_Y - 2*VALI), (ALIN_KUULA_X, ALIN_KUULA_Y - 2*VALI), (ALIN_KUULA_X + 38, ALIN_KUULA_Y - 2*VALI),
]   


def kuulia_lisarivit(kuulia):
    if kuulia == 10 or kuulia == 15: # 4. rivi
        koordinaatit1_orig.append((YLIN_KUULA_X - 19-38, YLIN_KUULA_Y + 3*VALI))
        koordinaatit1_orig.append((YLIN_KUULA_X - 19, YLIN_KUULA_Y + 3*VALI))
        koordinaatit1_orig.append((YLIN_KUULA_X + 19, YLIN_KUULA_Y + 3*VALI)) 
        koordinaatit1_orig.append((YLIN_KUULA_X + 19+38, YLIN_KUULA_Y + 3*VALI))  

        koordinaatit2_orig.append((ALIN_KUULA_X - 19-38, ALIN_KUULA_Y - 3*VALI))
        koordinaatit2_orig.append((ALIN_KUULA_X - 19, ALIN_KUULA_Y - 3*VALI))
        koordinaatit2_orig.append((ALIN_KUULA_X + 19, ALIN_KUULA_Y - 3*VALI))
        koordinaatit2_orig.append((ALIN_KUULA_X + 19+38, ALIN_KUULA_Y - 3*VALI))  

    if kuulia == 15: # 5. rivi
        koordinaatit1_orig.append((YLIN_KUULA_X - 38-38, YLIN_KUULA_Y + 4*VALI)) 
        koordinaatit1_orig.append((YLIN_KUULA_X - 38, YLIN_KUULA_Y + 4*VALI)) 
        koordinaatit1_orig.append((YLIN_KUULA_X, YLIN_KUULA_Y + 4*VALI)) 
        koordinaatit1_orig.append((YLIN_KUULA_X + 38, YLIN_KUULA_Y + 4*VALI))
        koordinaatit1_orig.append((YLIN_KUULA_X + 38 +38, YLIN_KUULA_Y + 4*VALI))

        koordinaatit2_orig.append((ALIN_KUULA_X - 38-38, ALIN_KUULA_Y - 4*VALI)) 
        koordinaatit2_orig.append((ALIN_KUULA_X - 38, ALIN_KUULA_Y - 4*VALI)) 
        koordinaatit2_orig.append((ALIN_KUULA_X, ALIN_KUULA_Y - 4*VALI)) 
        koordinaatit2_orig.append((ALIN_KUULA_X + 38, ALIN_KUULA_Y - 4*VALI))
        koordinaatit2_orig.append((ALIN_KUULA_X + 38 +38, ALIN_KUULA_Y - 4*VALI))




def alkuohjeet():
    ohjeet = []
    ohjeet.append("Paina näppäintä 1, 2 tai 3")
    ohjeet.append("")
    ohjeet.append("   1 =  6 kuulaa per pelaaja")
    ohjeet.append("   2 = 10 kuulaa per pelaaja")
    ohjeet.append("   3 = 15 kuulaa per pelaaja")

    return ohjeet