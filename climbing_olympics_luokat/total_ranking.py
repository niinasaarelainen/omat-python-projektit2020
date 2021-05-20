import speed, boulder, lead, kokonaistulos
from operator import itemgetter

class Kilpailija:

    def __init__(self, nimi):
        self.nimi = nimi
        self.pituus = None
        self.paino = None
        self.wingspan = None
        self.maa = None
        self.ika = None

    def anna_muut_tiedot(self, pituus, paino, wingspan, maa, ika):
        self.pituus = pituus
        self.paino = paino
        self.wingspan = wingspan
        self.maa = maa
        self.ika = ika

    def __str__(self):
        if self.wingspan > 0:                                                 # halutaan plusmerkki näkyviin
            return f"\n{self.nimi} ({self.maa})\n{self.ika} vuotta, {self.pituus} cm, wingspan +{self.wingspan}, {self.paino} kg"
        else:   
            return f"\n{self.nimi} ({self.maa})\n{self.ika} vuotta, {self.pituus} cm, wingspan {self.wingspan}, {self.paino} kg"
        


def luo_kilpailijat():
    # 20 naista:
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

    kilpailijat["Janja"].anna_muut_tiedot(164, 47, 1, "Slovenia", 22)    
    kilpailijat["Mia"].anna_muut_tiedot(163, 51, 2, "Slovenia", 24)
    kilpailijat["Jessica"].anna_muut_tiedot(163, 51, -2, "Austria", 24)
    kilpailijat["Petra"].anna_muut_tiedot(165, 54, 12, "Switzerland", 29)
    kilpailijat["Julia"].anna_muut_tiedot(166, 51, 2, "France", 28)    
    kilpailijat["Anouck"].anna_muut_tiedot(163, 51, 2, "France", 24)
    kilpailijat["Miho"].anna_muut_tiedot(162, 53, 2, "Japan", 23)
    kilpailijat["Akiyo"].anna_muut_tiedot(165, 49, 2, "Japan", 31)
    kilpailijat["Alannah"].anna_muut_tiedot(166, 51, 2, "Canada", 27)
    kilpailijat["Brooke"].anna_muut_tiedot(157, 46, 3, "USA", 20)
    kilpailijat["Kyra"].anna_muut_tiedot(163, 51, 2, "USA", 24)
    kilpailijat["Shauna"].anna_muut_tiedot(163, 51, 2, "Great Britain", 24)
    kilpailijat["Aleksandra"].anna_muut_tiedot(163, 51, 2, "Poland", 24)
    kilpailijat["Chaehyun"].anna_muut_tiedot(163, 51, 2, "South Korea", 24)
    kilpailijat["Iuliia"].anna_muut_tiedot(163, 51, 2, "Russia", 24)
    kilpailijat["Viktoriia"].anna_muut_tiedot(163, 51, 2, "Russia", 24)
    kilpailijat["Laura"].anna_muut_tiedot(163, 51, 2, "Italia", 24)
    kilpailijat["YiLing"].anna_muut_tiedot(163, 51, 2, "China", 24)
    kilpailijat["Oceania"].anna_muut_tiedot(163, 51, 2, "Australia", 24)
    kilpailijat["Erin"].anna_muut_tiedot(163, 51, 2, "South Africa", 24)
    
    #for nimi, kilpailija in kilpailijat.items():
    #    print(kilpailija)


kilpailijat = {}  # nimi : Kilpailija
luo_kilpailijat()
tulokset =  {}   #  nimi : Kokonaistulos

#   K A R S I N T A : 
speedKilpailu = speed.SpeedKilpailu()
sij = 1  # eka sijoitus = 1
for tulos in speedKilpailu.speed_karsinta(kilpailijat)  :
    t = kokonaistulos.Kokonaistulos(tulos.kilpailija, sij) 
    print("tulos.nimi", tulos.nimi)
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
    print(f"{climber:18} {speed:<8}  {boulder:<8}  {lead:<8} {total:<8} ")
    print("-"*56)
    sijoitus = 1
    for koktulos in s:
        climber = koktulos.nimi        
        speed = koktulos.speed
        boulder = koktulos.boulder
        lead = koktulos.lead
        total = koktulos.yhteispisteet()
        print(f"{climber:18} {speed:<8}  {boulder:<8}  {lead:<8} {total:<8} ")
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
for tulos in boulderKilpailu.tulos_finaali(karsintatulos) :      
    print(tulos) 
    t = tulokset[tulos.nimi]    # ei tasasijoituksia
    t.lisaa_boulder(sij)
    sij += 1

print("\nL E A D -- FINAALI")
for tulos in leadKilpailu.jarjesta_sijoitukset(leadKilpailu.pisteet_finaali(karsintatulos)):    
    t = tulokset[tulos[0].nimi]    
    t.lisaa_lead(tulos[1])   # täällä saattaa olla tasasijoituksia, eri systeemi kuin speed/lead
    

printtaa_tulokset("FINAALI -- TOTAL POINTS")
