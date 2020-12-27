import pygame, random
from yhteiset import *

class Nuotti:
    
    def __init__(self):        
        self.alin_nuotti = 0  # keski-c
        self.ylin_nuotti = 4   # g
        self.sanakirjat()     
        self.x = WIDTH - 50  # lähtöpiste oikeassa reunassa
        self.y = self.arvo_nuotti()
        self.PALLON_KOKO = int(PALLON_KOKO / 2) +1    
      
    def sanakirjat(self):             
        self.sijainnit = {}
        self.nimet = {}
        for i in range(5):
            self.nimet[i] = chr(99 + i)     # chr 99 = c           
            self.sijainnit[i] = ALIN_NUOTTI_Y - i * int(VIIVOJEN_VALI/2)   # /2 = viivojen väliin myös nuotti        

    def arvo_nuotti(self):
        self.arvottu_indeksi = random.randint(self.alin_nuotti, self.ylin_nuotti)
        self.x = WIDTH - 50
        self.y = self.sijainnit[self.arvottu_indeksi] 
        return self.y   

    def arvo_vari(self):
        r = random.randint(0, 200)   #ei yli 200, jottei tule valkoista/liian vaaleaa
        g = random.randint(0, 200)
        b = random.randint(0, 200)
        return r, g, b

    def nykyinen_nimi(self):
        return self.nimet[self.arvottu_indeksi]   
        
    def liiku(self):  
        self.x -= 1
        # osuu nuottiavaimeen:
        return not self.x == NUOTTIAV_SIJAINTI + (2 * self.PALLON_KOKO)  