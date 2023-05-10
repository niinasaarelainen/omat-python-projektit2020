import itertools

data = []
distances = {}


def readfile():
    f = open("data.txt", "r") 
    for rivi in f:
        data.append(rivi.strip().replace("to", "="))

def modostaHash():
    for rivi in data:
        start, end, km = rivi.split(" = ")
        km = int(km)
        if start not in distances:
            distances[start] = [[end, km]]
        else: 
            distances[start].append([end, km])
        if end not in distances:
            distances[end] = [[start, km]]
        else: 
            distances[end].append([start, km])



def tutki():

    permut = list(itertools.permutations(distances.keys()))
    kilometrit = []

    for p in permut:
        km = 0 
        for i in range(len(p)-1):             
            town = p[i]
            values = distances[town]
            for v in values:
                #print("v[0]", v[0], "town", town)
                if v[0] == p[i+1]:                    
                    km += v[1]

        kilometrit.append(km)

    print(kilometrit)
    pisin = sorted(kilometrit)[-1]
    print(pisin)



readfile()
modostaHash()
tutki()    # 358   too high, 207 oikein
