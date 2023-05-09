
import itertools


data = []
distances = {}


def readfile():
    f = open("data_1.txt", "r") 
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
    keys = distances.keys()
    kilometrit = []

    for p in permut:
        for i in p:
            km = 0   
            values = distances[p[i]]
            for v in values:
                print("v[0]", v[0], "town", town)
                if v[0] == town:
                    km += v[1]

            kilometrit.append(km)
            print(p)

    pienin = sorted(kilometrit)[0]
    print(pienin)



readfile()
modostaHash()
tutki()    # 358   too high
