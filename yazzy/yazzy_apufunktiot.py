import pygame, random
from noppa import *

MAX_SILMALUKU = 8
KUVAN_KOKO = 75
NOPPIEN_VALI = 5

def nopat_listaan():
    nopat =[]            # ei-valitut eli norminopat
    valitut =[]           # valitut 

    for i in range (1, MAX_SILMALUKU + 1):
        s = 'img\d'+str(i)+'.png'
        d = pygame.image.load(s).convert_alpha()
        d= pygame.transform.scale(d, (KUVAN_KOKO, KUVAN_KOKO) )
        nopat.append(d)

        s = 'img\d'+str(i)+'_valittu.png'
        d_valittu = pygame.image.load(s).convert_alpha()
        d_valittu= pygame.transform.scale(d_valittu, (KUVAN_KOKO, KUVAN_KOKO) )
        valitut.append(d_valittu)
    
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
    ohjeet.append("  - suorat 1-5, 2-6, 3-7 ja 4-8")
    ohjeet.append("  ")
    ohjeet.append("  klikkaa hiirtä aloittaaksesi")   

    return ohjeet
    

def valitse_lukitsemattomat(nopat):  
    print("---valitse_lukitsemattomat---")
    heitto = nopat
    for i in range(5):
        if heitto[i].valittu == False:
            heitto[i].luku = random.randint(1, MAX_SILMALUKU)
        print(heitto[i].luku )   
    return heitto


def valitse_5_randomia(nopat):    
    heitto = nopat
    for i in range(5):
        heitto[i].luku = random.randint(1, MAX_SILMALUKU)    
        heitto[i].valittu = False

        print(str(i) + ".luku ", heitto[i].luku )    
    return heitto


def mitä_kerätään():
    kerätään = ["kaksi paria", "kolmoset", "täyskäsi", "neloset",
                "Y A Z Z Y ! ! !", "suora 1-5", "suora 2-6", "suora 3-7", "suora 4-8"]
    return kerätään