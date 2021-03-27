import speed, boulder, lead
from operator import itemgetter


#   K A R S I N T A : 
speedKilpailu = speed.SpeedKilpailu()
tulokset = {}
i = 1  # eka sijoitus = 1
for tulos in speedKilpailu.speed_karsinta()  :
    tulokset[tulos.nimi] = []
    tulokset[tulos.nimi].append(i)   # ei tasasijoituksia
    i += 1

boulderKilpailu = boulder.BoulderKilpailu()
i = 1
for tulos in boulderKilpailu.tulos_karsinta():    
    tulokset[tulos.nimi].append(i)    # ei tasasijoituksia
    i += 1

leadKilpailu  = lead.LeadKilpailu()
karsintatulokset = leadKilpailu.tulos_karsinta()
print("\nL E A D -- KARSINTA")
for tulos in leadKilpailu.jarjesta_sijoitukset(karsintatulokset) :
    tulokset[tulos[0].nimi].append(tulos[1])   # täällä saattaa olla tasasijoituksia
    

sijoitukset = []
for nimi, sij in tulokset.items():
    sijoitukset.append([nimi, sij, sij[0] * sij[1] * sij[2]])



def printtaa_tulokset(sijoitukset, karsinta_vai_finaali):
    climber ="CLIMBER"
    lead = "LEAD"
    speed = "SPEED"
    boulder = "BOULDER"
    total = "TOTAL"
    print("\n"+karsinta_vai_finaali)
    print(f"{climber:18} {speed:>8}  {boulder:>8}  {lead:>8} {total:>8} ")
    print("-"*56)
    for tyyppi in sijoitukset:
        climber = tyyppi[0]
        speed = tyyppi[1][0]
        boulder = tyyppi[1][1]
        lead = tyyppi[1][2]
        total = tyyppi[2]
        print(f"{climber:18} {speed:>8}  {boulder:>8}  {lead:>8} {total:>8} ")


sijoitukset.sort(key=itemgetter(2))
printtaa_tulokset(sijoitukset, "KARSINTA -- TOTAL POINTS")


#  F I N A A L I   8 PARASTA
print("\nS P E E D -- FINAALI")
tulokset = {}
i = 1  # eka sijoitus = 1
for tulos in speedKilpailu.speed_finaali(sijoitukset[:8]):
    
    print(tulos) 
    tulokset[tulos.nimi] = []
    tulokset[tulos.nimi].append(i)   # ei tasasijoituksia
    i += 1

i = 1
print("\nB O U L D E R -- FINAALI")
for tulos in boulderKilpailu.tulos_finaali(sijoitukset[:8]) :      
    print(tulos) 
    tulokset[tulos.nimi].append(i)    # ei tasasijoituksia
    i += 1

print("\nL E A D -- FINAALI")
for tulos in leadKilpailu.jarjesta_sijoitukset(leadKilpailu.pisteet_finaali(sijoitukset[:8])):    
    tulokset[tulos[0].nimi].append(tulos[1])   # täällä saattaa olla tasasijoituksia
    

sijoitukset = []
for nimi, sij in tulokset.items():
    sijoitukset.append([nimi, sij, sij[0] * sij[1] * sij[2]])

sijoitukset.sort(key=itemgetter(2))
printtaa_tulokset(sijoitukset, "FINAALI -- TOTAL POINTS")
