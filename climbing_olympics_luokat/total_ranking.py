import speed, boulder, lead, kokonaistulos
from operator import itemgetter


tulokset =  {}   #  nimi : Kokonaistulos

#   K A R S I N T A : 
speedKilpailu = speed.SpeedKilpailu()
sij = 1  # eka sijoitus = 1
for tulos in speedKilpailu.speed_karsinta()  :
    t = kokonaistulos.Kokonaistulos(tulos.nimi, sij) 
    tulokset[tulos.nimi] = t # ei tasasijoituksia
    sij += 1

boulderKilpailu = boulder.BoulderKilpailu()
sij = 1
for tulos in boulderKilpailu.tulos_karsinta():    
    t = tulokset[tulos.nimi]    # ei tasasijoituksia
    t.lisaa_boulder(sij)
    sij += 1

leadKilpailu  = lead.LeadKilpailu()
karsintatulokset = leadKilpailu.tulos_karsinta()
print("\nL E A D -- KARSINTA")
for tulos in leadKilpailu.jarjesta_sijoitukset(karsintatulokset) :
    t = tulokset[tulos[0].nimi]    
    t.lisaa_lead(tulos[1])   # täällä saattaa olla tasasijoituksia, eri systeemi kuin speed/lead
    


def printtaa_tulokset(karsinta_vai_finaali):
    koktulos = tulokset.values()
    s = sorted(koktulos, key=lambda tulos: (tulos.yhteispisteet(), -tulos.voitot()))
    climber ="CLIMBER"
    lead = "LEAD"
    speed = "SPEED"
    boulder = "BOULDER"
    total = "TOTAL"
    print("\n"+karsinta_vai_finaali)
    print(f"{climber:18} {speed:>8}  {boulder:>8}  {lead:>8} {total:>8} ")
    print("-"*56)
    for koktulos in s:
        climber = koktulos.nimi
        speed = koktulos.speed
        boulder = koktulos.boulder
        lead = koktulos.lead
        total = koktulos.yhteispisteet()
        print(f"{climber:18} {speed:>8}  {boulder:>8}  {lead:>8} {total:>8} ")
    return s[:8]


karsintatulos = printtaa_tulokset("KARSINTA -- TOTAL POINTS")
print(karsintatulos)


#  F I N A A L I   8 PARASTA
print("\nS P E E D -- FINAALI")
tulokset = {}
sij = 1  # eka sijoitus = 1
for tulos in speedKilpailu.speed_finaali(karsintatulos):    
    print(tulos) 
    t = kokonaistulos.Kokonaistulos(tulos.nimi, sij) 
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
    

printtaa_tulokset( "FINAALI -- TOTAL POINTS")
