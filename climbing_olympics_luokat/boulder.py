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
            return f"{self.nimi:15} -"
        elif self.topit_lkm == 0:
            return f"{self.nimi:15} No Tops, {self.zonet_lkm}Z{self.zonet_yritykset}"
        return f"{self.nimi:15} {self.topit_lkm}T{self.topit_yritykset}, {self.zonet_lkm}Z{self.zonet_yritykset}"


class BoulderKilpailu:

    def tulos_karsinta(self):      # erilainen data kuin BoulderTulos !! Tämän olisi voinut jäättää pois
        pisteet = []      
        pisteet.append(["Janja", "T1", "Z1", "T2", "Z1", "Z1"]) # 3 boulderia, vikasta ei toppia
        pisteet.append(["Jain", "T10", "Z1", "T2", "Z1", "Z6"])
        pisteet.append(["Jessica", "T3", "Z1", "T5", "Z1", "Z7"])
        pisteet.append(["Alex", "T2", "Z1", "Z1", "Z12"])
        pisteet.append(["Fanny", "T2", "Z1", "Z1", "Z3"])
        pisteet.append(["AlexHidas", "T2", "Z1", "Z1", "Z1"])
        pisteet.append(["Julia", "T3", "Z1", "T5", "Z1", "Z9"])
        pisteet.append(["Ihmelapsi", "Z1", "Z1", "Z12"])
        pisteet.append(["Anna", "T4","Z1", "Z1", "Z12"])
        pisteet.append(["Margo", "T5", "Z1", "Z1", "Z12"])    
            
        tulokset = []   # järjestämätön data    
        for tulos in pisteet:   
            self.topit_lkm = 0 
            self.topit_yritykset = 0
            self.zonet_lkm = 0
            self.zonet_yritykset = 0
        
            for piste in tulos[1:]:  
                if "T" in piste:
                    self.topit_lkm += 1
                    self.topit_yritykset += int(piste[1:])
                elif "Z" in piste:   
                    self.zonet_lkm += 1
                    self.zonet_yritykset += int(piste[1:])      
            tulokset.append(BoulderTulos(tulos[0], self.topit_lkm, self.topit_yritykset, self.zonet_lkm, self.zonet_yritykset))  

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

    def jarjesta_dictiin(self, lista, ind):
        dict = {}
        for tulos in lista:
            if tulos[ind] in dict:
                dict[tulos[ind]].append(tulos)
            else:
                dict[tulos[ind]] = []    
                dict[tulos[ind]].append(tulos)
        return dict
 

"""
boulderKilpailu = BoulderKilpailu()
print("\nB O U L D E R -- KARSINTA")
for tulos in boulderKilpailu.tulos_karsinta():
    print(tulos)  """

