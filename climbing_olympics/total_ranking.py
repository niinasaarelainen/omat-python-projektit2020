import speed, boulder, lead, tkinter
from operator import itemgetter

# tkinter.

#   K A R S I N T A : 
tulokset = {}
i = 1  # eka sijoitus = 1
for tulos in speed.speed_karsinta():
    tulokset[tulos[0]] = []
    tulokset[tulos[0]].append(i)   # ei tasasijoituksia
    i += 1

i = 1
for tulos in boulder.karsintatulos:    
    tulokset[tulos[0]].append(i)    # ei tasasijoituksia
    i += 1

for tulos in lead.karsintatulos:    
    tulokset[tulos[0]].append(tulos[1]+1)   # täällä saattaa olla tasasijoituksia
    

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
printtaa_tulokset(sijoitukset, "KARSINTA")


#  F I N A A L I

tulokset = {}
i = 1  # eka sijoitus = 1
for tulos in speed.speed_finaali(sijoitukset[:8]):
    tulokset[tulos[0]] = []
    tulokset[tulos[0]].append(i)   # ei tasasijoituksia
    i += 1

i = 1
for tulos in boulder.pisteet_finaali(sijoitukset[:8]) :  
    tulokset[tulos[0]].append(i)    # ei tasasijoituksia
    i += 1

for tulos in lead.tulokset(lead.pisteet_finaali(sijoitukset[:8])):    
    tulokset[tulos[0]].append(tulos[1]+1)   # täällä saattaa olla tasasijoituksia
    

sijoitukset = []
for nimi, sij in tulokset.items():
    sijoitukset.append([nimi, sij, sij[0] * sij[1] * sij[2]])

sijoitukset.sort(key=itemgetter(2))
printtaa_tulokset(sijoitukset, "FINAALI")