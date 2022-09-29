import pygame, random
from yhteiset import *

class Nuotti:
    
    def __init__(self, alin_nuotti, ylin_nuotti):        
        self.alin_nuotti = alin_nuotti  # indeksitarkistukset tehty ennen kutsua
        self.ylin_nuotti = ylin_nuotti   
        self.sanakirjat()     
        self.x = WIDTH - 50  
        self.y = self.arvo_nuotti()
        self.PALLON_KOKO = int(PALLON_KOKO / 2) +1

    
    def arvo_vari(self):
        r = random.randint(0, 200)   #ei yli 200, jottei tule valkoista/liian vaaleaa
        g = random.randint(0, 200)
        b = random.randint(0, 200)
        return r, g, b
    
    def sanakirjat(self):             
        self.sijainnit = {}
        self.keycodet = {}

        for i in range(self.alin_nuotti, self.ylin_nuotti + 1):
            if i == 0 or i == 7:   # a
                self.keycodet[i] = 97
            elif i == 6: # h
                self.keycodet[i] = 104
            elif i <= 5: # ylä-c - ylä-f  ei jatka aakkosia i, j, k....
                self.keycodet[i] = 104 - i    # g-avain = 102
            else:
                self.keycodet[i] = 111 - i       # g-avain = 109         
            self.sijainnit[i] = YLIN_VIIVA + i * int(VIIVOJEN_VALI/2)   # /2 = viivojen väliin myös nuotti
        

    def arvo_nuotti(self):
        self.arvottu_indeksi = random.randint(self.alin_nuotti, self.ylin_nuotti)
        self.x = WIDTH - 50
        self.y = self.sijainnit[self.arvottu_indeksi] 
        return self.y   

    def nykyinen_keycode(self):
        return self.keycodet[self.arvottu_indeksi]   
        
    def liiku(self):  
        self.x -= 1
        # osuu nuottiavaimeen:
        return not self.x == NUOTTIAV_SIJAINTI + (2 * self.PALLON_KOKO)  