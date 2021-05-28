import speed, boulder, lead, kokonaistulos
from operator import itemgetter

class Kilpailija:

    def __init__(self, nimi, pituus, paino, wingspan, maa, ika, ranking = ""):
        self.nimi = nimi
        self.pituus = pituus
        self.paino = paino
        self.wingspan = wingspan
        self.maa = maa
        self.ika = ika
        self.ranking = ranking

    def painotukset(self, s, b, l):  # arvosana 1-10 kunkin disciplinen taidoista, 10 = maailman paras
        self.s = s
        self.b = b
        self. l = l

    def __str__(self):
        if self.wingspan > 0:                                                 # halutaan plusmerkki näkyviin
            return f"\n{self.nimi} ({self.maa})\n {self.ika} years, {self.pituus} cm, wingspan +{self.wingspan}, {self.paino} kg\n best ranking in 2019: {self.ranking}"
        else:   
            return f"\n{self.nimi} ({self.maa})\n {self.ika} years, {self.pituus} cm, wingspan {self.wingspan}, {self.paino} kg\n best ranking in 2019: {self.ranking}"
        
####  end  class Kilpailija ##############################################################


def luo_kilpailijat_miehet():
    # 20 miestä olympialaisissa 2021:
    kilpailijat["Sean McColl"] = Kilpailija("Sean McColl", 169, 60, 0, "Canada",33, "3rd (Lead)")    
    kilpailijat["Sean McColl"].painotukset(6, 8, 8) # arvosana 1-10 kunkin disciplinen taidoista, 10 = maailman paras
    kilpailijat["Alexey Rubtsov"] = Kilpailija("Alexey Rubtsov", 178, 63,0,"Russia", 32, "7th (Boulder)")
    kilpailijat["Alexey Rubtsov"].painotukset(4, 9, 4)
    kilpailijat["Jakob Schubert"] = Kilpailija("Jakob Schubert", 173, 63, 0,"Austria", 30, "10th (Boulder)")
    kilpailijat["Jakob Schubert"].painotukset(7, 10, 9)
    kilpailijat["Tomoa Narasaki"] = Kilpailija("Tomoa Narasaki", 170, 58,3, "Japan", 24, "1st (Boulder)") 
    kilpailijat["Tomoa Narasaki"].painotukset(9, 10, 7)
    kilpailijat["Kai Harada"] = Kilpailija("Kai Harada", 168, 51, 0,"Japan",22, "4th (Lead)")    
    kilpailijat["Kai Harada"].painotukset(9, 10, 7) 
    kilpailijat["Colin Duffy"] = Kilpailija("Colin Duffy", 168, 55, 4,"USA", 17, "-") 
    kilpailijat["Colin Duffy"] .painotukset(6, 9, 8)   
    kilpailijat["Nathaniel Coleman"] = Kilpailija("Nathaniel Coleman", 182, 74, 5,"USA",24, "20th (Boulder)")
    kilpailijat["Nathaniel Coleman"].painotukset(8, 8, 6)
    kilpailijat["Adam Ondra"] = Kilpailija("Adam Ondra", 186, 70, 12, "Czeck", 28, "1st (Lead)") 
    kilpailijat["Adam Ondra"].painotukset(4, 10, 10)
    kilpailijat["Jan Hojer"] = Kilpailija("Jan Hojer", 188, 77, 10, "Germany", 29,"6th (Boulder)")
    kilpailijat["Jan Hojer"].painotukset(6, 7, 8)
    kilpailijat["Rishat Khaibullin"] = Kilpailija("Rishat Khaibullin", 177, 66, -2, "Kazakhstan", 25, "29th (Speed)") 
    kilpailijat["Rishat Khaibullin"].painotukset(10, 2, 2)
    kilpailijat["Mickael Mawem"] = Kilpailija("Mickael Mawem", 177, 68, 7, "France", 30, "30th (Boulder)") 
    kilpailijat["Mickael Mawem"].painotukset(3, 8, 5)
    kilpailijat["Alexander Megos"] = Kilpailija("Alexander Megos", 173, 57, 8, "Germany", 28, "7th (Lead)") 
    kilpailijat["Alexander Megos"].painotukset(6, 8, 8)
    kilpailijat["Ludovico Fossali"] = Kilpailija("Ludovico Fossali", 177, 68, 2, "Italy", 24, "15th (Speed)") 
    kilpailijat["Ludovico Fossali"].painotukset(10, 2, 2)
    kilpailijat["Michael Piccolruaz"] = Kilpailija("Michael Piccolruaz", 177, 62, 3, "Italy", 25, "33rd (Boulder)")
    kilpailijat["Michael Piccolruaz"].painotukset(3, 7, 6)
    kilpailijat["Jongwon Chon"] = Kilpailija("Jongwon Chon", 176, 53, 10, "South Korea", 25, "4th (Boulder)")
    kilpailijat["Jongwon Chon"].painotukset(8, 10, 7)
    kilpailijat["Bassa Mawem"] = Kilpailija("Bassa Mawem", 177, 71, 2, "France", 36, "1st (Speed)")
    kilpailijat["Bassa Mawem"] .painotukset(10, 4, 5)
    kilpailijat["Alberto Ginéz López"] = Kilpailija("Alberto Ginéz López", 169, 58, 3,"Spain", 18,"2nd (Lead)")
    kilpailijat["Alberto Ginéz López"].painotukset(7, 6, 10)
    kilpailijat["Tom O'Halloran"] = Kilpailija("Tom O'Halloran", 177, 62, 4, "Australia", 28, "78th (Speed)")
    kilpailijat["Tom O'Halloran"].painotukset(8, 3, 4)
    kilpailijat["Christopher Cosser"] = Kilpailija("Christopher Cosser", 177, 71, -1, "South Africa", 20, "-")
    kilpailijat["Christopher Cosser"].painotukset(2, 2, 3)
    kilpailijat["YuFei Pan"] = Kilpailija("YuFei Pan", 170, 59, 1, "China", 20, "13th (Lead)")
    kilpailijat["YuFei Pan"].painotukset(5, 5, 8)



