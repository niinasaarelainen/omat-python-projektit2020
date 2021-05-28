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

    def eka_kierros(self, kilpailijat, voittoaika):
        self.ajat = []
        for nimi, kilpailija in kilpailijat.items(): 
            minimi = int((1 + kilpailija.s/10) * voittoaika * 1000)
            self.ajat.append(SpeedTulos(kilpailija, random.randint(minimi, int(minimi*1.2))/1000))   # aikoja 8.000 .. 15.000 s

        s = sorted(self.ajat, key=lambda tulos: tulos.aika)
        return s


    def finaalikierros(self, sijoitukset, kilpailijat, voittoaika):
        self.ajat = []
        for koktulos in sijoitukset:
            minimi = int((1 + kilpailijat[koktulos.nimi].s/10) * voittoaika * 1000)
            self.ajat.append(SpeedTulos(koktulos.kilpailija, random.randint(minimi, int(minimi*1.2))/1000))   # aikoja 8.000 .. 15.000 s
        s = sorted(self.ajat, key=lambda tulos: tulos.aika)
        return s


    def losers(self, tyypit, voittoaika):
        self.ajat = []

        for tulos in tyypit:
            r = random.randint(1, 4)
            if r == 1 :  
                self.ajat.append(SpeedTulos(tulos.kilpailija, fail))   
            else:
                minimi = int((1 + tulos.kilpailija.s/10) * voittoaika * 1000)
                self.ajat.append(SpeedTulos(tulos.kilpailija, random.randint(minimi, int(minimi*1.2))/1000))   

        s = sorted(self.ajat, key=lambda tulos: tulos.aika)
        return s 


    def winners(self, tyypit, voittoaika):
        self.ajat = []

        for tulos in tyypit:
            minimi = int((1 + tulos.kilpailija.s/10) * voittoaika * 1000)
            self.ajat.append(SpeedTulos(tulos.kilpailija, random.randint(minimi, int(minimi*1.2))/1000))   

        
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

    def speed_karsinta(self, kilpailijat, voittoaika):
        alkutulos = self.eka_kierros(kilpailijat, voittoaika)
        puolivali = int(len(alkutulos)/2)    # huom!  /2 tekee floatin vaikka tulos on int  8/2 != 4 vaan 4.0 !!! 
        losersit = self.losers(alkutulos[puolivali:], voittoaika)
        winnersit = self.winners(alkutulos[:puolivali], voittoaika)
        print("\nS P E E D -- KARSINTA")
        the_tulos = self.finaalit(winnersit) + losersit
        for tulos in the_tulos:
            print(tulos) 
        return the_tulos

    def speed_finaali(self, sijoitukset, kilpailijat, voittoaika):
        alkutulos = self.finaalikierros(sijoitukset, kilpailijat, voittoaika)
        puolivali = int(len(alkutulos)/2)    # huom!  /2 tekee floatin vaikka tulos on int  8/2 != 4 vaan 4.0 !!! 
        losersit = self.losers(alkutulos[puolivali:], voittoaika)
        winnersit = self.winners(alkutulos[:puolivali], voittoaika)
        return self.finaalit(winnersit) + losersit

"""
speedKilpailu = SpeedKilpailu()
speedKilpailu.speed_karsinta()     # 2.tullut voi olla hitaampi kuin 3./4.
# speedKilpailu.speed_finaali()   ei voi testata kun ei ole sijoitukset, joka rakentuu total_rankingissa
"""