import pygame

class Oikeellisuus:
   
   
    def tarkista(self, ruudukko, edelliset_muuvit):
        self.syy = ""
        self.ruudukko = ruudukko
        self.vika_indeksi = len(self.ruudukko) - 1
        self.edelliset_muuvit = edelliset_muuvit
        if self.ymparilla_ei_tyhjaa() and self.xy_rivissa() and self.ei_samoja():
            return True
        return False


    def ymparilla_ei_tyhjaa(self):
        for x, y in self.edelliset_muuvit:           
            if y - 1 > 0:
                if not self.ruudukko[y - 1][x] == "":
                    return True 
            if x - 1 > 0: 
                if not self.ruudukko[y][x - 1] == "":
                    return True 
            if x + 1 < self.vika_indeksi:
                if not self.ruudukko[y][x + 1] == "":
                    return True 
            if y + 1 < self.vika_indeksi:
                if not self.ruudukko[y  + 1 ][x] == "":
                    return True 
            self.syy = "kirjaimen tulee koskettaa vaaka- tai pystysuunnassa vanhaa kirjainta "
        return False
        

    def xy_rivissa(self):
        y_t = [y for x, y in self.edelliset_muuvit]
        x_t = [x for x, y in self.edelliset_muuvit]
        if not y_t[0] == y_t[-1] and not x_t[0] == x_t[-1] :
            self.syy = "laittamasi kirjaimet eivät saa olla diagonaalisuuntaisesti"
            return False        
        return True


    def ei_samoja(self):
        l = [muuvi for muuvi in self.edelliset_muuvit if self.edelliset_muuvit.count(muuvi) > 1]
        if len(l) > 0:
            self.syy = "ei saa laittaa useita kirjaimia päällekkäin samalla vuorolla"
            return False
        return True


    def ei_tyhjaa_valissa(self):
        pass