def luo_kilpailijat_naiset():
    # 20 naista olympialaisissa 2021:
    kilpailijat["Janja"] = Kilpailija("Janja Garnbret")    
    kilpailijat["Mia"] = Kilpailija("Mia Krampl")
    kilpailijat["Jessica"] = Kilpailija("Jessica Pilz") 
    kilpailijat["Petra"] = Kilpailija("Petra Kllinger") 
    kilpailijat["Julia"] = Kilpailija("Julia Chanourdie")     
    kilpailijat["Anouck"] = Kilpailija("Anouck Jaubert")
    kilpailijat["Miho"] = Kilpailija("Miho Nonaka") 
    kilpailijat["Akiyo"] = Kilpailija("Akiyo Noguchi") 
    kilpailijat["Alannah"] = Kilpailija("Alannah Yip") 
    kilpailijat["Brooke"] = Kilpailija("Brooke Raboutou") 
    kilpailijat["Kyra"] = Kilpailija("Kyra Condie") 
    kilpailijat["Shauna"] = Kilpailija("Shauna Coxey") 
    kilpailijat["Aleksandra"]  = Kilpailija("Aleksandra Miroslaw")
    kilpailijat["Chaehyun"] = Kilpailija("Chaehyun Seo")
    kilpailijat["Iuliia"] = Kilpailija("Iuliia Kaplina")
    kilpailijat["Viktoriia"] = Kilpailija("Viktoriia Meshkova")
    kilpailijat["Laura"] = Kilpailija("Laura Rogora")
    kilpailijat["YiLing"] = Kilpailija("YiLing Song")
    kilpailijat["Oceania"] = Kilpailija("Oceania MacKenzie")
    kilpailijat["Erin"] = Kilpailija("Erin Sterkenburg")

    kilpailijat["Janja"].anna_muut_tiedot(164, 47, 1, "Slovenia", 22, "1st (Boulder)")    
    kilpailijat["Mia"].anna_muut_tiedot(163, 51, 2, "Slovenia", 20, "9th (Lead)")
    kilpailijat["Jessica"].anna_muut_tiedot(163, 51, -2, "Austria", 24, "5th (Boulder)")
    kilpailijat["Petra"].anna_muut_tiedot(165, 54, 12, "Switzerland", 29, "6th (Boulder)")
    kilpailijat["Julia"].anna_muut_tiedot(166, 51, 2, "France", 24, "9th (Boulder)")    
    kilpailijat["Anouck"].anna_muut_tiedot(163, 51, 2, "France", 24, "2nd (Speed)")
    kilpailijat["Miho"].anna_muut_tiedot(162, 53, 2, "Japan", 23, "15th (Boulder)")
    kilpailijat["Akiyo"].anna_muut_tiedot(165, 49, 2, "Japan", 31, "2nd (Boulder)")
    kilpailijat["Alannah"].anna_muut_tiedot(166, 51, 2, "Canada", 27, "12th (Boulder)")
    kilpailijat["Brooke"].anna_muut_tiedot(157, 46, 3, "USA", 20, "46th (Lead)")
    kilpailijat["Kyra"].anna_muut_tiedot(163, 51, 2, "USA", 24, "18th (Boulder)")
    kilpailijat["Shauna"].anna_muut_tiedot(163, 51, 2, "Great Britain", 24, "11th (Boulder)")
    kilpailijat["Aleksandra"].anna_muut_tiedot(163, 51, 2, "Poland", 27, "9th (Speed)")
    kilpailijat["Chaehyun"].anna_muut_tiedot(163, 51, 2, "South Korea", 17, "1st (Lead)")
    kilpailijat["Iuliia"].anna_muut_tiedot(163, 51, 2, "Russia", 28, "10th (Speed)")
    kilpailijat["Viktoriia"].anna_muut_tiedot(163, 51, 2, "Russia", 20, "35th (Lead)")
    kilpailijat["Laura"].anna_muut_tiedot(163, 51, 2, "Italia", 20, "14th (Lead)")
    kilpailijat["YiLing"].anna_muut_tiedot(163, 51, 2, "China", 24, "1st (Speed)")
    kilpailijat["Oceania"].anna_muut_tiedot(163, 51, 2, "Australia", 18, "26th (Boulder)")
    kilpailijat["Erin"].anna_muut_tiedot(163, 51, 2, "South Africa", 18, "-")
    

