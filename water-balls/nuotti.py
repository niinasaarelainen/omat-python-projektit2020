import pygame, random
from yhteiset import *

class Nuotti:
    
    def __init__(self):        
        self.alin_nuotti = 1  # keski-c
        self.ylin_nuotti = 14   # g
        self.x = self.arvo_nuotti() * 50
        self.y = 100
        self.PALLON_KOKO = int(PALLON_KOKO / 2) +1   

    def arvo_nuotti(self):
        self.arvottu_indeksi = random.randint(self.alin_nuotti, self.ylin_nuotti)
        self.x = self.arvottu_indeksi  * 50
        self.y = 100
        return self.y   

    def arvo_vari(self):
        r = random.randint(0, 70)   #ei yli 200, jottei tule valkoista/liian vaaleaa
        g = random.randint(0, 70)
        b = random.randint(100, 200)
        return r, g, b
        
    def liiku(self):  
        self.x -= 1
        # osuu nuottiavaimeen:
        return not self.x == NUOTTIAV_SIJAINTI + (2 * self.PALLON_KOKO)  