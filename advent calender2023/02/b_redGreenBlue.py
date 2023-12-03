from functools import reduce

data = []
pallot = {}

def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        rivi = rivi.replace(",", "").replace(";", "")
        data.append(rivi.strip().split(":"))   

def makeHash():
    for rivi in data:
        game, nro = rivi[0].split(" ")
        pallot[int(nro)] = rivi[1].strip()

def tutki():   
    tulos = 0 
    
    for ind in pallot:
        rivin_maksimit = []
        min = {"red": [], "green": [], "blue": []}  
        sp = pallot[ind].split(" ")

        for i in range(0, len(sp), 2):  # 2 = joka toinen alkio
            min[sp[i+1]].append(int(sp[i]))

        for k, v in min.items():
            rivin_maksimit.append(max(v))

        mul = reduce((lambda x, y: x * y), rivin_maksimit)
        tulos += mul

    return tulos

readfile() 
makeHash()
result = tutki()
print(result)