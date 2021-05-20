import operator, random


class BoulderTulos:

    def __init__ (self, nimi, topit_lkm , topit_yritykset, zonet_lkm, zonet_yritykset):
        self.nimi = nimi
        self.topit_lkm = topit_lkm 
        self.topit_yritykset = topit_yritykset
        self.zonet_lkm = zonet_lkm
        self.zonet_yritykset = zonet_yritykset
        self.pisteet = []

    def __str__(self):
        if self.topit_lkm == 0 and self.zonet_lkm == 0:
            return f"{self.nimi:15} No Tops, No Zones"
        elif self.topit_lkm == 0:
            return f"{self.nimi:15} No Tops, {self.zonet_lkm}Z{self.zonet_yritykset}"
        return f"{self.nimi:15} {self.topit_lkm}T{self.topit_yritykset}, {self.zonet_lkm}Z{self.zonet_yritykset}"


class BoulderKilpailu:

    def tulos_karsinta(self, kilpailijat):      # erilainen data kuin BoulderTulos !! Tämän olisi voinut jäättää pois
        tulokset = [] 
        for kilpailija in kilpailijat:
            if kilpailija == 'Janja':
                self.topit_lkm = random.randint(3,4)
                self.topit_yritykset = random.randint(self.topit_lkm, 5)  #4 reittiä, flash jokaisesta : 3
                self.zonet_lkm = random.randint(self.topit_lkm, 4)
                self.zonet_yritykset = random.randint(self.topit_yritykset, self.topit_yritykset)
            else:
                self.topit_lkm = random.randint(0,4)
                self.topit_yritykset = random.randint(4, 15)
                self.zonet_lkm = random.randint(self.topit_lkm, 4)
                self.zonet_yritykset = random.randint(3, self.topit_yritykset)
            tulokset.append(BoulderTulos(kilpailijat[kilpailija].nimi, self.topit_lkm, self.topit_yritykset, self.zonet_lkm, self.zonet_yritykset))  
        s = sorted(tulokset, key=lambda tulos: (-tulos.topit_lkm, tulos.topit_yritykset, -tulos.zonet_lkm, tulos.zonet_yritykset))  
      
        print("\nB O U L D E R -- KARSINTA")
        for tulos in s:
            print(tulos) 
        return s


    def tulos_finaali(self, sijoitukset):
        tulokset = [] 
        for koktulos in sijoitukset:
            if koktulos.nimi == 'Janja':
                self.topit_lkm = random.randint(2,3)
                self.topit_yritykset = random.randint(self.topit_lkm, 5)  # 3 reittiä, flash jokaisesta : 3
                self.zonet_lkm = random.randint(self.topit_lkm, 3)
                self.zonet_yritykset = random.randint(self.topit_yritykset, self.topit_yritykset)
            else:
                self.topit_lkm = random.randint(0,3)
                self.topit_yritykset = random.randint(3, 15)
                self.zonet_lkm = random.randint(self.topit_lkm, 3)
                self.zonet_yritykset = random.randint(3, self.topit_yritykset)
            tulokset.append(BoulderTulos(koktulos.nimi, self.topit_lkm, self.topit_yritykset, self.zonet_lkm, self.zonet_yritykset))  
        s = sorted(tulokset, key=lambda tulos: (-tulos.topit_lkm, tulos.topit_yritykset, -tulos.zonet_lkm, tulos.zonet_yritykset))  
        return s
 