import pygame

class Oikeellisuus:
   
   
    def tarkista(self, ruudukko, kerrokset, edelliset_muuvit):
        self.ruudukko = ruudukko
        self.kerrokset = kerrokset
        self.edelliset_muuvit = edelliset_muuvit
        if self.ymparilla_ei_tyhjaa() and self.xy_rivissa() and self.ei_samoja():
            return True
        return False


    def ymparilla_ei_tyhjaa(self):
        return True

    def xy_rivissa(self):
        return True

    def ei_samoja(self):
        l = [muuvi for muuvi in self.edelliset_muuvit if self.edelliset_muuvit.count(muuvi) > 1]
        if len(l) > 0:
            return False
        return True


    