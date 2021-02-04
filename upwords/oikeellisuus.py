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
        y_t = [y for x, y in self.edelliset_muuvit]
        x_t = [x for x, y in self.edelliset_muuvit]
        if not y_t[0] == y_t[-1] and not x_t[0] == x_t[-1] :
            print(y_t[0], y_t[-1], x_t[0], x_t[-1])
            return False
        return True


    def ei_samoja(self):
        l = [muuvi for muuvi in self.edelliset_muuvit if self.edelliset_muuvit.count(muuvi) > 1]
        if len(l) > 0:
            return False
        return True


    