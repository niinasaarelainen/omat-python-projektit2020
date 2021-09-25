import pygame

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
        self.osat.append([200, 250, 50, 450])
        # o jalka
        self.osat.append([200, 250, 350, 450])

    def piirra(self, naytto, montako):
        sininen = (0, 0, 100)
        for i in range(montako):
            osa = self.osat[i]
            if len(osa) == 4:
                pygame.draw.line(naytto, sininen, (osa[0], osa[1]), (osa[2], osa[3]), 6)
            else:
                pygame.draw.circle(naytto, sininen, (osa[0], osa[1]), osa[2]) 


