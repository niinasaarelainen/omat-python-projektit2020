from operator import itemgetter
import random
fail = 1000

class SpeedTulos:

    def __init__ (self, nimi, aika):
        self.nimi = nimi
        self.aika = aika

    def __str__(self):
        if self.aika == fail:
            return f"{self.nimi:15}fail"
        return f"{self.nimi:15}{self.aika} sec"
        


class SpeedKilpailu:    

    def eka_kierros(self):
        self.ajat = []
        self.ajat.append(SpeedTulos("Janja", 10.522))
        self.ajat.append(SpeedTulos("Jain", 11.022))
        self.ajat.append(SpeedTulos("Jessica", 8.023))
        self.ajat.append(SpeedTulos("Alex", 8.022))
        self.ajat.append(SpeedTulos("AlexPlus", 9.929))   
        self.ajat.append(SpeedTulos("AlexHidas", 17.022))   
        self.ajat.append(SpeedTulos("Julia", fail))          # varaslähtö
        self.ajat.append(SpeedTulos("Ihmelapsi", 7.022))
        self.ajat.append(SpeedTulos("Anna", fail))
        self.ajat.append(SpeedTulos("Margo", 7.922))

        s = sorted(self.ajat, key=lambda tulos: tulos.aika)
        return s


    def finaalikierros(self, sijoitukset):
        self.ajat = []
        for i in range(8):
            self.ajat.append([sijoitukset[i][0], random.randint(8000,15000)/1000])   # aikoja 8.000 .. 15.000 s

        self.ajat.sort(key=itemgetter(1))
        return self.ajat


    def losers(self, tyypit):
        self.ajat = []

        for tyyppi in tyypit:
            r = random.randint(1, 4)
            if r == 1 :  
                self.ajat.append([tyyppi[0], fail])   
            else:
                self.ajat.append([tyyppi[0], random.randint(8000,15000)/1000])   # aikoja 8.000 .. 15.000 s
        
        self.ajat.sort(key=itemgetter(1))
        return self.ajat    


    def winners(self, tyypit):
        self.ajat = []

        for tyyppi in tyypit:
            self.ajat.append([tyyppi[0], random.randint(7000,12000)/1000])   
        
        self.ajat.sort(key=itemgetter(1))
        return self.ajat    


    def finaalit(self, winners):
        tulos = []

        # 3.-4. sija
        self.ajat = []
        for tyyppi in winners[2:]:
            self.ajat.append([tyyppi[0], random.randint(7900,11000)/1000])      
        self.ajat.sort(key=itemgetter(1), reverse = True)
        #print("3-4-", self.ajat)
        tulos += self.ajat       # ei voi lisätä kaikkia kerralla, koska 2. sijoittunut voi olla huonompi kuin 3.

        # 1.-2. sija
        self.ajat = []
        for tyyppi in winners[:2]:
            self.ajat.append([tyyppi[0], random.randint(7500,10000)/1000])      
        self.ajat.sort(key=itemgetter(1), reverse = True)
        #print("1-2-", self.ajat)
        tulos += self.ajat 

        tulos.reverse()
        return tulos

    def speed_karsinta(self):
        alkutulos = self.eka_kierros()
        puolivali = int(len(alkutulos)/2)    # huom!  /2 tekee floatin vaikka tulos on int  8/2 != 4 vaan 4.0 !!! 
        losersit = self.losers(alkutulos[puolivali:])
        winnersit = self.winners(alkutulos[:puolivali])
        print("\nS P E E D -- KARSINTA")
        the_tulos = self.finaalit(winnersit) + losersit
        for tulos in the_tulos:
            if tulos[1] == 1000:
                pr = f"{tulos[0]}: fail"   
            else:
                pr = f"{tulos[0]}: {tulos[1]} sekuntia"
            print(pr) 
        return the_tulos

    def speed_finaali(self, sijoitukset):
        alkutulos = self.finaalikierros(sijoitukset)
        puolivali = int(len(alkutulos)/2)    # huom!  /2 tekee floatin vaikka tulos on int  8/2 != 4 vaan 4.0 !!! 
        losersit = self.losers(alkutulos[puolivali:])
        winnersit = self.winners(alkutulos[:puolivali])
        return self.finaalit(winnersit) + losersit


speedKilpailu = SpeedKilpailu()
for tulos in speedKilpailu.eka_kierros():
    print(tulos)