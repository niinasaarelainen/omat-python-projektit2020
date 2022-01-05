
stringi = ""
vastaus = ""



def readfile():
    global stringi
    f = open("data.txt", "r") 
    for rivi in f:
        stringi = rivi.strip()


def react(rivi):
    uusi_lista = list(rivi)
    
    for i in range(len(rivi) - 1):
        pari = [rivi[i], rivi[i + 1]]
        lower =  [item for item in pari if item.islower()]
        if len(lower) == 1 and rivi[i].lower() == rivi[i + 1].lower():
            uusi_lista[i] = ""
            uusi_lista[i + 1] = ""
            break
    
    uusi_rivi = "".join(uusi_lista)
    return  uusi_rivi             
 

def poista(kirjain):
    global stringi
    uusi_s = stringi
    pienet = stringi.count(kirjain.lower())
    isot = stringi.count(kirjain)
    minimi = min(pienet, isot)
    for i in range(minimi):
        uusi_s = uusi_s.replace(kirjain, "")
        uusi_s = uusi_s.replace(kirjain.lower(), "")
    return uusi_s

  
readfile()
setti = set(stringi)

stringit = []
for kirjain in sorted(list(setti))[:len(setti)//2]:
    uusi_s = poista(kirjain)
    for i in range(49800):
        uusi_s = react(uusi_s) 
    stringit.append(uusi_s)

lyhyin = min([(len(s), s) for s in stringit])
print(lyhyin)
 
 
 