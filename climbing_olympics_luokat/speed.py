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

    def minimiaika(self, kilpailija, voittoaika):
        kerroin = abs(kilpailija.s - 10)/10 + 1    # s = 1-10
        return int(kerroin * voittoaika * 1000)

    def eka_kierros(self, kilpailijat, voittoaika):
        self.ajat = []
        for nimi, kilpailija in kilpailijat.items(): 
            minimi = self.minimiaika(kilpailija, voittoaika)
            print("minimi:", minimi)
            self.ajat.append(SpeedTulos(kilpailija, random.randint(minimi, int(minimi*1.2))/1000))   

        s = sorted(self.ajat, key=lambda tulos: tulos.aika)
        return s


    def finaalikierros(self, sijoitukset, kilpailijat, voittoaika):
        self.ajat = []
        for koktulos in sijoitukset:
            minimi = self.minimiaika(koktulos.kilpailija, voittoaika)
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
                minimi = self.minimiaika(tulos.kilpailija, voittoaika)
                self.ajat.append(SpeedTulos(tulos.kilpailija, random.randint(minimi, int(minimi*1.2))/1000))   

        s = sorted(self.ajat, key=lambda tulos: tulos.aika)
        return s 


    def winners(self, tyypit, voittoaika):
        self.ajat = []

        for tulos in tyypit:
            minimi = self.minimiaika(tulos.kilpailija, voittoaika)
            self.ajat.append(SpeedTulos(tulos.kilpailija, random.randint(minimi, int(minimi*1.2))/1000))   
        
        s = sorted(self.ajat, key=lambda tulos: tulos.aika)
        return s 


    def finaalit(self, winners, voittoaika):
        tulokset = []
        # 3.-4. sija
        self.ajat = []
        for tulos in winners[2:]:
            minimi = self.minimiaika(tulos.kilpailija, voittoaika)
            self.ajat.append(SpeedTulos(tulos.kilpailija, random.randint(minimi, int(minimi*1.2))/1000))   
        s = sorted(self.ajat, key=lambda tulos: tulos.aika, reverse = True)
        tulokset += s      # ei voi lisätä kaikkia kerralla, koska 2. sijoittunut voi olla huonompi kuin 3.

        # 1.-2. sija
        self.ajat = []
        for tulos in winners[:2]:
            minimi = self.minimiaika(tulos.kilpailija, voittoaika)
            self.ajat.append(SpeedTulos(tulos.kilpailija, random.randint(minimi, int(minimi*1.2))/1000))       
        s = sorted(self.ajat, key=lambda tulos: tulos.aika, reverse = True)
        tulokset += s

        tulokset.reverse()   
        return tulokset

    def speed_karsinta(self, kilpailijat, voittoaika):
        alkutulos = self.eka_kierros(kilpailijat, voittoaika)
        puolivali = int(len(alkutulos)/2)    # huom!  /2 tekee floatin vaikka tulos on int  8/2 != 4 vaan 4.0 !!! 
        losersit = self.losers(alkutulos[puolivali:], voittoaika)
        winnersit = self.winners(alkutulos[:puolivali], voittoaika)
        print("\nS P E E D -- KARSINTA")
        the_tulos = self.finaalit(winnersit, voittoaika) + losersit
        for tulos in the_tulos:
            print(tulos) 
        return the_tulos

    def speed_finaali(self, sijoitukset, kilpailijat, voittoaika):
        alkutulos = self.finaalikierros(sijoitukset, kilpailijat, voittoaika)
        puolivali = int(len(alkutulos)/2)    # huom!  /2 tekee floatin vaikka tulos on int  8/2 != 4 vaan 4.0 !!! 
        losersit = self.losers(alkutulos[puolivali:], voittoaika)
        winnersit = self.winners(alkutulos[:puolivali], voittoaika)
        return self.finaalit(winnersit, voittoaika) + losersit
