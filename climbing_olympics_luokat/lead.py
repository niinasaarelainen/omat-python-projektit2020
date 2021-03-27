import random

class LeadTulos:

    def __init__ (self, nimi, ote, aika):
        self.nimi = nimi
        self.ote = ote
        self.aika = aika
    def __str__(self):        
        return f"{self.nimi:15}  {self.ote:7} (time:{self.aika:.2f})" 


class LeadKilpailu:

    def tulos_karsinta(self):      # 10 kilpailijaa, 8 finaaliin     
        top = 46.0        
        self.tulokset = []
        self.tulokset.append(LeadTulos("Janja", top, 4.40))   # 3. parametri = aika, max 6 min
        self.tulokset.append(LeadTulos("Jain", 44.0, 5.0))    # Jain ja Julia kaikki samat    
        self.tulokset.append(LeadTulos("Julia", 44.0, 5.0))
        self.tulokset.append(LeadTulos("Jessica", 39.5, 5.50))
        self.tulokset.append(LeadTulos("Alex", 9.0, 2.41))
        self.tulokset.append(LeadTulos("AlexPlus", 9.5, 3.30))   # +
        self.tulokset.append(LeadTulos("AlexHidas", 9.0, 3.51))   # -
        self.tulokset.append(LeadTulos("Ihmelapsi", top, 4.41))
        self.tulokset.append(LeadTulos("Margo", 45.5, 5.11))
        self.tulokset.append(LeadTulos("Anna", 22.0, 4.41))

        s = sorted(self.tulokset, key=lambda tulos: (-tulos.ote, tulos.aika))
        return s


    def pisteet_finaali(self, sijoitukset):
        self.tulokset = []
        top = 48.0
        for i in range(8):
            if sijoitukset[i][0] == 'Janja':
                tulos =  random.randint(top/1.2*100, top*100)/100     # Janja pääsee väh. 5/6 reittiä
            else:
                tulos =  random.randint(top/2*100, top*100)/100
            aika = random.randint(200, 600)/100
            self.tulokset.append([sijoitukset[i][0], tulos, aika])   # 3. parametri = aika, max 6 min
            
        s = sorted(self.tulokset, key=lambda s: (-s[1], s[2]) )  
        return s


    def tulokset(self, tulokset_list):
        tulokset = []
        sijoitus = 0
        tulokset.append([tulokset_list[0][0], sijoitus])    # eka on joka tapauksessa eka
        for i in range(1, len(tulokset_list)):
            # jos sama tulos ja sama aika
            if tulokset_list[i][1] == tulokset_list[i-1][1] and tulokset_list[i][2] == tulokset_list[i-1][2] :   
                tulokset.append([tulokset_list[i][0], sijoitus])
            else:            
                sijoitus = i        
                tulokset.append([tulokset_list[i][0], sijoitus])        
        
        return tulokset
            

leadKilpailu  = LeadKilpailu()
tulokset_list = leadKilpailu.tulos_karsinta()
#karsintatulos = leadKilpailu.tulokset(tulokset_list)
print("\nL E A D -- KARSINTA")
for tulos in tulokset_list:
    print(tulos) 
