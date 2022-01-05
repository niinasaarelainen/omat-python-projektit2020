
data = []
eroja_min = 1000


def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi.strip())


def samankaltaiset():
    global data
    vastaus = ""
        
    strings = tutki(data)    
    print(strings)
    for i in range(len(strings[0])):
        if strings[0][i] == strings[1][i]:   # huom vertailu pitää tehdä näin  strings[0][i] in strings[1][i] --> väärin 
            vastaus += strings[0][i]

    return vastaus


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




readfile()
print(samankaltaiset())
 
