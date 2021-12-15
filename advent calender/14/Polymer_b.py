data = []
lahtokohta = ""
muunnokset = {}
kahden_sarjat = {}
maarat = {}

def readfile():   # b-kohta
    global data, lahtokohta, muunnokset
    f = open("data_easy.txt", "r")         
    for rivi in f:
        if "->" in rivi:
            key, value = rivi.split("->")
            muunnokset[key.strip()] = value.strip()
        elif rivi.strip() == "":
            continue
        else:
            lahtokohta = rivi.strip()
            tee_kaksoset(lahtokohta)

def tee_kaksoset(lahtokohta):
    pit = len(lahtokohta)
    for i in range(pit - 1):
        kahden_sarjat[lahtokohta[i:i+2]] = 1
    
    print(kahden_sarjat)




def muunna():
    global muunnokset, kahden_sarjat
    uusi_kahden_sarjat = {}
    for sarja in kahden_sarjat:
        uusi_kirjain = muunnokset[sarja]
        uusi_kaksonen1 = sarja[0] + uusi_kirjain
        uusi_kaksonen2 = uusi_kirjain + sarja[1] 
        print("uusi_kaksonen1", uusi_kaksonen1, "uusi_kaksonen2", uusi_kaksonen2)
        if uusi_kaksonen1 not in uusi_kahden_sarjat:
            uusi_kahden_sarjat[uusi_kaksonen1] = 1
        else:
            uusi_kahden_sarjat[uusi_kaksonen1] += 1
        if uusi_kaksonen2 not in uusi_kahden_sarjat:
            uusi_kahden_sarjat[uusi_kaksonen2] = 1
        else:
            uusi_kahden_sarjat[uusi_kaksonen2] += 1

    kahden_sarjat = uusi_kahden_sarjat

    print("kahden_sarjat@muunna end", kahden_sarjat)


def laske():
    global kahden_sarjat
    for sarja in kahden_sarjat:
        #print("sarja", sarja, "kahden_sarjat[sarja]", kahden_sarjat[sarja])
        if sarja[0] not in maarat:
            maarat[sarja[0]] = kahden_sarjat[sarja]
        else:
            maarat[sarja[0]] += kahden_sarjat[sarja]
        if sarja[1] not in maarat:
            maarat[sarja[1]] = kahden_sarjat[sarja]
        else:
            maarat[sarja[1]] += kahden_sarjat[sarja]    

    print("maarat", maarat)
    mi = min(maarat.values())
    ma = max(maarat.values())
    print(ma - mi)


readfile()
#print(muunnokset, lahtokohta)


for i in range(3):
    muunna()


laske()  