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
            return f"{self.nimi:28} No Tops, No Zones"
        elif self.topit_lkm == 0:
            return f"{self.nimi:28} No Tops, {self.zonet_lkm}Z{self.zonet_yritykset}"
        return f"{self.nimi:28} {self.topit_lkm}T{self.topit_yritykset}, {self.zonet_lkm}Z{self.zonet_yritykset}"


class BoulderKilpailu:

    def tulos_karsinta(self, kilpailijat):      # erilainen data kuin BoulderTulos !! Tämän olisi voinut jäättää pois
        tulokset = [] 
        for kilpailija in kilpailijat:
            maksimi = int(kilpailijat[kilpailija].b/10 * 4) #4 reittiä
            self.topit_lkm = random.randint(max(0, maksimi -1), maksimi)
            self.topit_yritykset = random.randint(self.topit_lkm, 10) 
            self.zonet_lkm = random.randint(self.topit_lkm, min(4, maksimi +1))
            self.zonet_yritykset = random.randint(self.zonet_lkm, 15)
           
            tulokset.append(BoulderTulos(kilpailijat[kilpailija].nimi, self.topit_lkm, self.topit_yritykset, self.zonet_lkm, self.zonet_yritykset))  
        s = sorted(tulokset, key=lambda tulos: (-tulos.topit_lkm, tulos.topit_yritykset, -tulos.zonet_lkm, tulos.zonet_yritykset))  
      
        print("\nB O U L D E R -- KARSINTA")
        for tulos in s:
            print(tulos) 
        return s


    def tulos_finaali(self, sijoitukset, kilpailijat):
        tulokset = [] 
        for koktulos in sijoitukset:
            maksimi = int(kilpailijat[koktulos.nimi].b/10 * 3)  #3 reittiä
            self.topit_lkm = random.randint(max(0, maksimi -1), maksimi)
            self.topit_yritykset = random.randint(self.topit_lkm, 9)  
            self.zonet_lkm = random.randint(self.topit_lkm, min(4, maksimi +1))
            self.zonet_yritykset = random.randint(self.zonet_lkm, 15)
            
            tulokset.append(BoulderTulos(koktulos.nimi, self.topit_lkm, self.topit_yritykset, self.zonet_lkm, self.zonet_yritykset))  
        s = sorted(tulokset, key=lambda tulos: (-tulos.topit_lkm, tulos.topit_yritykset, -tulos.zonet_lkm, tulos.zonet_yritykset))  
        return s
 