def kilpailu():
    global tulokset
    #   K A R S I N T A : 
    speedKilpailu = speed.SpeedKilpailu()
    sij = 1  # eka sijoitus = 1
    for tulos in speedKilpailu.speed_karsinta(kilpailijat)  :
        t = kokonaistulos.Kokonaistulos(tulos.kilpailija, sij) 
        tulokset[tulos.nimi] = t # ei tasasijoituksia
        sij += 1

    boulderKilpailu = boulder.BoulderKilpailu()
    sij = 1
    for tulos in boulderKilpailu.tulos_karsinta(kilpailijat): 
        t = tulokset[tulos.nimi]    # ei tasasijoituksia
        t.lisaa_boulder(sij)
        sij += 1

    leadKilpailu  = lead.LeadKilpailu()
    karsintatulokset = leadKilpailu.tulos_karsinta(kilpailijat)
    print("\nL E A D -- KARSINTA")
    for tulos in leadKilpailu.jarjesta_sijoitukset(karsintatulokset) :
        t = tulokset[tulos[0].nimi]    
        t.lisaa_lead(tulos[1])   # täällä saattaa olla tasasijoituksia, eri systeemi kuin speed/lead
        


    def printtaa_tulokset(karsinta_vai_finaali):
        koktulos = tulokset.values()
        if karsinta_vai_finaali == "FINAALI -- TOTAL POINTS":
            s = sorted(koktulos, key=lambda tulos: (tulos.yhteispisteet(), -tulos.voitot(), tulos.yhteenlasketut_pisteet(), tulos.karsinnansijoitus))
        else:
            s = sorted(koktulos, key=lambda tulos: (tulos.yhteispisteet(), -tulos.voitot(), tulos.yhteenlasketut_pisteet()))
        climber ="CLIMBER"
        lead = "LEAD"
        speed = "SPEED"
        boulder = "BOULDER"
        total = "TOTAL"
        print("\n"+karsinta_vai_finaali)
        print(f"{climber:28} {speed:<8}  {boulder:<8}  {lead:<8} {total:<8} ")
        print("-"*63)
        sijoitus = 1
        for koktulos in s:
            climber = koktulos.nimi        
            speed = koktulos.speed
            boulder = koktulos.boulder
            lead = koktulos.lead
            total = koktulos.yhteispisteet()
            print(f"{climber:28} {speed:<8}  {boulder:<8}  {lead:<8} {total:<8} ")
            koktulos.karsinnan_sij = sijoitus
            sijoitus += 1
        return s[:8]


    karsintatulos = printtaa_tulokset("KARSINTA -- TOTAL POINTS")


    #  F I N A A L I   8 PARASTA
    print("\nS P E E D -- FINAALI")
    tulokset_karsinta = tulokset
    tulokset = {}
    sij = 1  # eka sijoitus = 1
    for tulos in speedKilpailu.speed_finaali(karsintatulos):    
        print(tulos) 
        t = kokonaistulos.Kokonaistulos(tulos.kilpailija, sij) 
        tulokset[tulos.nimi] = t # ei tasasijoituksia
        sij += 1

    sij = 1
    print("\nB O U L D E R -- FINAALI")
    for tulos in boulderKilpailu.tulos_finaali(karsintatulos, kilpailijat) :      
        print(tulos) 
        t = tulokset[tulos.nimi]    # ei tasasijoituksia
        t.lisaa_boulder(sij)
        sij += 1

    print("\nL E A D -- FINAALI")
    for tulos in leadKilpailu.jarjesta_sijoitukset(leadKilpailu.pisteet_finaali(karsintatulos, kilpailijat)):    
        t = tulokset[tulos[0].nimi]    
        t.lisaa_lead(tulos[1])   # täällä saattaa olla tasasijoituksia, eri systeemi kuin speed/lead
        

    printtaa_tulokset("FINAALI -- TOTAL POINTS")



kilpailijat = {}  # nimi : Kilpailija
tulokset =  {}   #  nimi : Kokonaistulos

print("\n 1  Naisten kilpailu")
print("\n 2  Miesten kilpailu")
print("\n 3  20 naiskilpailijan tiedot")
print("\n 4  20 miesskilpailijan tiedot")
vastaus = input("\nMitä tehdään? Anna numero 1-4 ")
if vastaus == "1":
    luo_kilpailijat_naiset()
    kilpailu()
elif vastaus == "2":    
    luo_kilpailijat_miehet()
    kilpailu()
elif vastaus == "3": 
    luo_kilpailijat_naiset()
    for nimi, kilpailija in kilpailijat.items():
        print(kilpailija)
elif vastaus == "4":   
    luo_kilpailijat_miehet()
    for nimi, kilpailija in kilpailijat.items():
        print(kilpailija)  
