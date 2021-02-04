import pygame

class Oikeellisuus:
   
   
    def tarkista(self, ruudukko, edelliset_muuvit):
        self.ruudukko = ruudukko
        self.vika_indeksi = len(self.ruudukko) - 1
        self.edelliset_muuvit = edelliset_muuvit
        if self.ymparilla_ei_tyhjaa() and self.xy_rivissa() and self.ei_samoja():
            return True
        return False


    def ymparilla_ei_tyhjaa(self):
        for x, y in self.edelliset_muuvit:           
            if not self.ruudukko[max(y - 1, 0)][x] == "":
                 return True 
            if not self.ruudukko[y][max(x - 1, 0)] == "":
                return True 
            if not self.ruudukko[y][min(x + 1, self.vika_indeksi)] == "":
                return True 
            if not self.ruudukko[min(y  + 1, self.vika_indeksi)][x] == "":
                return True 
        return False
        

    def xy_rivissa(self):
        y_t = [y for x, y in self.edelliset_muuvit]
        x_t = [x for x, y in self.edelliset_muuvit]
        if not y_t[0] == y_t[-1] and not x_t[0] == x_t[-1] :
            return False
        return True


    def ei_samoja(self):
        l = [muuvi for muuvi in self.edelliset_muuvit if self.edelliset_muuvit.count(muuvi) > 1]
        if len(l) > 0:
            return False
        return True


    