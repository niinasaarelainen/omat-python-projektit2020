import pygame, random
from noppa import *



def nopat_listaan():
    KUVAN_KOKO = 70

    d1 = pygame.image.load('img\d1.png').convert_alpha()
    d1= pygame.transform.scale(d1, (KUVAN_KOKO, KUVAN_KOKO) )

    d2 = pygame.image.load('img\d2.png').convert_alpha()
    d2= pygame.transform.scale(d2, (KUVAN_KOKO, KUVAN_KOKO) )

    d3 = pygame.image.load('img\d3.png').convert_alpha()
    d3= pygame.transform.scale(d3, (KUVAN_KOKO, KUVAN_KOKO) )

    d4 = pygame.image.load('img\d4.png').convert_alpha()
    d4= pygame.transform.scale(d4, (KUVAN_KOKO, KUVAN_KOKO) )

    d5 = pygame.image.load('img\d5.png').convert_alpha()
    d5= pygame.transform.scale(d5, (KUVAN_KOKO, KUVAN_KOKO) )

    d6 = pygame.image.load('img\d6.png').convert_alpha()
    d6= pygame.transform.scale(d6, (KUVAN_KOKO, KUVAN_KOKO) )

    d1_valittu = pygame.image.load('img\d1_valittu.png').convert_alpha()
    d1_valittu= pygame.transform.scale(d1_valittu, (KUVAN_KOKO, KUVAN_KOKO) )

    d2_valittu = pygame.image.load('img\d2_valittu.png').convert_alpha()
    d2_valittu= pygame.transform.scale(d2_valittu, (KUVAN_KOKO, KUVAN_KOKO) )

    d3_valittu = pygame.image.load('img\d3_valittu.png').convert_alpha()
    d3_valittu= pygame.transform.scale(d3_valittu, (KUVAN_KOKO, KUVAN_KOKO) )

    d4_valittu = pygame.image.load('img\d4_valittu.png').convert_alpha()
    d4_valittu= pygame.transform.scale(d4_valittu, (KUVAN_KOKO, KUVAN_KOKO) )

    d5_valittu = pygame.image.load('img\d5_valittu.png').convert_alpha()
    d5_valittu= pygame.transform.scale(d5_valittu, (KUVAN_KOKO, KUVAN_KOKO) )

    d6_valittu = pygame.image.load('img\d6_valittu.png').convert_alpha()
    d6_valittu= pygame.transform.scale(d6_valittu, (KUVAN_KOKO, KUVAN_KOKO) )  

    nopat =[]           # ei-valitut eli norminopat
    nopat.append(d1)
    nopat.append(d2)
    nopat.append(d3)
    nopat.append(d4)
    nopat.append(d5)
    nopat.append(d6)

    valitut =[]         # vihreä reunus
    valitut.append(d1_valittu)
    valitut.append(d2_valittu)
    valitut.append(d3_valittu)
    valitut.append(d4_valittu)
    valitut.append(d5_valittu)
    valitut.append(d6_valittu)

    return nopat, valitut


def muodosta_nopat(ei_valitut, valitut):
    nopat = []
    for i in range(5):
        nopat.append(Noppa(i, ei_valitut, valitut))
    return nopat


def alkuohjeet():
    ohjeet = []
    ohjeet.append("Tässä YAZZYn riisutussa versiossa kerätään:")
    ohjeet.append("  - kaksi paria")
    ohjeet.append("  - 3 samaa")
    ohjeet.append("  - täyskäsi")
    ohjeet.append("  - 4 samaa")
    ohjeet.append("  - 5 samaa")
    ohjeet.append("  - suorat 1-5 ja 2-6")
    ohjeet.append("  ")
    ohjeet.append("  klikkaa hiirtä aloittaaksesi")   

    return ohjeet
    


def valitse_5_randomia(nopat):    
    heitto = nopat
    for i in range(5):
        heitto[i].luku = random.randint(0, 5)    
        heitto[i].valittu = False
    return heitto


def mitä_kerätään():
    kerätään = ["kaksi paria", "kolmoset", "täyskäsi", "neloset",
                "Y A Z Z Y ! ! !", "pikku suora (1-5)", "iso suora (2-6)"]
    return kerätään