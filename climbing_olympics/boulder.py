import operator, random


def pisteet_karsinta():     
    pisteet = []
    pisteet.append(["Janja", "T1", "Z1", "T2", "Z1", "Z1"]) # 3 boulderia, vikasta ei toppia
    pisteet.append(["Jain", "T10", "Z1", "T2", "Z1", "Z6"])
    pisteet.append(["Jessica", "T3", "Z1", "T5", "Z1", "Z7"])
    pisteet.append(["Alex", "T2", "Z1", "Z1", "Z12"])
    pisteet.append(["AlexPlus", "T2", "Z1", "Z1", "Z3"])
    pisteet.append(["AlexHidas", "T2", "Z1", "Z1", "Z1"])
    pisteet.append(["Julia", "T3", "Z1", "T5", "Z1", "Z9"])
    pisteet.append(["Ihmelapsi", "Z1", "Z1", "Z12"])
    pisteet.append(["Anna", "T4","Z1", "Z1", "Z12"])
    pisteet.append(["Margo", "T5", "Z1", "Z1", "Z12"])    
        
    tulokset = []   # järjestämätön data    
    for tulos in pisteet:
        topit_lkm = 0
        topit_yritykset = 0
        zonet_lkm = 0
        zonet_yritykset = 0
        for piste in tulos[1:]:  
            if "T" in piste:
                topit_lkm += 1
                topit_yritykset += int(piste[1:])
            elif "Z" in piste:   
                zonet_lkm += 1
                zonet_yritykset += int(piste[1:])      
        tulokset.append([tulos[0], topit_lkm, topit_yritykset, zonet_lkm, zonet_yritykset])  

    s = sorted(tulokset, key=lambda s: (-s[1], s[2], -s[3], s[4],) )  
    return s

def pisteet_finaali(sijoitukset):
    pisteet = []
    for i in range(8):
        topit_lkm = random.randint(0,3)
        topit_yritykset = random.randint(3, 20)
        zonet_lkm = random.randint(topit_lkm,3)
        zonet_yritykset = random.randint(3, 30)
        pisteet.append([sijoitukset[i][0], topit_lkm, topit_yritykset, zonet_lkm, zonet_yritykset])  
    s = sorted(pisteet, key=lambda s: (-s[1], s[2], -s[3], s[4],) )   
    return s

def jarjesta_dictiin(lista, ind):
    dict = {}
    for tulos in lista:
        if tulos[ind] in dict:
            dict[tulos[ind]].append(tulos)
        else:
            dict[tulos[ind]] = []    
            dict[tulos[ind]].append(tulos)
    return dict

 

karsintatulos = pisteet_karsinta()
print("\nB O U L D E R -- KARSINTA")
for tulos in karsintatulos:
    if tulos[1] == 0:
        pr = f"{tulos[0]}: {tulos[3]}Z{tulos[4]}"   # ei toppeja
    else:
        pr = f"{tulos[0]}: {tulos[1]}T{tulos[2]}, {tulos[3]}Z{tulos[4]}"
    print(pr) 





""" ilman lambadaa, ei mene oikein !!!

def onko_samoja_tuloksia(lista, ind):
    edellinen = lista[0]
    for tulos in lista[1:]:
        if edellinen[ind] == tulos[ind]:            
            #print("onko_samoja_tuloksia", tulos)
            return True
    return False


tulokset.sort(key=operator.itemgetter(1))
tulokset.reverse()

topit= jarjesta_dictiin(tulokset, 1)

    #print("topit:", topit)        

    the_tulos = []    # järjestetty data
    for t in range(3,-1, -1):   # 0-3 toppia
        if t in topit:
            topit[t].sort(key=operator.itemgetter(2))
            if len(topit[t]) > 1 and onko_samoja_tuloksia(topit[t], 2):
                topit_yrkat= jarjesta_dictiin(topit[t], 2)
                for ty in range(30,0, -1):    # sovitaan että ei ehdi tehdä enempää kuin 30 yritystä
                    if ty in topit_yrkat:
                        topit_yrkat[ty].sort(key=operator.itemgetter(3))
                        if len(topit[t]) > 1 and onko_samoja_tuloksia(topit[t], 2):
                            topit_yrkat= jarjesta_dictiin(topit[t], 2)
                            zonet= jarjesta_dictiin(topit_yrkat[ty], 3)
                            for z in range(3,-1, -1):    # 3 reittiä -->  3 zonea max
                                if z in zonet:
                                    zonet[z].sort(key=operator.itemgetter(4)) 
                                    the_tulos += zonet[z]    
                        else:     
                            the_tulos += topit_yrkat[ty]  
            else:
                the_tulos += topit[t]    

"""                