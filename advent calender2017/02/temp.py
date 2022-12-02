# tässä oletus että samankaltaisimmilla olisi sama 1. kirjain

def samankaltaiset():
    global data
    eroja = 1000
    
    alkukirjaimittain = {}
    

    for rivi in data:
        if rivi[0] in alkukirjaimittain:
            alkukirjaimittain[rivi[0]].append(rivi)
        else:
            alkukirjaimittain[rivi[0]] = []
            alkukirjaimittain[rivi[0]].append(rivi)

   
    print(alkukirjaimittain)

    for key in alkukirjaimittain:
        print(key)
        if len(alkukirjaimittain[key]) > 1:
            tulos =  tutki(alkukirjaimittain[key]) 
            if tulos != None:
                strings = tulos    
    
    vastaus =  [kirjain for kirjain in strings[0] if kirjain in strings[1]]

    return "".join(vastaus)

def tutki(lista):
    global eroja_min
    strings = []
    
    for verrokki in lista:        
        for vertaa_tahan in lista:
            eroja = 0
            if verrokki != vertaa_tahan:
                for i in range(len(verrokki)):
                   # print(verrokki[i], vertaa_tahan[i])
                    if verrokki[i] != vertaa_tahan[i]:
                        eroja += 1
            if eroja < eroja_min and eroja != 0:
                eroja_min = eroja
                print("eroja_min", eroja_min)
                strings = []
                strings.append(vertaa_tahan)
                strings.append(verrokki)
                return strings
    return None