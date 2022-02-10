import pygame, random
from yhteiset import *

class Nuotti:

    def __init__(self):        
        self.alin_nuotti = 1 
        self.ylin_nuotti = 11  

    def arvo_nuotti(self):
        self.arvottu_indeksi = random.randint(self.alin_nuotti, self.ylin_nuotti)
        self.x = self.arvottu_indeksi  * 35
        self.y = 1
        return self.y   

    def arvo_vari(self):
        r = random.randint(0, 70)   #ei yli 200, jottei tule valkoista/liian vaaleaa
        g = random.randint(0, 70)
        b = random.randint(100, 200)
        return r, g, b
        
    

class Obsticle:
        
    def __init__(self, x, y, x2, y2):  
        self.x_aloitus = x
        self.y_aloitus = y
        self.x_lopetus = self.x_aloitus + x2
        self.y_lopetus = self.y_aloitus + y2