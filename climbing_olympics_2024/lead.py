import random

class LeadTulos:

    def __init__ (self, nimi, ote, aika, top):
        self.nimi = nimi
        self.ote = ote                  # TODO esim. 22+  siis plus !!
        self.aika = aika
        self.top = top
        self.top_str = "Top"

    def __str__(self):   
        if self.top == self.ote :
            return f"{self.nimi:28}  {self.top_str:7} (time:{self.aika:.2f})" 
        return f"{self.nimi:28}  {self.ote:<7} (time:{self.aika:.2f})" 


class LeadKilpailu:

    def tulos_karsinta(self, kilpailijat):      # 10 kilpailijaa, 8 finaaliin     
        self.tulokset = []
        top = 45
        for kilpailija in kilpailijat:
            maksimi = int(kilpailijat[kilpailija].l/10 * top)
            tulos =  random.randint(int(maksimi/1.3), maksimi)
            aika = random.randint(200, 600)/100
            self.tulokset.append(LeadTulos(kilpailijat[kilpailija].nimi, int(tulos), aika, top))   # 3. parametri = aika, max 6 min
            
        s = sorted(self.tulokset, key=lambda tulos: (-tulos.ote, tulos.aika))        
        return s

    def pisteet_finaali(self, sijoitukset, kilpailijat):
        self.tulokset = []
        top = 48
        for koktulos in sijoitukset:
            maksimi = int(kilpailijat[koktulos.nimi].l/10 * top)
            tulos =  random.randint(int(maksimi/1.3), maksimi)
            aika = random.randint(200, 600)/100
            self.tulokset.append(LeadTulos(koktulos.nimi, int(tulos), aika, top))   # 3. parametri = aika, max 6 min
            
        s = sorted(self.tulokset, key=lambda tulos: (-tulos.ote, tulos.aika))        
        return s


    def jarjesta_sijoitukset(self, tulokset_list):
        tulokset = []
        sijoitus = 1
        tulokset.append([tulokset_list[0], sijoitus])    # eka on joka tapauksessa eka
        for i in range(1, len(tulokset_list)):
            # jos sama tulos ja sama aika
            if tulokset_list[i].ote == tulokset_list[i-1].ote and tulokset_list[i].aika == tulokset_list[i-1].aika :   
                tulokset.append([tulokset_list[i], sijoitus + 1])
            else:            
                sijoitus = i        
                tulokset.append([tulokset_list[i], sijoitus + 1]) 
        
        for tulos in tulokset:
            print(f"{tulos[1]:3}. {tulos[0].__str__()}")      
        
        return tulokset
            