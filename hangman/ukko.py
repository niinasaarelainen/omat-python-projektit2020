import pygame
from vakiot import *

class Ukko:

    def __init__(self):
        self.osat = []
        self.monesko_virhe = 0


    def osat_taulukkoon(self):
        #naru
        self.osat.append([200, 0, 200, 50])         
        #pää
        self.osat.append([200, 50, 25]) 
        #yläruumis
        self.osat.append([200, 50, 200, 250])         
        # v käsi
        self.osat.append([200, 100, 150, 200]) 
        # o käsi
        self.osat.append([200, 100, 250, 200]) 
        # v jalka
        self.osat.append([200, 250, 50, 420])
        # o jalka
        self.osat.append([200, 250, 350, 420])
        # ilme
        self.osat.append([188, 47, 5, 212, 47, 5, 200, 59, 9]) 


    def piirra(self, naytto, montako):
        
        for i in range(montako):
            osa = self.osat[i]
            if len(osa) == 4:
                pygame.draw.line(naytto, sininen, (osa[0], osa[1]), (osa[2], osa[3]), 6)
            elif len(osa) == 3:
                pygame.draw.circle(naytto, sininen, (osa[0], osa[1]), osa[2]) 
            else:
                pygame.draw.circle(naytto, ruskea, (osa[0], osa[1]), osa[2]) 
                pygame.draw.circle(naytto, ruskea, (osa[3], osa[4]), osa[5]) 
                pygame.draw.circle(naytto, ruskea, (osa[6], osa[7]), osa[8])


