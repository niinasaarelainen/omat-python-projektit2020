
stringi = ""
stringi_jaettava = ""
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
 

    
# dabCBAcaDA   oma
# dabCBAcaDA    oikea v    

readfile()
stringi_jaettava = stringi[:10000]
for i in range(10000):
    stringi_jaettava = react(stringi_jaettava) 
print(stringi_jaettava)
vastaus += stringi_jaettava

stringi_jaettava = stringi[10000:20000]
for i in range(10009):
    stringi_jaettava = react(stringi_jaettava) 
print(stringi_jaettava)
vastaus += stringi_jaettava

stringi_jaettava = stringi[20000:30000]
for i in range(10009):
    stringi_jaettava = react(stringi_jaettava) 
print(stringi_jaettava)
vastaus += stringi_jaettava

stringi_jaettava = stringi[30000:40000]
for i in range(10009):
    stringi_jaettava = react(stringi_jaettava) 
print(stringi_jaettava)
vastaus += stringi_jaettava
 
stringi_jaettava = stringi[40000:]
for i in range(10009):
    stringi_jaettava = react(stringi_jaettava) 
print(stringi_jaettava)
vastaus += stringi_jaettava

print(len(vastaus))   # 11756 too high
 
 
 