import pygame, random
from noppa import *



def nopat_listaan():
    KUVAN_KOKO = 72
    nopat =[]            # ei-valitut eli norminopat
    valitut =[]           # valitut 

    for i in range (1,7):
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
    ohjeet.append("  - suorat 1-5 ja 2-6")
    ohjeet.append("  ")
    ohjeet.append("  klikkaa hiirtä aloittaaksesi")   

    return ohjeet
    

def valitse_lukitsemattomat(nopat):  
    print("---valitse_lukitsemattomat---")
    heitto = nopat
    for i in range(5):
        if heitto[i].valittu == False:
            heitto[i].luku = random.randint(1, 6)
        print(heitto[i].luku )   
    return heitto


def valitse_5_randomia(nopat):    
    heitto = nopat
    for i in range(5):
        heitto[i].luku = random.randint(1, 6)    
        heitto[i].valittu = False

        print(str(i) + ".luku ", heitto[i].luku )    
    return heitto


def mitä_kerätään():
    kerätään = ["kaksi paria", "kolmoset", "täyskäsi", "neloset",
                "Y A Z Z Y ! ! !", "pikku suora (1-5)", "iso suora (2-6)"]
    return kerätään