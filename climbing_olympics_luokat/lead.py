import random

class LeadTulos:

    def __init__ (self, nimi, ote, aika):
        self.nimi = nimi
        self.ote = ote
        self.aika = aika
    def __str__(self):        
        return f"{self.nimi:15}  {self.ote:7} (time:{self.aika:.2f})" 


class LeadKilpailu:

    def tulos_karsinta(self, kilpailijat):      # 10 kilpailijaa, 8 finaaliin     
        self.tulokset = []
        top = 45.0
        for kilpailija in kilpailijat:
            if kilpailija == 'Janja':
                tulos =  random.randint(top/1.2*100, top*100)/100     # Janja pääsee väh. 5/6 reittiä
            else:
                tulos =  random.randint(top/2*100, top*100)/100
            aika = random.randint(200, 600)/100
            self.tulokset.append(LeadTulos(kilpailijat[kilpailija].nimi, int(tulos), aika))   # 3. parametri = aika, max 6 min
            
        s = sorted(self.tulokset, key=lambda tulos: (-tulos.ote, tulos.aika))        
        return s

    def pisteet_finaali(self, sijoitukset):
        self.tulokset = []
        top = 48.0
        for koktulos in sijoitukset:
            if koktulos.nimi == 'Janja':
                tulos =  random.randint(top/1.2*100, top*100)/100     # Janja pääsee väh. 5/6 reittiä
            else:
                tulos =  random.randint(top/2*100, top*100)/100
            aika = random.randint(200, 600)/100
            self.tulokset.append(LeadTulos(koktulos.nimi, int(tulos), aika))   # 3. parametri = aika, max 6 min
            
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
            
"""
leadKilpailu  = LeadKilpailu()
tulokset_list = leadKilpailu.tulos_karsinta()
karsintatulos = leadKilpailu.tulokset(tulokset_list)  """  

