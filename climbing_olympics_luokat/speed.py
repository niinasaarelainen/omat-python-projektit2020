from operator import itemgetter
import random
fail = 1000

class SpeedTulos:

    def __init__ (self, kilpailija, aika):
        self.nimi = kilpailija.nimi 
        self.kilpailija = kilpailija  # luokan kilpailija olio
        self.aika = aika

    def __str__(self):
        if self.aika == fail:
            return f"{self.nimi:28}fail"
        return f"{self.nimi:28}{self.aika} sec"
        


class SpeedKilpailu:    

    def eka_kierros(self, kilpailijat):
        self.tulokset = []
        ajat_eka_kierros = [10.522, 11.022, 8.023, 8.022, 9.929, 15.022, fail, 7.022, fail, 7.922, 10.522, 11.022, 8.023, 8.022, 9.929, 15.022, fail, 7.022, fail, 7.922, 8.888, 9.999, 10.01, 11.111]
        aikaind = 0
        for nimi, kilpailija in kilpailijat.items(): 
            self.tulokset.append(SpeedTulos(kilpailija, ajat_eka_kierros[aikaind]))
            aikaind += 1

        s = sorted(self.tulokset, key=lambda tulos: tulos.aika)
        return s


    def finaalikierros(self, sijoitukset):
        self.ajat = []
        for koktulos in sijoitukset:
            self.ajat.append(SpeedTulos(koktulos.kilpailija, random.randint(8000,15000)/1000))   # aikoja 8.000 .. 15.000 s
        s = sorted(self.ajat, key=lambda tulos: tulos.aika)
        return s


    def losers(self, tyypit):
        self.ajat = []

        for tyyppi in tyypit:
            r = random.randint(1, 4)
            if r == 1 :  
                self.ajat.append(SpeedTulos(tyyppi.kilpailija, fail))   
            else:
                self.ajat.append(SpeedTulos(tyyppi.kilpailija, random.randint(8000,15000)/1000))   # aikoja 8.000 .. 15.000 s
        
        s = sorted(self.ajat, key=lambda tulos: tulos.aika)
        return s 


    def winners(self, tyypit):
        self.ajat = []

        for tyyppi in tyypit:
            self.ajat.append(SpeedTulos(tyyppi.kilpailija, random.randint(7000,12000)/1000))   
        
        s = sorted(self.ajat, key=lambda tulos: tulos.aika)
        return s 


    def finaalit(self, winners):
        tulos = []

        # 3.-4. sija
        self.ajat = []
        for tyyppi in winners[2:]:
            self.ajat.append(SpeedTulos(tyyppi.kilpailija, random.randint(7900,11000)/1000))      
        s = sorted(self.ajat, key=lambda tulos: tulos.aika, reverse = True)
        tulos += s      # ei voi lisätä kaikkia kerralla, koska 2. sijoittunut voi olla huonompi kuin 3.

        # 1.-2. sija
        self.ajat = []
        for tyyppi in winners[:2]:
            self.ajat.append(SpeedTulos(tyyppi.kilpailija, random.randint(7500,10000)/1000))      
        s = sorted(self.ajat, key=lambda tulos: tulos.aika, reverse = True)
        tulos += s

        tulos.reverse()   
        return tulos

    def speed_karsinta(self, kilpailijat):
        alkutulos = self.eka_kierros(kilpailijat)
        puolivali = int(len(alkutulos)/2)    # huom!  /2 tekee floatin vaikka tulos on int  8/2 != 4 vaan 4.0 !!! 
        losersit = self.losers(alkutulos[puolivali:])
        winnersit = self.winners(alkutulos[:puolivali])
        print("\nS P E E D -- KARSINTA")
        the_tulos = self.finaalit(winnersit) + losersit
        for tulos in the_tulos:
            print(tulos) 
        return the_tulos

    def speed_finaali(self, sijoitukset):
        alkutulos = self.finaalikierros(sijoitukset)
        puolivali = int(len(alkutulos)/2)    # huom!  /2 tekee floatin vaikka tulos on int  8/2 != 4 vaan 4.0 !!! 
        losersit = self.losers(alkutulos[puolivali:])
        winnersit = self.winners(alkutulos[:puolivali])
        return self.finaalit(winnersit) + losersit

"""
speedKilpailu = SpeedKilpailu()
speedKilpailu.speed_karsinta()     # 2.tullut voi olla hitaampi kuin 3./4.
# speedKilpailu.speed_finaali()   ei voi testata kun ei ole sijoitukset, joka rakentuu total_rankingissa
"""