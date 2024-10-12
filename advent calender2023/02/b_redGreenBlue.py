from functools import reduce

data = []
pallot = {}

def readfile():
    f = open("data_1.txt", "r") 
    for rivi in f:
        rivi = rivi.replace(",", "").replace(";", "")
        data.append(rivi.strip().split(":"))   

def makeHash():
    for rivi in data:
        game, nro = rivi[0].split(" ")
        pallot[int(nro)] = rivi[1].strip()

def tutki():   
    tulos = 0               # fewest number of cubes of each color, but not over 12
    
    for ind in pallot:
        rivin_maksimit = []
        maarat = {"red": [], "green": [], "blue": []}  
        sp = pallot[ind].split(" ")

        for i in range(0, len(sp), 2):  # 2 = joka toinen alkio
            maarat[sp[i+1]].append(int(sp[i]))   #  esim. "blue": [3]

        for k, v in maarat.items():
            rivin_maksimit.append(max(v))    # pitää olla maksimi, koska pitää pystyä ottamaan sen verran, minimi ei riitä
            #print("rivin_maksimit", rivin_maksimit)

        mul = reduce((lambda x, y: x * y), rivin_maksimit)
        tulos += mul

    return tulos

readfile() 
makeHash()
print(pallot)
result = tutki()
print(result)